# OPERATIONAL WORKFLOWS — Chatting Wizard

> Source of truth for every process in the company.
> Maps WHO does WHAT (Human vs AI/Automation) for each step.
> All Monday task templates and automations MUST reference this document.

---

## 1. NEW MODEL ONBOARDING (Scripts)

**Trigger:** Angeles creates item in Monday.com (Client OnOffboarding CWENG)

| Step | Who | Action |
|---|---|---|
| 1. Detection | **AI** (onboard_model.py) | Scans Monday + Slack for new models |
| 2. Data fetch | **AI** (onboard_model.py) | Reads model info from Airtable Models table |
| 3. Config creation | **AI** (onboard_model.py) | Generates model config file (tools/models/*.py) |
| 4. Script generation | **AI** (model_factory.py) | Generates XLSX (Infloww-ready) + HTML guides + objections + sexting sequences |
| 5. Smart Messages generation | **AI** (generate_nudge_pages.py) | Generates smart-messages.html guide |
| 6. QA check | **AI** (qa_sexting.py) | Validates scripts automatically |
| 7. Dashboard update | **AI** (generate_dashboard.py) | Adds model to script dashboard |
| 8. Notification | **AI** (Slack) | Notifies Rei via Slack DM that scripts are ready |
| 9. Content preparation | **Angeles** (manual) | Prepares content: photos, videos for PPVs, teaser content for Smart Messages ZERO tier |
| 10. Import to Infloww | **Rei** (manual) | Uploads XLSX to Infloww, creates script commands |
| 11. Assign content to PPVs | **Rei** (manual) | Maps real content files to each PPV slot in Infloww |
| 12. Smart Messages setup | **Rei/Cath** (manual) | Creates Smart Messages in Infloww using HTML guide (~30-45 min per model) |
| 13. Verification | **Rei** (manual) | Tests commands in Infloww, confirms scripts are live |
| 14. Brief TLs | **Rycel** (manual) | Informs TLs about new model availability |

**Manual tasks for Monday:**
- Angeles: Content preparation (photos, videos)
- Rei: Import XLSX to Infloww + assign content + verify
- Rei/Cath: Set up Smart Messages in Infloww manually
- Rycel: Brief TLs on new model

---

## 2. SCRIPT UPDATE / OPTIMIZATION

**Trigger:** Manual request (Pau, Rei, or performance data suggests changes needed)

| Step | Who | Action |
|---|---|---|
| 1. Identify need | **Pau/Rei** (manual) | Decide what model/script needs updating |
| 2. Edit config | **AI** (via Cursor agent) | Edits tools/models/{model}.py per instructions |
| 3. Regenerate | **AI** (model_factory.py) | Regenerates XLSX + HTML for that model |
| 4. QA check | **AI** (qa_sexting.py) | Validates updated scripts |
| 5. Re-import | **Rei** (manual) | Re-imports updated XLSX to Infloww |
| 6. Re-assign content | **Rei** (manual) | Updates content assignments if PPV structure changed |

**Manual tasks for Monday:**
- Rei: Re-import XLSX to Infloww

---

## 3. DAILY DATA PIPELINE

**Trigger:** GitHub Actions cron (07:30 UTC Tue–Sun, 15:30 UTC Mon)

| Step | Who | Action |
|---|---|---|
| 1. Export CSV | **Daniela** (manual) | Exports Inflow CSV daily, uploads to Slack DM with Santi |
| 2. Download CSV | **AI** (ingest_daily.py) | Downloads from Slack DM automatically |
| 3. Fetch hours | **AI** (hubstaff_client.py) | Gets Hubstaff hours per chatter |
| 4. Merge & store | **AI** (ingest_daily.py) | Merges metrics + hours → Airtable Daily Performance |
| 5. Generate dashboard | **AI** (generate_dashboard.py) | Creates HTML dashboard → GitHub Pages |
| 6. Send briefings | **AI** (send_briefings.py) | Sends Slack DMs to TLs 30min before shift |

**Manual tasks for Monday:**
- Daniela: Export and upload Inflow CSV (daily, ~2pm UTC on Mondays)

**Monday special:** Daniela can't export before ~2pm UTC on Mondays → ingest deferred to 15:30 UTC.

---

## 4. TL COACHING SESSIONS

**Trigger:** TL receives automated briefing via Slack (30 min before shift)

| Step | Who | Action |
|---|---|---|
| 1. Briefing sent | **AI** (send_briefings.py) | Identifies top chatters needing coaching, generates talking points |
| 2. Review briefing | **TL** (manual) | Reads Slack briefing in #0-team-leaders |
| 3. Conduct coaching | **TL** (manual) | Calls/messages chatter, discusses KPIs and talking points |
| 4. Log session | **TL** (manual) | Fills Airtable Coaching Log form (date, chatter, notes, action items, optional: Focus KPI + target) |
| 5. Track goals | **AI** (dashboard) | Shows goal progress in next briefing |

**Manual tasks for Monday:**
- TLs: Conduct coaching sessions and log them (frequency: every 2 working days per chatter)

---

## 5. TL LIVE ASSISTANCE

**Trigger:** Chatter requests help during shift

| Step | Who | Action |
|---|---|---|
| 1. Chatter asks for help | **Chatter** | Messages TL in Slack/Discord |
| 2. TL assists | **TL** (manual) | Provides guidance on current chat situation |
| 3. Log assistance | **TL** (manual) | Fills TL Live Assistance Report in Airtable (evidence, method, resolution) |

**Manual tasks for Monday:**
- TLs: Log assistance reports

---

## 6. PERFORMANCE MONITORING

**Trigger:** Continuous (dashboard updates daily)

| Step | Who | Action |
|---|---|---|
| 1. Calculate scores | **AI** (dashboard) | Weighted average: Sales/hr 35%, Msg/hr 15%, CVR 15%, Reply Time 15%, Unlock 10%, Golden 10% |
| 2. Flag red flags | **AI** (dashboard) | Sales/hr <$20, CVR <7%, Unlock <30%, Golden <1.5%, Msg/hr <70, Reply >2.5min |
| 3. Review dashboard | **Pau/Rycel** (manual) | Check dashboard at chattingwizard.github.io/cw-coaching/ |
| 4. Escalate issues | **Pau/Rycel** (manual) | Create tasks for TLs if intervention needed |

**Manual tasks for Monday:**
- Pau/Rycel: Review dashboard, escalate to TLs when needed

---

## 7. TRAFFIC / WORKLOAD BALANCING

**Trigger:** Dashboard shows imbalance (max/min Fans/hr ≥ 2x)

| Step | Who | Action |
|---|---|---|
| 1. Calculate Fans/hr | **AI** (dashboard) | fans_chatted / hours_worked per chatter |
| 2. Flag imbalance | **AI** (dashboard) | ≥2x = warning (yellow), ≥3x = critical (red) |
| 3. Review distribution | **TL** (manual) | Checks traffic chart in dashboard |
| 4. Rebalance | **TL** (manual) | Moves chatters between models/accounts |

**Manual tasks for Monday:**
- TLs: Rebalance chatter assignments when traffic imbalance detected

---

## 8. WEEKLY OPERATIONS

**Trigger:** Weekly cycle

| Task | Who | When |
|---|---|---|
| Create next week's schedule | **Rycel** (manual) | Friday |
| Review weekly KPIs | **Rycel** (manual) | Friday |
| Coaching log completeness check | **Rycel** (manual) | Friday |
| Weekly management review | **Pau** (manual) | Friday |
| Verify Inflow data exported | **Daniela** (manual) | Monday |
| Calculate bonuses (if applicable) | **Rycel** (manual) | End of month |

---

## 9. RECRUITMENT PIPELINE

**Trigger:** Application received

| Step | Who | Action |
|---|---|---|
| 1. Screen applications | **Mileh** (manual) | Filters in Airtable, marks qualified as "Interview" |
| 2. Send Discord invite | **Mileh** (manual) | Assigns "Applicant" role, creates thread in #recruits |
| 3. Post welcome + test link | **Mileh** (manual) | 24-48h deadline for screening test |
| 4. Grade test | **Mileh** (manual) | Pass → send interview link / Fail → remove |
| 5. Conduct interview | **Mileh** (manual) | 15-min interview (knowledge + writing test) |
| 6. Pass/Fail decision | **Mileh** (manual) | Update Airtable → "Training", assign Discord "Day 1" |

---

## 10. TRAINING PROGRAM (5 Days)

**Trigger:** Recruit passes interview

| Day | Who | Content | Duration |
|---|---|---|---|
| Day 0 | **Mileh** (manual) | Interview | 15 min |
| Day 1 | **Mileh** (manual) | Foundations + Infloww walkthrough + practice | 2-3 hrs |
| Day 2 | **Mileh** (manual) | Journey step-by-step + annotated chats + practice | 2-3 hrs |
| Day 3 | **Mileh** (manual) | Advanced skills + objections drill + full simulation | 3 hrs |
| Day 4 | **Mileh** (manual) | Written quiz (80% pass) + live chatting exam (3.5/5 avg) | 1-2 hrs |

**Between days:** Recruits self-study using Chatting School website (GitHub Pages).

**Pass:** Update Airtable → "Probation", coordinate handover with Rycel.
**Fail:** Can retake exam once; second fail = removed.

---

## 11. PROBATION (14 Days)

**Trigger:** Recruit passes final exam → Mileh hands over to Rycel/TL

| Step | Who | When | Action |
|---|---|---|---|
| 1. Handover message | **Mileh** (manual) | Day 0 | Telegram to Rycel: name, scores, strengths, areas to watch |
| 2. Assign to TL + models | **Rycel** (manual) | Day 1 | Assigns TL, gives 1-2 models (reduced load) |
| 3. Add to Airtable | **Rycel** (manual) | Day 1 | Adds to Chatters table, ensures Inflow name matches |
| 4. Daily chat review | **TL** (manual) | Days 1-3 | Reviews chats daily |
| 5. Coaching session | **TL** (manual) | Days 2, 4, 6 | Focus: script adherence, character, speed |
| 6. Increase workload | **TL** (manual) | Week 2 | Full model assignments |
| 7. Coaching session | **TL** (manual) | Days 8, 10, 12 | Focus: consistency, sales, difficult situations |
| 8. KPI tracking | **AI** (automatic) | Week 2 | System tracks via daily pipeline |
| 9. Probation report | **TL** (manual) | Day 14 | Submits report to Rycel: KPIs, quality, trajectory, recommendation |
| 10. Pass/Fail decision | **Rycel** (manual) | Day 14 | Pass: Sales/hr ≥$20, Reply <2min, no violations. Edge case: extend 7 days |

---

## 12. CONTENT MANAGEMENT

**Trigger:** Various (client request, chatter need, custom order)

### Content Request
| Step | Who | Action |
|---|---|---|
| 1. Identify need | **Chatter/TL** | Identifies missing content for a model |
| 2. Create request | **Angeles** (manual) | Logs in Content Request board |
| 3. Coordinate with model/agency | **Angeles** (manual) | Requests content from model or agency |
| 4. Receive & upload | **Angeles** (manual) | Uploads content to model's account |

### Custom Order
| Step | Who | Action |
|---|---|---|
| 1. Fan requests custom | **Chatter** | Negotiates price and details with fan |
| 2. Log in Airtable | **Chatter** | Creates Custom record (model, type, price, description) |
| 3. Coordinate delivery | **Angeles/TL** (manual) | Ensures model creates content, chatter delivers to fan |

### Deep Dive (Revenue Analysis)
| Step | Who | Action |
|---|---|---|
| 1. Identify model for review | **Pau/Rycel** (manual) | Selects model for revenue deep dive |
| 2. Analyze data | **Pau/Rycel** (manual) | Reviews metrics in Deep Dive board |
| 3. Create action plan | **Pau/Rycel** (manual) | Decides changes to model strategy |

---

## 13. CLIENT MANAGEMENT

**Trigger:** Recurring or client-initiated

| Task | Who | Frequency |
|---|---|---|
| Client reports & follow-ups | **Angeles** (manual) | As needed |
| Weekly checklist per model | **Angeles** (manual) | Weekly |
| Client calls | **Angeles** (manual) | As scheduled |
| Model onboarding communication | **Angeles** (manual) | Per new model |
| Model offboarding | **Angeles** (manual) | Per departure |

---

## AUTOMATION COVERAGE SUMMARY

| Area | Automated | Manual |
|---|---|---|
| **Script Generation** | Detection, data fetch, config, generation, QA, dashboard, notification | Infloww import, content assignment, Smart Messages setup |
| **Data Pipeline** | CSV download, Hubstaff fetch, merge, store, dashboard, briefings | Daniela: daily CSV export/upload |
| **Coaching** | Briefings, urgency scoring, goal tracking, performance scores | TLs: conduct sessions, log in Airtable |
| **Dashboard** | Fully automated | — |
| **Hiring** | — | Mileh: all steps manual |
| **Training** | Video generation, website hosting | Mileh: all live sessions manual |
| **Probation** | KPI tracking (via daily pipeline) | TL: daily review, coaching, report. Rycel: decision |
| **Content** | — | Angeles: all steps manual |
| **Client Management** | — | Angeles: all steps manual |
