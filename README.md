# Sales Digital Twin

**Recommended for non-technical people: use [HappyCapy](https://happycapy.ai) for 1-click setup and running it 24/7.**

HappyCapy is your own personal cloud computer in your browser with Claude Code as the default harness, running 24/7.

---

Find the right people to sell or partner with. Build a digital twin of the decision-maker. Test hundreds of outreach strategies in parallel. Get the winning playbook for email, sales calls, or LinkedIn.

In one line: **find who to reach → model how they decide → test many approaches → hand your team the best first move.**

---

## What this does (plain English)

Most teams pick targets by gut. Someone recommends a name. The website looks sharp. You send a note. Silence. Or worse, weeks of chasing the wrong person.

This skill slows that down on purpose.

You tell it what you are offering and who you want on the other side of the table: a customer, partner, investor, or hire.

It then does three jobs founders usually do by instinct:

1. **Find who is actually worth talking to**
2. **Figure out how that person thinks**
3. **Draft how to approach them without sounding generic or wrong**

The output is not a hype deck. It is a ranked shortlist, a researched model of each decision-maker, and a playbook for the first message and the hard objections.

---

## The simple idea

Build a **digital twin** of the person you care about.

Run **hundreds of outreach strategies** against that twin in parallel.

Watch **how they react**.

Then give your team the **final strategy** for email, sales calls, LinkedIn, or other reach-out.

Think of it as a rehearsal room for high-stakes outreach, before you spend real social capital.

---

## Workflow

### 1. You define the offer
What you are selling or partnering on. Who you want. What success looks like. What you will **not** claim.

This freeze matters. If the offer drifts mid-research, every conversation gets worse.

### 2. It finds candidates
It builds a wide list of companies and people that might fit across different types, not ten clones of the same company.

### 3. It scores and shortlists
It keeps only the strong fits. Everyone else gets a clear no with a reason. That alone saves weeks.

### 4. It locks the right person
Before deep work, it confirms the real company, brand, website, and decision-maker.

Wrong company and wrong person happen more than founders admit. If identity is not locked, research stops. No twin. No simulation. No playbook.

### 5. It researches them
Public signal only: website, LinkedIn, posts, talks, podcasts, recent news.

The goal is not a biography. It is a working model of how this person chooses, what they care about, what they distrust, and what would make them say no.

Missing data is marked as a gap. Silence is not treated as "nothing interesting."

### 6. It builds a digital twin
A researched stand-in for the decision-maker. Not sci-fi. A high-quality brief of how they reason.

Twins are graded by evidence quality. Thin brochure twins do not get expensive testing without an explicit warning.

### 7. It stress-tests outreach
It runs many email, conversation, and LinkedIn-style approaches against the twin.

This finds frames that land and phrases that backfire. It is useful rehearsal, not a crystal ball. Weak sample sizes are marked as directional only and do not fake certainty.

### 8. It gives your team the playbook
For each serious target you get:

- How to open
- How to frame the offer
- What proof to bring
- Likely objections
- At least three things **not** to say
- A first message draft
- Who else matters in the deal
- Confidence level: high, medium, or low

### 9. It ranks the portfolio (optional)
If you are choosing among many targets, it ranks them with a clear formula and publishes rejects with reasons.

Knowing who to ignore is half of good outreach.

---

## What you walk away with

- Who we considered
- Who made the cut and why
- Deep files on each serious target
- A digital twin of the decision-maker
- Simulation notes on what worked and what failed
- Approach playbooks your team can use this week
- A top list you can act on

Practical value for a non-technical founder: **fewer wrong meetings, better first messages, clearer no's.**

---

## What this is not

- Not magic lead gen
- Not "AI will close the deal for you"
- Not a substitute for taste, relationships, or a real offer
- Not a promise of real reply rates from simulation scores alone

It will not invent market activity where tools returned nothing. If a channel is empty, it says so. Fake completeness is how teams talk themselves into bad targets.

---

## When to use it

Use it when the cost of a bad conversation is high:

- Partner selection in a new market
- Enterprise outreach where the buyer is specific
- Investor targeting when thesis fit matters
- Hiring conversations where motivation and constraints matter
- Any situation where "just send more messages" is expensive in reputation

Skip it when you already have a warm intro to someone you know well. You do not need a twin for coffee with a friend.

---

## Best way to run this if you are not technical

**Use [HappyCapy](https://happycapy.ai).**

HappyCapy is your own personal cloud computer in your browser with Claude Code as the default harness, running 24/7.

That means:

- 1-click setup instead of fighting local installs
- The skill can keep working while your laptop is closed
- Non-technical founders can run the full workflow without turning into ops engineers

Open [happycapy.ai](https://happycapy.ai), start a session, install this skill, and tell it who you want to sell to or partner with.

---

## Install (technical)

### On HappyCapy or Claude Code

```bash
git clone https://github.com/ndpvt-web/sales-digital-twin.git \
  ~/.claude/skills/engagement-intel
```

Or copy this repo into `~/.claude/skills/engagement-intel/`.

### Quick start

```bash
# Find and rank a portfolio of targets
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py \
  outputs/my-run --mode portfolio

# Research one named company or person
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py \
  outputs/my-run --mode single --entity acme-ai
```

Then ask Claude:

> Run engagement intel for [your offer] targeting [customers / partners / investors] in [market].

The skill follows this path:

```
Offer
  → Find candidates
  → Score / shortlist
  → Lock identity
  → Research
  → Build digital twin
  → Simulate outreach
  → Write playbook
  → Rank top targets
```

---

## Quality rules baked in

These exist because earlier runs failed in predictable ways:

| Rule | Why it matters |
|------|----------------|
| Identity lock before deep work | Stops research on the wrong person or brand |
| Score before expensive deep-dives | Stops burning weeks on weak fits |
| Twin quality gates before simulation | Stops testing strategies on thin brochure models |
| No fake ranking on tiny samples | Stops "one lucky sim" theater |
| Empty tools marked as gaps | Stops pretending missing data is a market signal |

Success metric: **better decisions under uncertainty**, not maximized simulation scores.

---

## Who this is for

- Founders doing outbound sales or partnerships
- BD teams that want fewer spray-and-pray messages
- Operators entering a new market
- Anyone who wants a clear first-message plan before the real conversation

If you can describe your offer in plain words, you can use this.

---

## Repository layout

```
sales-digital-twin/
├── SKILL.md              # Full skill instructions for Claude
├── README.md             # This file
├── LICENSE
├── scripts/              # Setup + quality-check scripts
├── references/           # Detailed workflow, gates, anti-patterns
└── evals/                # Evaluation cases
```

For the deep technical procedure, see [`SKILL.md`](SKILL.md).

---

## Requirements

- Claude Code, or [HappyCapy](https://happycapy.ai) (recommended)
- Python 3.10+ for the gate scripts
- Optional research tools depending on your setup: browser access, LinkedIn session, X/Twitter access, YouTube transcripts, sales simulator

Non-technical users should ignore the tool list and just run it on [HappyCapy](https://happycapy.ai).

---

## License

MIT. See [LICENSE](LICENSE).

---

## Bottom line

Sales Digital Twin helps you answer four questions before you spend trust:

1. Who is actually worth the meeting?
2. Are we talking to the right company and the right person?
3. How do they decide?
4. What should we say first, and what should we never say?

Most teams answer those after ten awkward calls. This skill tries to answer them before the first one.

**Not more activity. Better judgment while you still have room to choose.**

Start here if you want the easy path: [https://happycapy.ai](https://happycapy.ai)
