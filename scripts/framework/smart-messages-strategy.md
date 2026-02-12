# Smart Messages Strategy — Chatting Wizard

## 1. Overview

Smart Messages are Infloww's automated messaging system. They fire based on triggers (fan comes online, subscribes, buys PPV, etc.) and deliver pre-written messages without chatter intervention.

**Purpose:** Generate interactions that chatters can convert into sessions and sales. Smart Messages are the HOOK. The chatter is the CLOSER.

**Key principle:** Every Smart Message must feel like the model spontaneously decided to write. The moment it feels automated, it loses all power.

**This document covers:**
- Nudge strategy (fan comes online) — the primary use case
- All other triggers — welcome, post-purchase, retention, win-back, resub, birthday
- Generic templates adaptable per model

**What this does NOT cover:**
- Model-specific message content (created separately per model)
- Script sequences (covered in `script-framework-v1.md`)

---

## 2. Nudge: Fan Comes Online

### 2.1 Purpose

When a fan connects, the system detects it and sends a message that looks like the model noticed and reached out. Goal: fan responds → chatter takes over → session → sale.

### 2.2 Fan Psychology by Segment

Understanding WHY each fan is in their tier determines what nudge will work.

| Segment | Who they are | What drives them | What activates them | What kills it |
|---------|-------------|-----------------|--------------------|----|
| **Whale** ($1000+) | Has money. Probably lonely, divorced, or emotionally unfulfilled. NOT paying for porn — paying to feel SPECIAL. | Emotional connection. "She thinks about ME." | GFE warmth. Feeling she genuinely missed him. | Generic messages. Feeling like one of many. |
| **Shark** ($400-1000) | Spends well but is selective. Likes the mix of connection + sexual content. | Balance of emotion + excitement. Buys when aroused AND feels value. | Flirty tease. "Something could happen right now." | Feeling sold to. Overt transactional messages. |
| **Shrimp** ($100-400) | Done 1-3 sessions. Still "testing". May be on multiple accounts. | Curiosity. "What does she have that I haven't seen?" | FOMO + tease. Feeling he's missing something good. | Not sure if this model is worth more vs others. |
| **Low Spender** ($30-100) | Bought 1-2 cheap PPVs. Price-sensitive. | Value for money. Will buy if cheap and good. | Sense of a deal. Curiosity + accessible price signal. | High prices. Feeling pressured. |
| **Rat** ($1-30) | Barely spent. Probably on many accounts. No emotional connection. | Something flashy, provocative, easy to grab. | Direct hooks. Strong tease. No GFE fluff. | Fake relationship building. Feels hollow. |
| **$0 Fan** | Never spent a cent. Either curious, a freeloader, shy, or new. NO emotional investment exists. | Promos, offers, low-barrier deals, sexual provocation. | Direct sale approach: low-price PPV, special offer, provocative tease with content attached. | GFE without any prior investment — feels unearned and fake. |

### 2.3 Segmentation

We create **4 separate Smart Messages**, each targeting a different spending tier.

| Smart Message | Include Lists | Psychology-driven Tone | Objective |
|--------------|---------------|------|-----------|
| **SM-NUDGE-VIP** | Whale + Shark | GFE warm, "I missed you", she thinks about him | Maintain emotional bond → chatter takes over → session |
| **SM-NUDGE-MID** | Shrimp + Low Spenders | Flirty tease, curiosity, "something could happen" | Spark interest → chatter pushes to session |
| **SM-NUDGE-LOW** | Rats | Direct hooks, provocative, no fluff | Activate into conversation → quick qualification |
| **SM-NUDGE-ZERO** | Fans (exclude ALL spending lists) | Provocative + direct sale. Promos, offers, low-price PPV attached. | Convert $0 into FIRST purchase. Less focus on conversation, more on transaction. |

**Why separate:** A Whale who spent $3,000 needs to feel like a VIP — he's paying for the illusion that she cares. A $0 fan has zero emotional investment — GFE is wasted on him. He needs a deal good enough to break the $0 barrier.

**SM-NUDGE-ZERO approach:** Unlike the other nudges which aim to generate conversation, ZERO nudges can go direct to sale. Attach a low-price PPV ($3-5) or free teaser content directly in the message. The goal is not to start a relationship — it's to break the spending barrier. If they buy, they move to a spending list and start getting better nudges. If they don't, minimal chatter time wasted.

### 2.3 Configuration (All 4 Nudges)

| Setting | Value | Why |
|---------|-------|-----|
| **Trigger** | Fan comes online | — |
| **Action** | After delay, 2-5 minutes random | Immediate = feels like a bot. 2-5 min = she "saw the notification and decided to write" |
| **Frequency** | Send every time fan matches trigger | Enables collection rotation |
| **Effective** | Immediately | — |
| **Expiry** | Never | — |
| **Stop message sequence** | ON | When fan replies, stop the chain so the chatter takes over |
| **Unsend messages** | OFF | If fan sees it later, it's still a valid touchpoint |

**Exclude filters (apply to all 4):**

| Filter | Value | Why |
|--------|-------|-----|
| Fans who were sent messages recently | 0 days, 6 hours | Prevents spamming fans already in conversation. Counts ALL messages (manual + auto). |
| Fans with unread messages | ON (exclude) | If the fan already wrote to us and we haven't read it, don't pile on — respond first |
| Creators | ON (exclude) | Don't nudge other creators |

**SM-NUDGE-ZERO additional excludes:**
- Whale list
- Shark list
- Shrimp list
- Low Spenders list
- Rats list

This leaves ONLY fans with $0 total spend.

### 2.4 Collection Structure

Each Smart Message has **10 collections**. The system picks one randomly each time the trigger fires, and doesn't repeat until all 10 have been used.

**Message chain per collection:**
- **6 collections**: 2 messages (double-text pattern — feels like she had another thought)
- **4 collections**: 1 message only (single text — she said what she wanted to say)

This mix prevents the pattern of always getting two messages, which would feel robotic.

**Wait time between M1 and M2:** 10-20 seconds. Simulates natural "oh and one more thing" double-text.

**{name} tag usage:** Used in ~30% of collections (3 out of 10). Too much = pattern detected. Too little = impersonal. Rotate which collections use it.

---

### 2.5 Message Templates

These are GENERIC templates. When adapting per model, adjust: vocabulary, emoji style, slang, personality quirks, and references to model-specific traits.

---

#### SM-NUDGE-VIP — Whale + Shark ($400+)

Psychology: These fans are emotionally invested. They've spent serious money. Nudge must reinforce the GFE bond — she misses him, she thinks about him, he's special.

**Collection 1** (2 msgs, GFE warm)
- M1: `hey you 💕`
- M2 (15s): `I was literally just thinking about you`

**Collection 2** (2 msgs, Flirty)
- M1: `mmm look who's here 😏`
- M2 (15s): `perfect timing... I just got comfortable in bed`

**Collection 3** (1 msg, GFE)
- M1: `finally you're on 😩 I missed you`

**Collection 4** (2 msgs, Situational)
- M1: `hiii 🥰`
- M2 (20s): `I'm so bored rn... save me?`

**Collection 5** (1 msg, Flirty)
- M1: `there you are 😏 been waiting for you`

**Collection 6** (2 msgs, Personal — uses {name})
- M1: `{name} 💕`
- M2 (15s): `I was hoping you'd come on today`

**Collection 7** (1 msg, Curiosity)
- M1: `omg perfect timing... I need to tell you something 😊`

**Collection 8** (2 msgs, Tease)
- M1: `guess what I'm doing rn 😏`
- M2 (20s): `actually... maybe I shouldn't say`

**Collection 9** (1 msg, Warm)
- M1: `hey babe 💗 you always show up at the right time`

**Collection 10** (2 msgs, Playful — uses {name})
- M1: `you 🫣`
- M2 (15s): `I literally just said out loud "I wish {name} was on" and here you are`

---

#### SM-NUDGE-MID — Shrimp + Low Spenders ($30-400)

Psychology: Proven buyers but not deep spenders. Mix of GFE warmth and flirty curiosity. Push them toward a session without being too intense.

**Collection 1** (2 msgs, Flirty)
- M1: `hey 😏`
- M2 (15s): `I'm in a mood rn and you popped up at the worst time`

**Collection 2** (1 msg, Curiosity)
- M1: `omg I have something to show you 🫣`

**Collection 3** (2 msgs, Warm + Tease — uses {name})
- M1: `hiii {name} 💕`
- M2 (15s): `I was just thinking about last time we talked...`

**Collection 4** (1 msg, Playful)
- M1: `well well well... look who's here 😏`

**Collection 5** (2 msgs, Situational)
- M1: `ugh I'm so bored 😩`
- M2 (20s): `talk to me? I need a distraction`

**Collection 6** (2 msgs, Flirty + Curiosity)
- M1: `hey you 🔥`
- M2 (15s): `I just did something kinda crazy... wanna see?`

**Collection 7** (1 msg, Direct)
- M1: `I was literally about to text you 😅`

**Collection 8** (2 msgs, Tease)
- M1: `mmm hi 😏`
- M2 (15s): `I'm lying in bed and I can't stop thinking about something`

**Collection 9** (1 msg, Warm)
- M1: `hey babe, you caught me at a fun time 😊`

**Collection 10** (2 msgs, Curiosity — uses {name})
- M1: `ok wait {name}`
- M2 (10s): `I've been saving something for you and I literally can't wait anymore`

---

#### SM-NUDGE-LOW — Rats ($1-30)

Psychology: Barely spent anything. They need a HOOK strong enough to pull them into conversation. More direct, more curiosity, more urgency. Don't over-invest in GFE — they haven't earned it yet.

**Collection 1** (2 msgs, Curiosity)
- M1: `hey 😏`
- M2 (15s): `I have something I think you'll like`

**Collection 2** (1 msg, Direct)
- M1: `omg you're on! I need to show you this 🫣`

**Collection 3** (2 msgs, Playful — uses {name})
- M1: `hi {name} 🔥`
- M2 (15s): `you came at the right time... I'm feeling generous today`

**Collection 4** (1 msg, Curiosity)
- M1: `ok I can't keep this to myself anymore 😩`

**Collection 5** (2 msgs, Playful)
- M1: `pssst`
- M2 (10s): `I have a surprise for you 😏`

**Collection 6** (2 msgs, Direct + Hook)
- M1: `hey babe 💕`
- M2 (15s): `I just made something that I think only you would appreciate`

**Collection 7** (1 msg, FOMO)
- M1: `I'm only going to be in this mood for a little bit... come talk to me 😏`

**Collection 8** (2 msgs, Tease)
- M1: `you 😏`
- M2 (15s): `I was thinking about you earlier and got a little carried away...`

**Collection 9** (1 msg, Playful)
- M1: `finally!! I've been waiting for someone fun to come on 😊`

**Collection 10** (2 msgs, Curiosity — uses {name})
- M1: `ok {name}`
- M2 (10s): `there's something I've been wanting to ask you 🫣`

---

#### SM-NUDGE-ZERO — $0 Fans — DIRECT SALE APPROACH

**Strategy shift:** Unlike VIP/MID/LOW nudges which generate conversation, ZERO nudges go direct to sale. These fans have no emotional investment. GFE is wasted on them. Instead: provocative tease + low-barrier offer.

**Configuration differences:**
- "Fans who were sent messages recently": 0 days, 12 hours (less frequent — don't waste effort)
- **Attach content:** 5-6 collections include a free teaser photo. 2-3 collections include a low-price PPV ($3-5). This breaks the $0 barrier without chatter involvement.
- If fan buys → they move to a spending list → start getting better nudges next time
- If fan responds but doesn't buy → chatter qualifies quickly, doesn't invest heavy time

**Collection 1** (2 msgs, Provocative + free teaser attached)
- M1: `I'm feeling generous today 😏` [ATTACH: free teaser photo]
- M2 (15s): `there's more where that came from...`

**Collection 2** (1 msg, Direct offer)
- M1: `I just made something really hot and I'm sending it to a few people at a special price 🔥 you in?` [ATTACH: PPV $3-5]

**Collection 3** (2 msgs, Tease + hook)
- M1: `I'm bored and I just did something naughty 🫣`
- M2 (15s): `wanna see? I'll give you a special deal 😏`

**Collection 4** (1 msg, Free teaser — uses {name})
- M1: `{name}... I think you need to see this 😏` [ATTACH: free teaser photo]

**Collection 5** (2 msgs, FOMO + offer)
- M1: `ok I never do this but...`
- M2 (10s): `I'm giving away my hottest stuff at a crazy price rn. you're lucky you're on 🔥` [ATTACH: PPV $3-5]

**Collection 6** (1 msg, Provocative free)
- M1: `this is what I'm wearing rn... or not wearing 😏` [ATTACH: free teaser photo]

**Collection 7** (2 msgs, Challenge + offer)
- M1: `I bet you can't handle what I just recorded 😈`
- M2 (15s): `prove me wrong... it's basically nothing 💕` [ATTACH: PPV $3-5]

**Collection 8** (1 msg, Free teaser + hook — uses {name})
- M1: `hey {name}, a little preview just for you 🔥 if you want the full thing, just say the word` [ATTACH: free teaser photo]

**Collection 9** (2 msgs, Curiosity + free)
- M1: `I just took this and idk if I should share it 🫣`
- M2 (15s): `you know what... here, you can have it 😏` [ATTACH: free teaser photo]

**Collection 10** (1 msg, Direct offer — uses {name})
- M1: `{name} I'm doing something special today... my best content at the lowest price ever. don't miss it 🔥` [ATTACH: PPV $3-5]

**Content split:** 5 collections with free teaser (hook to respond) + 5 collections with low-price PPV ($3-5, direct conversion attempt). Free teasers generate more responses. PPVs generate direct revenue. Mix of both covers both objectives.

---

### 2.6 Chatter Handoff

The nudge is the HOOK. When the fan responds, the chatter takes over. But the chatter needs to know WHAT to do based on who responded.

**Chatter decision tree after nudge response:**

| Fan Segment | Chatter Action |
|-------------|----------------|
| **VIP (Whale/Shark)** | Short rapport (3-5 msgs) → Teasing → Sexting. These fans are proven. Move fast but keep the GFE warm. Use RE- (re-engagement) scripts. |
| **MID (Shrimp/Low)** | Standard rapport (5-7 msgs) → Teasing → Sexting. Build the connection to push them up the spending ladder. |
| **LOW (Rats)** | Qualify quickly (2-3 msgs). If responsive → push to sexting. If monosyllabic → deprioritize. Don't invest heavy time. |
| **ZERO ($0)** | Qualify immediately. If they're new subs (<48h) → Welcome Journey flow. If old subs → quick qualification → push to sexting or deprioritize. Lowest priority in inbox. |

**Critical rule:** The chatter should NEVER reference the nudge message explicitly. If the nudge was "hey I was thinking about you 💕" and the fan says "hey! what were you thinking about?", the chatter continues naturally — NOT "oh I sent you that message because..."

---

## 3. Other Triggers

### 3.1 Fan Subscribes for First Time — Welcome (W-1 + AF-1 + AF-2)

**Status:** Already configured in Infloww. This IS the automated Welcome Journey.

**Strategy review:**

| Message | Timing | Content |
|---------|--------|---------|
| **W-1** | Immediately on subscribe | Short welcome (1-2 sentences) + free content (photos). Creates anticipation. |
| **AF-1** | 2-3 min after W-1 | Context setter + ego boost. "I was about to leave but you're too interesting." |
| **AF-2** | 1-2 min after AF-1 | Engagement hook — ask name. Goal: get a response. |

**Configuration:**
- Trigger: Fan subscribes for first time
- Frequency: Send only once
- Collections: 3-5 variations of the welcome sequence to avoid repetition across fans who talk to each other
- Stop on reply: ON (chatter takes over immediately)
- Delay: Immediately (fan expects a welcome)

**Key rules:**
- W-1 MUST include free content (photos/videos at $0). Immediate value.
- AF-2 MUST end with a question to provoke response. The name question is reliable: "what's your name babe? 😊"
- NEVER mention it's automated. Never say "welcome to my page!" — sounds like a landing page.
- Total W-1 to AF-2: under 5 minutes. The fan is HOT right now. Don't let them cool off.

### 3.2 Fan Purchases PPV — Post-Purchase Reinforcement

**Status:** NOT configured. HIGH PRIORITY to implement.

**Why it matters:** The moment after a purchase is peak emotional engagement. The fan just spent money — he needs validation that it was worth it. An automated reinforcement here boosts satisfaction and primes for the NEXT purchase.

**Strategy:**

| Setting | Value |
|---------|-------|
| Trigger | Fan purchases PPV |
| Delay | After delay, 1-2 min |
| Frequency | Every time (rotating collections) |
| Stop on reply | ON |
| Collections | 5-8 |

**Message examples (adapt per model):**

- `fuck 🥵 did you see it??`
- `mmm I hope you liked that one as much as I liked making it 😏`
- `that one was special... you better appreciate it 😈`
- `god I got so turned on recording that for you`
- `you have no idea what you do to me 🥵`

**Rules:**
- Short, 1 sentence max
- Sexual/excited tone — she's reacting to HIM seeing her content
- NEVER mention price or money
- NEVER say "thanks for the purchase" — breaks the illusion completely
- Feeds ego driver: he just caused HER reaction

**Segmentation:** Consider different messages for first-time buyers vs repeat buyers:
- First-time: More emotional, more excited ("omg you actually... 🫣")
- Repeat: More intimate, assumes comfort ("I knew you couldn't resist 😈")

### 3.3 Subscription Near Expiry — Retention

**Status:** NOT configured. HIGH PRIORITY.

**Why:** If the sub's subscription is about to expire and we don't act, we lose them. This is a retention touchpoint.

**Strategy:**

| Setting | Value |
|---------|-------|
| Trigger | Fan's subscription near expiry |
| Delay | After delay, 2-3 min |
| Frequency | Send only once |
| Stop on reply | ON |
| Collections | 5-8 |

**Message approach:** GFE emotional. Make the fan feel he'd be LOSING something valuable.

**Message examples:**

- `hey... I realized we haven't talked in a while and I miss that 💕`
- `{name} where have you been 😩 I was thinking about you`
- `I have something I've been saving just for you... but you gotta stick around to see it 😏`
- `don't disappear on me babe 💗 I'm not done with you yet`
- `I feel like we had something and I don't want to lose that 🥺`

**Rules:**
- NEVER mention the subscription directly ("your sub is expiring" = corporate garbage)
- NEVER mention money or renewal
- Pure GFE — she misses him, she wants him around
- The fan should feel like the MODEL wants him to stay, not the business
- Include free content in at least 2 collections (incentive to re-engage)

### 3.4 Subscription Expired — Win-Back

**Status:** NOT configured. MEDIUM PRIORITY.

**Why:** Fan already left. This is a last-ditch attempt. Limited because we can't chat freely after expiration — but the message can still be seen.

**Strategy:**

| Setting | Value |
|---------|-------|
| Trigger | Fan's subscription expired |
| Delay | After delay, 1-2 min |
| Frequency | Send only once |
| Stop on reply | ON |
| Collections | 3-5 |

**Message examples:**

- `hey... I noticed you're gone 😔 I hope everything's okay`
- `I was about to send you something special and realized you left 😩`
- `{name}... I'm not gonna lie, I miss talking to you 💕`

**Rules:**
- Emotional, not transactional
- NEVER mention "resubscribe" or pricing
- The goal is to create enough emotional pull that the fan comes back on his own
- Keep it short — one message per collection (no chains, he may not be able to respond)

### 3.5 Fan Resubscribes After a Break — Re-Welcome

**Status:** NOT configured. HIGH PRIORITY.

**Why:** This fan CAME BACK. He's already shown high intent. The re-welcome must feel like a genuine reunion, not the same welcome a new sub gets.

**Strategy:**

| Setting | Value |
|---------|-------|
| Trigger | Fan resubscribes after a break |
| Delay | Immediately |
| Frequency | Send only once |
| Stop on reply | ON |
| Collections | 5-8 |

**Message chain (2 msgs per collection):**

- C1: `omg you're back!! 😍` → (15s) → `I literally missed you so much`
- C2: `{name}!!! 💕💕` → (10s) → `ok I'm so happy rn you have no idea`
- C3: `wait... is that you?? 🥺` → (15s) → `I thought you forgot about me`
- C4: `FINALLY 😩` → (10s) → `I've been saving something for when you came back...`
- C5: `omg omg omg 😍` → (15s) → `don't you EVER leave me like that again`

**Rules:**
- Must acknowledge he was GONE and she NOTICED
- Excitement, not guilt
- NEVER say "welcome back to my page" — that's mass message energy
- Include free content in at least 2 collections as a "welcome back gift"
- After he responds, chatter should treat him like a Spender (short rapport → sexting). He came back because he wants more.

### 3.6 Fan's Birthday — GFE Touchpoint

**Status:** NOT configured. MEDIUM PRIORITY.

**Why:** Easy win. Low effort, high emotional impact. Makes the fan feel genuinely special. Pure GFE.

**Strategy:**

| Setting | Value |
|---------|-------|
| Trigger | Fan's birthday |
| Delay | Immediately |
| Frequency | Send only once |
| Stop on reply | ON |
| Collections | 5 |

**Message examples:**

- `happy birthday babe!! 🎂💕 I have a little something for you...`
- `it's your birthday?? omg 🥳 I have a surprise for you 😏`
- `happy birthday {name}!! 💕 today you get something special from me`
- `birthday boyy 🎂🥰 I made you a little present...`
- `omg happy birthday!! 🎉 guess what... I'm your gift today 😏`

**Rules:**
- Include free content (photos/short video) as a "birthday gift" — every collection
- Warm + playful tone
- If the fan responds, chatter can use the birthday as a natural pivot to sexting: "let me give you a proper birthday present 😏"
- This is pure relationship building. The ROI comes from the emotional bond, not a direct sale.

---

## 4. Rules & Best Practices

### Message Content Rules

1. **Max 1-2 sentences per message.** Nudges are spontaneous texts, not emails.
2. **Vary emoji use.** Not every message has emojis. Some have 1, some have 2, some have 0. Never 3+ emojis.
3. **No banned words.** Scan every message against the OF banned words list before publishing.
4. **Never include PPV/paid content in nudges.** The nudge generates conversation. Sales happen in the session.
5. **Never mention automation.** No "automatic", "system", "notification", "welcome to my page".
6. **{name} in 30% of collections.** Powerful when used sparingly. Overuse = obviously automated.
7. **Adapt per model.** These templates are generic. Each model needs messages that match her personality, vocabulary, emoji style, and persona.

### Configuration Rules

1. **Always use delay (2-5 min).** Immediate sends feel robotic.
2. **Always enable Stop on Reply.** When the fan responds, the chatter must take over.
3. **Always exclude fans with unread messages.** Don't pile messages on fans who already wrote to us.
4. **Always exclude fans sent messages recently (6h minimum).** Prevents double-nudging during active conversations.
5. **Always exclude Creators.**
6. **Set frequency to "every time"** for nudges (rotating collections). Set to "only once" for welcome, expiry, birthday.

### What Smart Messages Should NEVER Do

1. **Sell.** No PPV, no prices, no "check out my new content". That's mass message territory.
2. **Sound generic.** "Hey! How are you?" is garbage. Every message must have personality.
3. **Replace the chatter.** Smart Messages start conversations. Chatters close sales.
4. **Stack.** If exclude filters aren't set properly, a fan could get nudge + welcome + post-purchase in the same hour. That's spam.
5. **Reference themselves.** If the fan says "you just texted me", the chatter plays it natural ("yeah I saw you were on 😏"), never "oh that was an automated message".

### Adaptation Checklist (Per Model)

When creating model-specific Smart Messages:

- [ ] Messages match the model's personality and vocabulary?
- [ ] Emoji style matches the model's texting style?
- [ ] Cultural references are appropriate? (e.g., Latina model uses different slang than Asian model)
- [ ] No banned words in any message?
- [ ] At least 3 collections use {name} tag?
- [ ] Mix of 1-msg and 2-msg collections?
- [ ] Wait times between M1 and M2 vary (10s, 15s, 20s)?
- [ ] No two collections sound too similar?
- [ ] VIP messages feel warmer than LOW messages?
- [ ] Messages don't reference specific content that might not exist?

---

## 5. Operational Format — Implementation Per Model

Smart Messages **cannot be imported via Excel.** They must be created manually in Infloww, one by one. The deliverable for each model is a **copy-paste blueprint** that anyone can follow.

### 5.1 Blueprint Format

For each model, we generate a **Smart Message Blueprint** file: `[model]/smart-messages-blueprint.md`

The blueprint contains everything needed to set up all Smart Messages for that model, organized for sequential copy-paste execution.

**Blueprint structure per Smart Message:**

```
================================================================
SM-NUDGE-VIP — [Model Name]
================================================================

CONFIGURATION:
  Trigger:           Fan comes online
  Include:           Whale, Shark
  Exclude:           Sent messages recently (0d 6h), Unread messages, Creators
  Action:            After delay, 2 ~ 5 minutes
  Frequency:         Every time fan matches trigger
  Stop on reply:     YES
  Unsend messages:   NO

────────────────────────────────────────
COLLECTION 1
────────────────────────────────────────
Message 1:
hey you 💕

Wait: 0 min 15 sec

Message 2:
I was literally just thinking about you

────────────────────────────────────────
COLLECTION 2
────────────────────────────────────────
Message 1:
mmm look who's here 😏

Wait: 0 min 15 sec

Message 2:
perfect timing... I just got comfortable in bed

[... Collections 3-10 ...]
```

### 5.2 Why This Format

1. **Each message is on its own line.** The operator selects the text, copies, pastes into Infloww. No parsing needed.
2. **Configuration is spelled out.** The operator follows the settings like a checklist — no decisions required.
3. **Collections are numbered and separated.** Easy to track progress (done 5 of 10, 5 left).
4. **Attachment notes are inline.** Where content needs to be attached (free teaser, PPV), it's noted right next to the message.

### 5.3 Implementation Workflow

1. **Script Manager** creates the blueprint file for a model (adapting generic templates to model personality)
2. **Blueprint gets reviewed** by Pau / team
3. **Operator** opens the blueprint + Infloww side by side
4. **Operator creates each Smart Message** following the blueprint top to bottom:
   - Create SM → set config → create collections → paste messages → set waits → attach content where noted
5. **Operator marks completion** (checkbox or Slack confirmation)
6. **QA check:** Someone verifies the SM matches the blueprint (spot-check 2-3 collections)

### 5.4 Content Requirement Per Model

For SM-NUDGE-ZERO, each model needs:
- **5 free teaser photos** (lingerie/clothed, nothing explicit — used in ZERO nudge collections)
- **3-5 low-price PPV content pieces** ($3-5 each — used in ZERO nudge collections)

These must be prepared BEFORE the operator starts building the Smart Messages. Without content, ZERO nudges can't be set up.

### 5.5 Rollout Order

For the first model, the full setup takes ~30-45 minutes per model (4 Smart Messages × 10 collections × copy-paste). After the operator has done 2-3 models, time drops to ~20 minutes.

Recommended rollout:
1. Start with 1 test model (highest traffic) — monitor for 1 week
2. Analyze response rates per segment
3. Adjust if needed, then roll out to remaining models in batches of 5

---

## 6. Priority Roadmap

| Priority | Trigger | Why |
|----------|---------|-----|
| 1 | **Nudge: Fan comes online** | Highest volume opportunity. Generates daily interactions. |
| 2 | **Welcome: Fan subscribes** | Already exists but needs optimization. Most important first impression. |
| 3 | **Post-Purchase: Fan buys PPV** | Reinforces buying behavior. Easy to implement. |
| 4 | **Retention: Sub near expiry** | Prevents churn. Direct revenue impact. |
| 5 | **Re-Welcome: Fan resubscribes** | High-intent fan. Easy emotional win. |
| 6 | **Win-Back: Sub expired** | Limited impact but still worth having. |
| 7 | **Birthday** | Nice-to-have. Pure GFE. |
