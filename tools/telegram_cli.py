"""
Telegram CLI — Read and send messages as your own account.

Usage:
    python tools/telegram_cli.py chats                          # List recent chats
    python tools/telegram_cli.py read <chat> [--limit N]        # Read messages from chat
    python tools/telegram_cli.py send <chat> <message>          # Send message to chat
    python tools/telegram_cli.py search <query> [--limit N]     # Search messages globally
    python tools/telegram_cli.py contacts                       # List contacts

Session file: ~/.cw_telegram_session (already authenticated)
"""

import argparse
import os
import sys
import asyncio
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from telethon import TelegramClient
from telethon.tl.types import User, Chat, Channel

API_ID = 33342672
API_HASH = "8c349eb99d3f22ddc16def2f7181661f"
SESSION_PATH = os.path.join(os.path.expanduser("~"), ".cw_telegram_session")


def get_client():
    return TelegramClient(SESSION_PATH, API_ID, API_HASH)


def chat_name(entity):
    if isinstance(entity, User):
        name = entity.first_name or ""
        if entity.last_name:
            name += f" {entity.last_name}"
        return name.strip() or str(entity.id)
    elif hasattr(entity, 'title'):
        return entity.title
    return str(entity.id)


async def cmd_chats(args):
    async with get_client() as client:
        dialogs = await client.get_dialogs(limit=args.limit if hasattr(args, 'limit') else 30)
        print(f"{'Chat':<40} {'Type':<10} {'Unread':>6}  {'Last Message'}")
        print("-" * 90)
        for d in dialogs:
            name = d.name or "?"
            if isinstance(d.entity, User):
                ctype = "DM"
            elif isinstance(d.entity, Channel):
                ctype = "Channel"
            else:
                ctype = "Group"
            unread = d.unread_count
            last = ""
            if d.message:
                last = (d.message.text or "")[:50]
            print(f"{name:<40} {ctype:<10} {unread:>6}  {last}")
        print(f"\n-- {len(dialogs)} chats")


async def cmd_read(args):
    async with get_client() as client:
        entity = await resolve_chat(client, args.chat)
        messages = await client.get_messages(entity, limit=args.limit)
        messages = list(reversed(messages))
        for msg in messages:
            sender = ""
            if msg.sender:
                sender = chat_name(msg.sender)
            time = msg.date.strftime("%Y-%m-%d %H:%M") if msg.date else ""
            text = msg.text or "[media]"
            print(f"[{time}] {sender}: {text}")
        print(f"\n-- {len(messages)} messages")


async def resolve_chat(client, chat_ref):
    """Resolve a chat by ID, username, or partial name match."""
    if chat_ref.lstrip('-').isdigit():
        return await client.get_entity(int(chat_ref))
    try:
        return await client.get_entity(chat_ref)
    except (ValueError, Exception):
        pass
    # Fallback: search dialogs by partial name
    dialogs = await client.get_dialogs(limit=100)
    search = chat_ref.lower()
    for d in dialogs:
        if search in (d.name or "").lower():
            return d.entity
    raise ValueError(f"Chat not found: {chat_ref}")


async def cmd_send(args):
    async with get_client() as client:
        entity = await resolve_chat(client, args.chat)
        await client.send_message(entity, args.message)
        name = chat_name(entity)
        print(f"[OK] Message sent to {name}")


async def cmd_search(args):
    async with get_client() as client:
        messages = await client.get_messages(None, search=args.query, limit=args.limit)
        for msg in messages:
            sender = ""
            if msg.sender:
                sender = chat_name(msg.sender)
            chat = ""
            if msg.chat:
                chat = chat_name(msg.chat)
            time = msg.date.strftime("%Y-%m-%d %H:%M") if msg.date else ""
            text = msg.text or "[media]"
            print(f"[{time}] {chat} -- {sender}: {text}")
            print()
        print(f"-- {len(messages)} results for '{args.query}'")


async def cmd_contacts(args):
    async with get_client() as client:
        result = await client.get_contacts()
        print(f"{'Name':<35} {'Username':<20} {'Phone':<15} {'ID'}")
        print("-" * 80)
        for u in result:
            name = f"{u.first_name or ''} {u.last_name or ''}".strip()
            username = f"@{u.username}" if u.username else ""
            phone = u.phone or ""
            print(f"{name:<35} {username:<20} {phone:<15} {u.id}")
        print(f"\n-- {len(result)} contacts")


def main():
    parser = argparse.ArgumentParser(description="Telegram CLI")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("chats", help="List recent chats")
    p.add_argument("--limit", type=int, default=30)

    p = sub.add_parser("read", help="Read messages from a chat")
    p.add_argument("chat", help="Username, phone, or chat ID")
    p.add_argument("--limit", type=int, default=20)

    p = sub.add_parser("send", help="Send a message")
    p.add_argument("chat", help="Username, phone, or chat ID")
    p.add_argument("message")

    p = sub.add_parser("search", help="Search messages")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=20)

    sub.add_parser("contacts", help="List contacts")

    args = parser.parse_args()

    commands = {
        "chats": cmd_chats,
        "read": cmd_read,
        "send": cmd_send,
        "search": cmd_search,
        "contacts": cmd_contacts,
    }

    if args.command in commands:
        asyncio.run(commands[args.command](args))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
