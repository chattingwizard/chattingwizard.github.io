#!/usr/bin/env python3
"""
Slack CLI — Full admin control of Slack AS YOUR OWN ACCOUNT.
Uses a User OAuth Token (xoxp-) so all actions happen as you, not a bot.

Usage:
    python3 slack_cli.py auth-test                              # Verify connection
    python3 slack_cli.py channels                               # List channels
    python3 slack_cli.py read <channel> [--limit N]             # Read recent messages
    python3 slack_cli.py send <channel> <message>               # Send a message as you
    python3 slack_cli.py dms                                    # List DM conversations
    python3 slack_cli.py read-dm <user> [--limit N]             # Read DMs (by name or ID)
    python3 slack_cli.py send-dm <user> <message>               # Send DM as you
    python3 slack_cli.py users                                  # List workspace users
    python3 slack_cli.py search <query> [--limit N]             # Search messages

    # Admin / channel management
    python3 slack_cli.py create-channel <name> [--private]      # Create a channel
    python3 slack_cli.py archive-channel <channel>              # Archive a channel
    python3 slack_cli.py rename-channel <channel> <new_name>    # Rename a channel
    python3 slack_cli.py set-topic <channel> <topic>            # Set channel topic
    python3 slack_cli.py set-purpose <channel> <purpose>        # Set channel purpose
    python3 slack_cli.py invite <channel> <user>                # Invite user to channel
    python3 slack_cli.py kick <channel> <user>                  # Remove user from channel

    # User admin
    python3 slack_cli.py user-info <user>                       # Detailed user info
    python3 slack_cli.py deactivate-user <user_id>              # Deactivate a user (admin)

    # Reactions & pins
    python3 slack_cli.py react <channel> <timestamp> <emoji>    # Add reaction
    python3 slack_cli.py pin <channel> <timestamp>              # Pin a message
    python3 slack_cli.py unpin <channel> <timestamp>            # Unpin a message

    # Files
    python3 slack_cli.py upload <channel> <filepath> [--title]  # Upload a file
    python3 slack_cli.py files <channel> [--limit N]            # List files in channel

    # Reminders
    python3 slack_cli.py remind <user> <text> <time>            # Set a reminder

Env var required: SLACK_USER_TOKEN (xoxp-...)
"""

import argparse
import os
import sys
from datetime import datetime

try:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
except ImportError:
    print("ERROR: slack_sdk not installed. Run: pip3 install slack_sdk")
    sys.exit(1)


TOKEN_ENV = "SLACK_USER_TOKEN"


def get_client():
    token = os.environ.get(TOKEN_ENV)
    if not token:
        print(f"ERROR: {TOKEN_ENV} not set.")
        print(f"Export it: export {TOKEN_ENV}=xoxp-your-token-here")
        sys.exit(1)
    return WebClient(token=token)


# ── User cache ───────────────────────────────────────────────────────────────

_user_cache = {}


def _populate_user_cache(client):
    global _user_cache
    if _user_cache:
        return
    try:
        result = client.users_list(limit=500)
        for m in result["members"]:
            name = m.get("real_name") or m.get("name") or m["id"]
            _user_cache[m["id"]] = name
            if m.get("name"):
                _user_cache[f"@{m['name'].lower()}"] = m["id"]
            if m.get("real_name"):
                _user_cache[f"@{m['real_name'].lower()}"] = m["id"]
            display = m.get("profile", {}).get("display_name", "")
            if display:
                _user_cache[f"@{display.lower()}"] = m["id"]
    except SlackApiError:
        pass


def resolve_user_name(client, user_id):
    _populate_user_cache(client)
    return _user_cache.get(user_id, user_id)


def resolve_user_id(client, user_ref):
    if user_ref.startswith("U") and len(user_ref) >= 9 and user_ref.isalnum():
        return user_ref
    _populate_user_cache(client)
    key = f"@{user_ref.lstrip('@').lower()}"
    if key in _user_cache:
        val = _user_cache[key]
        if val.startswith("U") and len(val) >= 9:
            return val
    search = user_ref.lstrip("@").lower()
    for k, v in _user_cache.items():
        if k.startswith("@") and search in k:
            if v.startswith("U") and len(v) >= 9:
                return v
    print(f"Error: User '{user_ref}' not found.")
    sys.exit(1)


# ── Helpers ──────────────────────────────────────────────────────────────────

def resolve_channel(client, channel_ref):
    if channel_ref.startswith("C") and len(channel_ref) >= 9:
        return channel_ref
    name = channel_ref.lstrip("#")
    try:
        try:
            result = client.conversations_list(
                types="public_channel,private_channel", limit=500, exclude_archived=True
            )
        except SlackApiError:
            result = client.conversations_list(
                types="public_channel", limit=500, exclude_archived=True
            )
        for ch in result["channels"]:
            if ch["name"] == name:
                return ch["id"]
    except SlackApiError:
        pass
    print(f"Error: Channel '{channel_ref}' not found.")
    sys.exit(1)


def format_ts(ts):
    try:
        dt = datetime.fromtimestamp(float(ts))
        return dt.strftime("%Y-%m-%d %H:%M")
    except (ValueError, TypeError):
        return ts


# ── Core commands ────────────────────────────────────────────────────────────

def cmd_auth_test(args):
    client = get_client()
    try:
        resp = client.auth_test()
        print(f"[OK] Connected to Slack as YOU")
        print(f"  User:      {resp['user']}")
        print(f"  User ID:   {resp['user_id']}")
        print(f"  Workspace: {resp['team']}")
        print(f"  Team ID:   {resp['team_id']}")
    except SlackApiError as e:
        print(f"[FAIL] Auth failed: {e.response['error']}")
        sys.exit(1)


def cmd_channels(args):
    client = get_client()
    try:
        # Try public + private; fall back to public only if groups:read scope missing
        try:
            result = client.conversations_list(
                types="public_channel,private_channel",
                limit=200,
                exclude_archived=True,
            )
        except SlackApiError as scope_err:
            if "missing_scope" in str(scope_err):
                result = client.conversations_list(
                    types="public_channel",
                    limit=200,
                    exclude_archived=True,
                )
            else:
                raise
        channels = sorted(result["channels"], key=lambda c: c["name"])
        print(f"{'Channel':<35} {'Members':>7}  {'ID'}")
        print("-" * 70)
        for ch in channels:
            name = f"#{ch['name']}"
            members = ch.get("num_members", "?")
            print(f"{name:<35} {members:>7}  {ch['id']}")
        print(f"\nTotal: {len(channels)} channels")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_read(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    try:
        result = client.conversations_history(channel=channel_id, limit=args.limit)
        messages = list(reversed(result["messages"]))
        for msg in messages:
            user_id = msg.get("user", "unknown")
            name = resolve_user_name(client, user_id)
            time = format_ts(msg.get("ts", ""))
            text = msg.get("text", "")
            print(f"[{time}] {name}: {text}")
        print(f"\n— {len(messages)} messages from #{args.channel}")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_send(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    try:
        client.chat_postMessage(channel=channel_id, text=args.message)
        print(f"[OK] Message sent to #{args.channel} (as you)")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_dms(args):
    client = get_client()
    try:
        result = client.conversations_list(types="im", limit=200)
        print(f"{'User':<35} {'User ID':<15} {'DM Channel ID'}")
        print("-" * 70)
        for dm in result["channels"]:
            user_id = dm.get("user", "?")
            name = resolve_user_name(client, user_id)
            print(f"{name:<35} {user_id:<15} {dm['id']}")
        print(f"\nTotal: {len(result['channels'])} DMs")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_read_dm(args):
    client = get_client()
    user_id = resolve_user_id(client, args.user)
    try:
        result = client.conversations_open(users=[user_id])
        dm_channel = result["channel"]["id"]
    except SlackApiError as e:
        print(f"Error opening DM: {e.response['error']}")
        sys.exit(1)
    try:
        result = client.conversations_history(channel=dm_channel, limit=args.limit)
        messages = list(reversed(result["messages"]))
        for msg in messages:
            uid = msg.get("user", "unknown")
            name = resolve_user_name(client, uid)
            time = format_ts(msg.get("ts", ""))
            text = msg.get("text", "")
            print(f"[{time}] {name}: {text}")
        other_name = resolve_user_name(client, user_id)
        print(f"\n— {len(messages)} messages with {other_name}")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_send_dm(args):
    client = get_client()
    user_id = resolve_user_id(client, args.user)
    try:
        result = client.conversations_open(users=[user_id])
        dm_channel = result["channel"]["id"]
    except SlackApiError as e:
        print(f"Error opening DM: {e.response['error']}")
        sys.exit(1)
    try:
        client.chat_postMessage(channel=dm_channel, text=args.message)
        other_name = resolve_user_name(client, user_id)
        print(f"[OK] DM sent to {other_name} (as you)")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_users(args):
    client = get_client()
    try:
        result = client.users_list(limit=500)
        members = [
            m for m in result["members"]
            if not m.get("is_bot") and not m.get("deleted") and m.get("id") != "USLACKBOT"
        ]
        members.sort(key=lambda m: m.get("real_name", "").lower())
        print(f"{'Name':<30} {'Display Name':<20} {'ID'}")
        print("-" * 70)
        for m in members:
            real = m.get("real_name", "?")
            display = m.get("profile", {}).get("display_name", "")
            print(f"{real:<30} {display:<20} {m['id']}")
        print(f"\nTotal: {len(members)} users")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_search(args):
    client = get_client()
    try:
        result = client.search_messages(query=args.query, count=args.limit)
        matches = result.get("messages", {}).get("matches", [])
        for msg in matches:
            ch = msg.get("channel", {}).get("name", "?")
            user = msg.get("username", "?")
            time = format_ts(msg.get("ts", ""))
            text = msg.get("text", "")
            print(f"[{time}] #{ch} — {user}: {text}")
            print()
        print(f"— {len(matches)} results for '{args.query}'")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


# ── Admin: Channel management ───────────────────────────────────────────────

def cmd_create_channel(args):
    client = get_client()
    try:
        result = client.conversations_create(
            name=args.name,
            is_private=args.private,
        )
        ch = result["channel"]
        print(f"[OK] Channel #{ch['name']} created (ID: {ch['id']})")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_archive_channel(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    try:
        client.conversations_archive(channel=channel_id)
        print(f"[OK] Channel #{args.channel} archived")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_rename_channel(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    try:
        client.conversations_rename(channel=channel_id, name=args.new_name)
        print(f"[OK] Channel renamed to #{args.new_name}")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_set_topic(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    try:
        client.conversations_setTopic(channel=channel_id, topic=args.topic)
        print(f"[OK] Topic set for #{args.channel}")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_set_purpose(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    try:
        client.conversations_setPurpose(channel=channel_id, purpose=args.purpose)
        print(f"[OK] Purpose set for #{args.channel}")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_invite(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    user_id = resolve_user_id(client, args.user)
    try:
        client.conversations_invite(channel=channel_id, users=[user_id])
        name = resolve_user_name(client, user_id)
        print(f"[OK] {name} invited to #{args.channel}")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_kick(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    user_id = resolve_user_id(client, args.user)
    try:
        client.conversations_kick(channel=channel_id, user=user_id)
        name = resolve_user_name(client, user_id)
        print(f"[OK] {name} removed from #{args.channel}")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


# ── Admin: User management ───────────────────────────────────────────────────

def cmd_user_info(args):
    client = get_client()
    user_id = resolve_user_id(client, args.user)
    try:
        result = client.users_info(user=user_id)
        u = result["user"]
        p = u.get("profile", {})
        print(f"Name:         {u.get('real_name', '?')}")
        print(f"Display:      {p.get('display_name', '?')}")
        print(f"ID:           {u['id']}")
        print(f"Email:        {p.get('email', '?')}")
        print(f"Title:        {p.get('title', '?')}")
        print(f"Status:       {p.get('status_emoji', '')} {p.get('status_text', '')}")
        print(f"Timezone:     {u.get('tz_label', '?')}")
        print(f"Is Admin:     {u.get('is_admin', False)}")
        print(f"Is Owner:     {u.get('is_owner', False)}")
        print(f"Is Restricted:{u.get('is_restricted', False)}")
        print(f"Deleted:      {u.get('deleted', False)}")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_deactivate_user(args):
    """Deactivate a user via admin API (requires admin scope + Enterprise/Business+)."""
    client = get_client()
    try:
        # Note: admin.users.remove requires Enterprise Grid or Business+
        # For standard plans, use SCIM API or do it from the Slack admin UI
        client.api_call(
            "admin.users.remove",
            json={"team_id": args.team_id, "user_id": args.user_id},
        )
        print(f"[OK] User {args.user_id} deactivated")
    except SlackApiError as e:
        if "missing_scope" in str(e.response['error']):
            print(f"Note: admin.users.remove requires Enterprise Grid or Business+ plan.")
            print(f"For standard Slack plans, deactivate users from the admin panel.")
        else:
            print(f"Error: {e.response['error']}")
        sys.exit(1)


# ── Reactions & Pins ─────────────────────────────────────────────────────────

def cmd_react(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    try:
        client.reactions_add(channel=channel_id, timestamp=args.timestamp, name=args.emoji)
        print(f"[OK] :{args.emoji}: added")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_pin(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    try:
        client.pins_add(channel=channel_id, timestamp=args.timestamp)
        print(f"[OK] Message pinned in #{args.channel}")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_unpin(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    try:
        client.pins_remove(channel=channel_id, timestamp=args.timestamp)
        print(f"[OK] Message unpinned in #{args.channel}")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


# ── Files ────────────────────────────────────────────────────────────────────

def cmd_upload(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    try:
        client.files_upload_v2(
            channel=channel_id,
            file=args.filepath,
            title=args.title or os.path.basename(args.filepath),
        )
        print(f"[OK] File uploaded to #{args.channel}")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


def cmd_files(args):
    client = get_client()
    channel_id = resolve_channel(client, args.channel)
    try:
        result = client.files_list(channel=channel_id, count=args.limit)
        files = result.get("files", [])
        print(f"{'Name':<40} {'Type':<10} {'Size':>10}  {'Date'}")
        print("-" * 80)
        for f in files:
            name = f.get("name", "?")
            ftype = f.get("filetype", "?")
            size = f.get("size", 0)
            size_str = f"{size // 1024}KB" if size > 0 else "?"
            ts = format_ts(str(f.get("timestamp", "")))
            print(f"{name:<40} {ftype:<10} {size_str:>10}  {ts}")
        print(f"\n— {len(files)} files")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


# ── Reminders ────────────────────────────────────────────────────────────────

def cmd_remind(args):
    client = get_client()
    user_id = resolve_user_id(client, args.user)
    try:
        client.reminders_add(text=args.text, user=user_id, time=args.time)
        name = resolve_user_name(client, user_id)
        print(f"[OK] Reminder set for {name}: '{args.text}' at {args.time}")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
        sys.exit(1)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Slack CLI — full admin control as your own account"
    )
    sub = parser.add_subparsers(dest="command")

    # ── Core ──
    sub.add_parser("auth-test", help="Test authentication")
    sub.add_parser("channels", help="List channels")

    p = sub.add_parser("read", help="Read channel messages")
    p.add_argument("channel", help="Channel name or ID")
    p.add_argument("--limit", type=int, default=20)

    p = sub.add_parser("send", help="Send message to channel")
    p.add_argument("channel", help="Channel name or ID")
    p.add_argument("message")

    sub.add_parser("dms", help="List DMs")

    p = sub.add_parser("read-dm", help="Read DMs with user")
    p.add_argument("user", help="User name or ID")
    p.add_argument("--limit", type=int, default=20)

    p = sub.add_parser("send-dm", help="Send DM")
    p.add_argument("user", help="User name or ID")
    p.add_argument("message")

    sub.add_parser("users", help="List users")

    p = sub.add_parser("search", help="Search messages")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=20)

    # ── Channel admin ──
    p = sub.add_parser("create-channel", help="Create a channel")
    p.add_argument("name")
    p.add_argument("--private", action="store_true")

    p = sub.add_parser("archive-channel", help="Archive a channel")
    p.add_argument("channel")

    p = sub.add_parser("rename-channel", help="Rename a channel")
    p.add_argument("channel")
    p.add_argument("new_name")

    p = sub.add_parser("set-topic", help="Set channel topic")
    p.add_argument("channel")
    p.add_argument("topic")

    p = sub.add_parser("set-purpose", help="Set channel purpose")
    p.add_argument("channel")
    p.add_argument("purpose")

    p = sub.add_parser("invite", help="Invite user to channel")
    p.add_argument("channel")
    p.add_argument("user")

    p = sub.add_parser("kick", help="Remove user from channel")
    p.add_argument("channel")
    p.add_argument("user")

    # ── User admin ──
    p = sub.add_parser("user-info", help="Detailed user info")
    p.add_argument("user")

    p = sub.add_parser("deactivate-user", help="Deactivate user (Enterprise/Business+)")
    p.add_argument("user_id")
    p.add_argument("team_id")

    # ── Reactions & pins ──
    p = sub.add_parser("react", help="Add reaction")
    p.add_argument("channel")
    p.add_argument("timestamp")
    p.add_argument("emoji")

    p = sub.add_parser("pin", help="Pin message")
    p.add_argument("channel")
    p.add_argument("timestamp")

    p = sub.add_parser("unpin", help="Unpin message")
    p.add_argument("channel")
    p.add_argument("timestamp")

    # ── Files ──
    p = sub.add_parser("upload", help="Upload file")
    p.add_argument("channel")
    p.add_argument("filepath")
    p.add_argument("--title", default=None)

    p = sub.add_parser("files", help="List files in channel")
    p.add_argument("channel")
    p.add_argument("--limit", type=int, default=20)

    # ── Reminders ──
    p = sub.add_parser("remind", help="Set a reminder")
    p.add_argument("user")
    p.add_argument("text")
    p.add_argument("time", help="Unix timestamp or natural language like 'in 5 minutes'")

    args = parser.parse_args()

    cmds = {
        "auth-test": cmd_auth_test,
        "channels": cmd_channels,
        "read": cmd_read,
        "send": cmd_send,
        "dms": cmd_dms,
        "read-dm": cmd_read_dm,
        "send-dm": cmd_send_dm,
        "users": cmd_users,
        "search": cmd_search,
        "create-channel": cmd_create_channel,
        "archive-channel": cmd_archive_channel,
        "rename-channel": cmd_rename_channel,
        "set-topic": cmd_set_topic,
        "set-purpose": cmd_set_purpose,
        "invite": cmd_invite,
        "kick": cmd_kick,
        "user-info": cmd_user_info,
        "deactivate-user": cmd_deactivate_user,
        "react": cmd_react,
        "pin": cmd_pin,
        "unpin": cmd_unpin,
        "upload": cmd_upload,
        "files": cmd_files,
        "remind": cmd_remind,
    }

    if args.command in cmds:
        cmds[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
