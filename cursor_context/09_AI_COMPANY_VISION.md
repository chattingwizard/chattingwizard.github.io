# Chatting Wizard — AI Company Vision

> Decision: Focus 100% on AI Chatbot first. Everything else comes after the chatbot works well.
> This document captures the long-term vision so it's not lost.

## The Vision

Replace all human employees (except Pau for client relations) with specialized AI agents that communicate with each other via Supabase. Target: 1 person running the entire agency.

## Current Priority: AI Chatbot (CW_AI project)

The chatbot is the hardest and most important piece. Until it sells PPV effectively and chats naturally, nothing else matters. All development resources go here first.

## Agent Architecture (FOR LATER — after chatbot is solid)

```
Cliente (Telegram bot)
    │
    ▼
AI Account Manager Bot
    │
    ├─ tone/style changes ──▶ AI Chatbot
    ├─ new content ──▶ AI Content Manager
    └─ pricing changes ──▶ AI Script Manager

AI Coach ◄──► AI Chatbot (auto-optimization loop)
    │
    └──▶ AI Script Manager (prompt updates)

All agents ◄──► Supabase (shared brain)
All agents ──▶ OpenAI API (intelligence)
```

## Agents to Build (in priority order, AFTER chatbot works)

### 1. AI Coach (Week 4-5)
- Analyzes chatbot conversation data daily
- Identifies patterns: what sells, what doesn't
- Auto-prompts the chatbot with optimized strategies
- Runs A/B tests on conversation approaches
- Measures impact of changes
- Tech: Python + Supabase + OpenAI API

### 2. AI Script Manager (Week 3-4, with CRM)
- Already 90% built
- Currently blocked by Infloww's closed API
- With own CRM: auto-imports scripts directly
- AI creates scripts, tests them, optimizes automatically
- Tech: Python + CRM API

### 3. AI Content Manager (Week 3-4, with CRM)
- Monitors model's content drive (Google Drive or similar)
- Detects new uploads
- Processes and schedules posts to OnlyFans via CRM
- Simple automation, not AI-heavy
- Tech: Python + Google Drive API + CRM API

### 4. AI Account Manager Telegram Bot (Week 5)
- Receives client instructions via Telegram
- Parses intent: tone change, pricing, content, complaints
- Routes to the appropriate agent
- Sends daily/weekly reports to clients
- Escalates to Pau for complex issues
- Tech: Python + Telethon/Telegram Bot API + Supabase

### 5. Inter-Agent OS (Week 5-6)
- Supabase table: `agent_instructions`
- Agents write instructions for other agents
- Each agent polls for new instructions
- Logging and audit trail
- Kill switch for Pau to override any agent

## Inter-Agent Communication Protocol

Simple table in Supabase:

```sql
CREATE TABLE agent_instructions (
    id UUID PRIMARY KEY,
    from_agent TEXT NOT NULL,      -- 'coach', 'account_manager', etc.
    to_agent TEXT NOT NULL,        -- 'chatbot', 'script_manager', etc.
    instruction_type TEXT NOT NULL, -- 'prompt_update', 'config_change', 'alert'
    payload JSONB NOT NULL,        -- The actual instruction
    status TEXT DEFAULT 'pending', -- 'pending', 'applied', 'rejected'
    created_at TIMESTAMPTZ DEFAULT NOW(),
    applied_at TIMESTAMPTZ
);
```

## Infrastructure

| Component | Service | Cost/month |
|-----------|---------|------------|
| LLM API | OpenAI GPT-4o | $50-200 |
| Database | Supabase | Free-$25 |
| Hosting | Railway | $5-20 |
| Total | | ~$75-245/month |

vs. current human team cost: ~$3,000-5,000+/month

## Timeline (aggressive, 12h/day)

```
Weeks 1-3:  AI Chatbot (backtesting, prompts, optimization)
Week 3:     CRM ready (Santi)
Week 3-4:   Chatbot + CRM integration. Script Manager auto. Content Manager.
Week 4-5:   AI Coach v1. Account Manager bot.
Week 5-6:   Inter-agent OS. Testing. Polish.
Week 6:     First account running 100% AI.
```

## Key Principle

The chatbot is 80% of the technical difficulty. Everything else is "plumbing."
Build the hard thing first. The rest follows.

## Decision Log

- 2026-02-17: Pau decides to focus 100% on chatbot first, shelve multi-agent until chatbot is solid
- 2026-02-17: Confirmed all development can be done in Cursor (Python + APIs, no external tools needed)
- 2026-02-17: CRM (Santi) is the main dependency for production integration (~3 weeks)
