# COACHING SYSTEM — OPERATIONAL REFERENCE

## Overview

Automated coaching system that tracks chatter performance daily, generates a COO dashboard, and sends TL briefings before each shift. Reduces Pau's micromanaging by surfacing exactly who needs attention and why.

## Data Sources (Detailed)

### Hubstaff (API v2)
- **What**: Time-tracking tool used by all chatters to log work hours
- **Authority**: THE definitive source for whether a chatter worked on a given day
- **Rule**: If Hubstaff hours < 1 for a chatter on a day, they did NOT work. Period. No need to check sales, messages, or any other metric.
- **Integration**: OAuth 2.0 with automatic token refresh. `tools/hubstaff_client.py`
- **Data pulled**: Daily hours per chatter, matched by name to Airtable

### Inflow (CSV export)
- **What**: CRM/platform used to manage OnlyFans chat operations
- **Authority**: Source of truth for all sales and chat performance metrics
- **Metrics**: Sales ($), CVR (%), Unlock Rate (%), Golden Ratio (%), Messages/hr, Reply Time, Fans Chatted
- **Export process**: Daniela manually exports daily CSV from Inflow and uploads to Slack DM with Santi
- **Column "Group"**: Contains the TL team assignment in Inflow (redundant with Airtable but useful for cross-reference)
- **Known issues**: 
  - Names in Inflow may not match Airtable (e.g. "Ajay Adedeji" vs "Adedeji Oyeniran")
  - CSV may contain inactive/old chatters (220+ vs 31 active in Airtable)
  - Daniela has been asked to standardize names and filter to active chatters only

### Airtable
- **Chatters table**: Canonical list of active chatters with name, team (TL), and metadata
- **Daily Performance table**: One record per chatter per day. Fields: Chatter, Date, Sales, CVR, Unlock, Golden, Msg/hr, Reply Time, Fans, Hours, Team
- **Performance table**: Historical weekly aggregated data (used by weekly view in dashboard)
- **Coaching Logs**: Records of TL coaching sessions
- **Reports table**: TL reports on chatter issues

## Pipeline

### Daily Ingest (`tools/ingest_daily.py`)
1. Downloads latest CSV from Daniela's Slack DM
2. Parses CSV (handles various delimiters and column name variations via COLUMN_MAP)
3. Fetches Hubstaff hours for the same date
4. Merges data: Inflow metrics + Hubstaff hours per chatter
5. Stores in Airtable Daily Performance table
6. Skips records that already exist (dedup by chatter + date)

### Dashboard Generation (`tools/generate_dashboard.py`)
1. Loads all data from Airtable (chatters, daily perf, weekly perf, coaching logs, reports)
2. Normalizes names and builds fuzzy alias map (Inflow names → Airtable canonical names)
3. Generates single-file HTML dashboard with embedded JSON data
4. Deploys to GitHub Pages repo (`C:\Users\34683\cw-coaching\`)

### TL Briefings (`tools/send_briefings.py`)
1. Loads same data as dashboard
2. For each TL: identifies chatters needing coaching (worst performers, most days since coaching, red flags)
3. Sends Slack DM to TL 30 minutes before their shift starts
4. Includes: top 3 chatters to coach today, why, and suggested talking points

## Scheduling (GitHub Actions)

Cron jobs in `.github/workflows/coaching-daily.yml`:
- Uses `github.event.schedule` (not `date -u +%H`) for robust cron detection
- Monday special case: data ingest deferred from 07:30 to 15:30 UTC because Daniela can't export before ~2pm UTC on Mondays

| Cron (UTC) | What runs |
|---|---|
| `30 7 * * *` | Ingest + Dashboard + Briefings (except Monday: only Danilyn briefing with old data) |
| `30 15 * * *` | Ezekiel briefing. On Mondays: also runs deferred ingest + dashboard + management report |
| `30 23 * * *` | Huckle + Danilyn briefings |

## KPIs and Thresholds

Performance score is weighted average (0-100) of these KPIs:
- **Sales/hr** (35% weight) — primary signal
- **CVR** — conversion rate
- **Unlock Rate** — % of fans who unlock paid content
- **Golden Ratio** — proprietary metric
- **Msg/hr** — messages sent per hour
- **Reply Time** — average response time (lower = better, inverted scoring)

Score interpretation:
- 80+ = Top performer
- 60-79 = Good
- 40-59 = Fair
- 20-39 = Low
- 0-19 = Critical
- No hours (< 1h Hubstaff) = Day off (not scored, not flagged)

## Name Matching

Airtable "Chatters" table has canonical names. Inflow CSV has operational names that may differ.

Matching strategy:
1. Normalize: lowercase, collapse multiple spaces, strip whitespace
2. Exact match on normalized names
3. Fuzzy: try last-name + first-name match
4. Fuzzy: try partial name containment
5. If no match: show "No data available" in dashboard, flag for manual resolution

When names can't be matched, ask Daniela to update Inflow names to match Airtable.

## Traffic / Workload Management

Traffic (number of fans a chatter handles) depends on which models/accounts they're assigned to.

**Metric**: Fans/hr (fans_chatted / hours_worked) — normalizes for shift length differences.

**Dashboard visualization**: Horizontal bars per TL team, ranking chatters by Fans/hr with color coding:
- GREEN (HIGH): > 25% above team average
- BLUE (NORMAL): within +/- 25% of team average
- YELLOW (LOW): > 25% below team average

**Imbalance detection**: If max Fans/hr / min Fans/hr >= 2x, show warning badge.

**TL actions on imbalance**:
- Move chatters between models/accounts to balance load
- Adjust shifts/schedules if imbalance is persistent

**Team daily summary**: Each TL tab shows aggregated metrics:
- Total Sales, Avg $/hr, Avg CVR, Total Fans, Active chatters vs total (day-offs excluded)

## Dashboard Enhancements

Features added to chatter cards:
- **Trend arrows**: Green up / red down arrows on each KPI, comparing today vs 7-day average (>10% deviation triggers arrow)
- **Sparklines**: 7-day mini line chart of Sales/hr in each card header
- **Streak badges**: "Xd declining" (red) or "Xd improving" (green) when 3+ consecutive days of change
- **Sales Funnel**: In expanded card detail, shows Fans → PPVs Sent → Unlocked → Sales with conversion rates and bottleneck identification

## Lessons Learned

- **Always use the authoritative source.** Don't invent composite heuristics when a single signal (like Hubstaff hours) is definitive. Ask "what is the source of truth?" before building logic.
- **Name mismatches are the #1 data quality issue.** Always normalize before comparing, and push for source-side fixes (Daniela updating Inflow) rather than building ever-more-complex matching.
- **GitHub Actions cron times can drift.** Use `github.event.schedule` to detect which cron fired, not the current time.
- **Dashboard messages must be user-friendly.** The COO (Pau) is non-technical. No "name mismatch?" messages — use simple language like "Day off" or "No data available".
