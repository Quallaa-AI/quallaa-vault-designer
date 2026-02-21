# Quallaa Project Memory

## Knowledge Base Philosophy

KB files represent **current state and future direction** — not historical journals.
- Remove obsolete info when updating. Don't append "originally we did X" footnotes.
- If something was decided and implemented, state it as fact. Don't preserve the deliberation.
- Keep files compact. Research briefs that have been resolved go to `knowledge-base/archive/`.
- Timestamps mean "last verified accurate," not a changelog.
- See CLAUDE.md "Knowledge Base Philosophy" section for full guidance.

## Agentic Architecture Principles

Inspired by Boris Cherny (Claude Code creator) — two interviews. Full reference: `memory/cherny-principles.md`

**Model philosophy:**
- **Build for the model 6 months from now.** Your product market fit won't be great yet, but when the model catches up you hit the ground running.
- **The Bitter Lesson:** Never bet against the model. Scaffolding has ~2 month shelf life. Gains (10-20%) get wiped by the next model.
- **The product IS the model.** Expose it. Minimal scaffolding. Don't box it in with rigid orchestrators — give tools + goal, let it figure out the order.
- **Trust the model over scaffolding.** Tone guidance, schedule management, follow-up branching — all removed. Model handles these through tool descriptions and base prompts.

**Product principles:**
- **Latent demand (users):** Build things people already hack your product to do. Don't invent new workflows.
- **Latent demand (model):** Watch what the model is *trying* to do and make that easier. Research calls this "being on-distribution."
- **Speed is the principle.** If you can do it today, do it today. Underfund projects slightly — scarcity forces Claude usage and creative problem-solving.
- **Fast feedback loops.** Fix every user report within minutes. People feel heard → give more feedback → product improves faster.

**Practical tips:**
- **Use the most capable model.** Less capable models often cost MORE total tokens due to corrections. Opus one-shots what Sonnet takes 3 attempts for.
- **Plan mode 80% of tasks.** Plan → iterate on plan → auto-accept edits. Good plan = one-shot execution with Opus 4.6.
- **Unlimited tokens for experimentation.** Don't optimize/cost-cut early. Let engineers try crazy ideas. Optimize when something works at scale.
- **Be a generalist.** Cross disciplines. Engineers with design sense, PMs who code, builders who talk to users.
- **CLAUDE.md should be minimal.** Delete and rebuild rather than accumulate. With each model, you need less instruction.
- **Subagents for hard bugs:** Calibrate parallel subagent count to task difficulty (3-5-10 agents researching different angles).
- **Design tools for natural reasoning.** `scheduled_for: "2026-02-20T09:00"` not `delay_hours: 17.5`.
- **Overengineering check:** "For every plan, assess: overengineered, underengineered, or right-sized — and why."
- **Detailed session notes:** `memory/2026-02-19-scaffolding-cleanup.md`

## Agent SDK Architecture (Current)

- **Prompt assembly:** Guardrails, disclosure, timezone, contact profile, fallback context, concierge caller context. Tone and schedule management scaffolding **removed** — model trusted to handle.
- **Follow-up cron:** Single universal prompt with metadata pass-through. No per-sequence-type branching.
- **No programmatic back-off.** `shouldBackOff()` removed. Model sees conversation history + schedule data and decides for itself. No WARNING injection.
- **Unified escalation:** `escalate(target, message)` — one tool for all escalations. Booking requests are escalations where the model includes booking details. `get_open_escalations` and `resolve_escalation` complete the lifecycle.
- **18 tools** across 7 categories (escalation, scheduling, engagement, communication, internal/concierge, research). Ghost tool_definitions cleaned up.
- **Tool registry pattern:** Clean, extensible, no state machines. AsyncLocalStorage for tool context.
- **Research tools:** `web_search` (Brave Search API) for QMA agent.

## Repository Structure

| Repo | GitHub | Local Path | Purpose |
|------|--------|------------|---------|
| Main Web App | `Quallaa-AI/quallaa-web` | `~/Documents/GitHub/quallaa` | Next.js web app, API, portal |
| Mac Bridge | `Quallaa-AI/quallaa-bridge-mac` | `~/Documents/GitHub/quallaa-bridge-mac` | macOS iMessage bridge app |
| Android Bridge | `Quallaa-AI/quallaa-bridge-android` | `~/Documents/GitHub/quallaa-bridge-android` | Android SMS bridge app |

## Bridge Apps v1.0.0

Both apps released and hosted on Supabase Storage (public bucket):
- **Mac DMG:** `bridge-downloads/mac/QuallaBridge-1.0.0.dmg`
- **Android APK:** `bridge-downloads/android/QuallaBridge-1.0.0.apk`

Download links in portal: Settings → App Setup (Pro tier)

## Key Credentials & Backup

- **Android keystore:** `quallaa-bridge-android/quallaa-release.keystore` (alias: `quallaa`)
- **Mac signing:** Developer ID Application certificate, notarization via `xcrun notarytool`
- **Notarization keychain profile:** `quallaa-notarize` (Apple ID: `jefftoff@me.com`, Team ID: `C5BM8DML5Q`)
- **iCloud backup:** Critical non-git files backed up to `iCloud Drive/Quallaa Backup/`:
  - `env.local`, `env.production.local`, `quallaa-release.keystore`
  - **Re-copy when changed:** If env vars are updated or keys rotated, re-copy to iCloud backup

## Architecture Notes

- Pro tier uses bridge apps for SMS/iMessage relay from contractor's own phone number
- Starter tier uses Twilio number directly
- Both tiers have a Twilio number (Pro uses it for missed call detection only)

## Vision & Strategic Direction

- **Foundation:** A real person solving a real problem for contractors who are losing real money.
- **Mandate:** "Make something insanely great." Customers will come when the product deserves them.
- **Core thesis:** The product isn't the feature (AI text-back) — it's a real person standing behind a system that works, with certification proving it was done right.
- **Certification IS the GTM** — not friction, not compliance overhead. Contractors trust a person, not a brand.
- **Long-term arc:** Communication → Operations → Robotics → Industry Standard
- **Robotics connection:** Bridge architecture (signal → AI → device → human oversight) generalizes from phones to robots.
- **Certification scales:** Certified Pro (communication) → Certified Partner (operations) → Certified Operator (robotics)
- Key docs: `knowledge-base/strategy/certification-and-trust-strategy.md`, `knowledge-base/strategy/vision-and-long-term-trajectory.md`

## 866 Number as Top of Funnel

- **The 866 number (+18664916416) IS the marketing funnel.** Business cards say "Text this number to try it out — our AI picks up."
- **Primary GTM motion:** In-person Denver outreach (starting Feb 25, 2026) → hand business card → contractor texts 866 → concierge AI demos the product → lead created → signup
- **The product demos itself.** Contractor experiences the exact thing they'd be buying while being sold on it. No website, no demo call, no signup form needed.
- **Concierge agent** (`quallaa-concierge`, Sonnet) has 8 concierge tools: lookup_account, get_product_info, create_lead, send_signup_link, provision_account, get_account_info, check_bridge_status, send_email — plus unified `escalate` tool
- **866 routing overrides** (in `app/api/sms/incoming/route.ts`):
  - F&F contacts → Coach Q (wellness coach)
  - Everyone else → Concierge
- **QMA has its own number** (`+18339665232`, 833 toll-free, pending verification) — no 866 routing override needed
- **Business cards** in `public/Quallaa business card front.png` and `public/Quallaa business card back.png`
- Key docs: `knowledge-base/marketing/go-to-market-strategy.md`, `knowledge-base/strategy/pre-launch-marketing-plan.md`

## CLI Chat (`npm run chat`)

- `scripts/chat.ts` — interactive terminal chat with any configured AI agent
- Supports `--client "Name"`, `--agent "slug"`, `--phone "+15551234567"` flags to skip menus
- DB persistence with `trigger_type: 'cli_chat'`, `source: 'cli_chat'` — non-billable, visible in portal
- Default caller: synthetic phone `+10000000001` ("CLI Tester")

## Portal Test Message Feature

- `POST /api/portal/test-message` — runs real AI agent, returns response to portal UI, no SMS sent
- Uses synthetic phone `+10000000000` ("Test Customer") and `trigger_type: 'test'`
- Rate limited: 1 test per 60s per client

## Security Audit Script

- `npm run security-audit` — 43 static checks across 5 domains (prompt injection, auth, data handling, XSS, rate limiting)
- `scripts/security-audit.ts` (CLI) + `lib/security/audit.ts` (engine)
- Pure file analysis, no DB/env/runtime needed. `--json` flag for CI.

## QMA (Quallaa Marketing Assistant)

- **Agent:** `quallaa-marketing-assistant` | Sonnet | 10 turns | 120s timeout
- **Dedicated number:** `+18339665232` (833 toll-free, pending verification). Team escalations use verified 866 as interim.
- **Tools:** `web_search`, `escalate`, `get_open_escalations`, `schedule_followup`, `check_schedule`, `cancel_followup`
- **Cron:** `app/api/cron/qma-research/route.ts` — 4x/day weekdays, Denver business hours
- **Two-way:** Jeff texts +18339665232 → routes directly to QMA via channel lookup. No routing override needed.
- **Scheduling:** check_schedule FIRST, scheduled_for in local time. Self-schedules research follow-ups, Jeff-directed tasks, escalation nudges.
- **Brave Search:** $5/month free credits = 1,000 searches. Current usage ~300-450/month.
- **Key doc:** `knowledge-base/marketing/qma-and-email-infrastructure.md`

## Email Infrastructure

- **`send_email` tool** on concierge: Resend, branded template, back-off logic (bounce/complaint/3x unopened)
- **`agent_emails` table:** Tracks every agent-sent email with Resend ID, status lifecycle
- **Resend webhook:** `app/api/webhooks/resend/route.ts` — updates status on deliver/open/click/bounce/complain
- **`marketing_consents` table:** Consent records with audit trail (text, IP, user-agent)
- **Calculator consent checkbox:** `components/CalculatorEmailCapture.tsx`

## Twilio Compliance & Phone Numbers

- **10DLC Campaign:** IN_PROGRESS (resubmitted Feb 19, 2026). Previously FAILED (error 30909: CTA verification). Resubmitted with improved CTA, all CTIA disclosures, 3 URLs. Review: 10-15 business days.
- **Brand:** Approved (TCR ID: BIYNX4J, identity VERIFIED)
- **Toll-free pool (Starter tier interim):** 7 numbers purchased, all in messaging service. Verification auto-submitted on purchase.
  - **Verified (can send):** +18664916416 (866, concierge/escalations), +18559586034 (855, QMA verified line)
  - **In review (~12 days from Feb 19):** +18339665232 (833, QMA), +18333741553, +18669016949, +18449301943, +18557014617
- **Local numbers:** Blocked until 10DLC approved. Legacy 720 released (emergency address pending, then auto-releases).
- **Cost:** ~$15/mo for 7 toll-free numbers ($2.15 each)
- **Strategy:** Toll-free for immediate Starter provisioning. 10DLC running in parallel — if approved, can switch to cheaper local numbers later.
- **Key doc:** `knowledge-base/technical-docs/twilio-compliance-guide.md`

## Jeff's Dedicated Agent Lines

Jeff interacts with two agents as a user (not as host/operator):

| Agent | Number | Contact Name | Status |
|-------|--------|-------------|--------|
| Wellness Coach | +18664916416 (866) | Coach Q | Works now (F&F override on 866) |
| QMA | +18559586034 (855) | QMA | Verified, works now |

- Wellness-coach uses 866 via F&F code override — no dedicated number needed.
- QMA has TWO channels: 855 (verified, Jeff texts this) and 833 (primary, in review ~March 3 for cron/escalation use).
- When Jeff texts 855 → routes to QMA → responds from 855. QMA cron uses 833 (primary) once verified.
- Concierge stays on 866 — Jeff is the host, not a user.

## Ideas to Investigate

- **Portal security status display:** Show audit results in portal (green light, timestamp, "43/43 passed", details). Quallaa-branded — not Claude/Anthropic branded. Fits better as Quallaa trust signal tied to certification narrative.
