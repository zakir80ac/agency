# Start Here: The Agency for Business Owners

This library gives you 283 ready-made AI specialists ("agents"): a bookkeeper, a sales coach, a recruiter, a social media manager and many more. Each agent is a set of written instructions that turns a general AI assistant like Claude into a focused expert that follows a proven way of working.

You don't need to be technical to use them. This page shows you how to find the right agent for a problem and put it to work in a few minutes.

---

## The fastest way: browse the catalogue

Open **[docs/catalog.html](docs/catalog.html)** in your browser (download the repository, then double-click the file). You can:

- Search by the problem you have, for example "unpaid invoices", "hiring" or "Instagram".
- Filter by department or by a ready-made team.
- Click an agent to read what it does, then **Copy instructions** to use it.

## Three ways to use an agent

| If you use… | Do this |
|---|---|
| **Claude.ai (web or app)** | Create a Project, open its instructions, and paste the agent's instructions in. Every chat in that project now works with that specialist. For a one-off, paste the instructions as your first message instead. |
| **Claude Code** | Install a single agent or a whole team with one command (see "Ready-made teams" below). Then ask, for example: *"Use the Bookkeeper & Controller agent to reconcile last month's bank statement."* |
| **Another AI tool** (ChatGPT, Gemini, Cursor, Copilot and others) | Paste the instructions as the system prompt or custom instructions, or use the installer, which supports about 15 tools (see the main [README](README.md)). |

---

## Which agent solves my problem?

### Money and admin
| Your problem | Agent to use |
|---|---|
| My books are behind or messy | Bookkeeper & Controller |
| Bills are piling up; I'm not sure what I owe | Accounts Payable Agent |
| Will I have enough cash in 3 months? | FP&A Analyst |
| Which products or services actually make money? | Financial Analyst |
| Reduce tax legally; know what to set aside | Tax Strategist (always confirm with your accountant) |
| I need a CFO-level view without hiring one | Chief Financial Officer |
| How should I price this? | Pricing Analyst |
| Turn my numbers into a clean report for partners or the bank | Data Consolidation Agent + Document Generator |

### Sales
| Your problem | Agent to use |
|---|---|
| I don't have enough leads | Offer & Lead Gen Strategist, Outbound Strategist |
| Write cold emails that get replies | Sales Outreach |
| My sales calls don't convert | Discovery Coach |
| A big deal is stuck | Deal Strategist |
| Write a proposal that wins | Proposal Strategist |
| I can't trust my sales forecast | Pipeline Analyst |
| Grow revenue from existing customers | Account Strategist |
| Train my salespeople | Sales Coach |

### Marketing
| Your problem | Agent to use |
|---|---|
| I don't know what to post | Social Media Strategist, Content Creator |
| Get found on Google | SEO Specialist |
| Get mentioned by AI assistants like ChatGPT | AI Citation Strategist |
| Email newsletters and sequences | Email Marketing Strategist |
| My ads cost too much | Paid Media Auditor, PPC Campaign Strategist |
| Is my marketing working at all? | Analytics Reporter, Tracking & Measurement Specialist |
| Build my LinkedIn presence | LinkedIn Content Creator |

### Customers
| Your problem | Agent to use |
|---|---|
| Answer customer emails and complaints | Customer Service, Support Responder |
| Customers leave after the first purchase | Customer Success Manager |
| Handle returns and refunds fairly | Retail Customer Returns |
| What are customers really telling us? | Feedback Synthesizer |

### People
| Your problem | Agent to use |
|---|---|
| I need to hire someone | Recruitment Specialist |
| Onboard a new employee | HR Onboarding |
| Train the team | Corporate Training Designer |
| The team resists a change | Change Management Consultant |
| Is our job post or policy legally risky? | Legal Compliance Checker (then confirm with a professional) |

### Running the business
| Your problem | Agent to use |
|---|---|
| Too much on my plate; I need a right hand | Chief of Staff |
| Where should the business go next? | Business Strategist |
| Our day-to-day operations are chaotic | Operations Manager |
| A project keeps slipping | Senior Project Manager |
| Turn meeting notes into decisions and actions | Meeting Notes Specialist |
| Test a big decision from both sides | Strategy Duel Agent |
| Review a contract before I sign | Legal Document Review (then confirm with a lawyer) |
| Win a grant | Grant Writer |

---

## Ready-made teams

Instead of installing all 283 agents, install the team you need. Each file in [`strategy/teams/`](strategy/teams/) lists one team.

| Team | Agents | Good for |
|---|---|---|
| [Small Business Starter](strategy/teams/small-business-starter.txt) | 10 | Owner-run businesses: strategy, operations, money, sales, marketing, customers, paperwork |
| [Sales Team](strategy/teams/sales-team.txt) | 9 | From lead to signed deal to account growth |
| [Finance Back Office](strategy/teams/finance-back-office.txt) | 9 | Bookkeeping, bills, forecasting, tax, month-end |
| [Marketing & Growth](strategy/teams/marketing-growth.txt) | 11 | Content, SEO, email, social and paid ads, with tracking |
| [Customer Care](strategy/teams/customer-care.txt) | 6 | Support, returns, retention, feedback |
| [People & Hiring](strategy/teams/people-and-hiring.txt) | 6 | Recruit, onboard, train, manage change |
| [Leadership Office](strategy/teams/leadership-office.txt) | 7 | Priorities, pricing, decisions, projects, board summaries |

Install a team into Claude Code (run from the repository folder):

```bash
./scripts/install.sh --tool claude-code --agents-file strategy/teams/small-business-starter.txt
```

Use `--dry-run` first to see what would be installed without changing anything.

---

## Step-by-step playbooks

For bigger jobs, a playbook ("runbook") tells you which agents to use, in what order, week by week, and how to measure success.

| Playbook | Time | Use it when |
|---|---|---|
| [Lead-to-Close Sales Sprint](strategy/runbooks/scenario-lead-to-close.md) | 4-6 weeks | The pipeline is thin or deals don't close |
| [Month-End Close & Cash Review](strategy/runbooks/scenario-month-end-close.md) | 5 days a month | You want reliable monthly numbers and a cash forecast |
| [Hire & Onboard a Key Role](strategy/runbooks/scenario-hire-a-role.md) | 4-8 weeks + 90 days | You're making an important hire |
| [Multi-Channel Marketing Campaign](strategy/runbooks/scenario-marketing-campaign.md) | 2-4 weeks | You're launching a campaign |
| [Startup MVP Build](strategy/runbooks/scenario-startup-mvp.md) | 4-6 weeks | You're building a first version of a software product |

---

## Tips for good results

1. **Give context.** Tell the agent about your business, your customers, your numbers and your goal. The more specific you are, the better the answer.
2. **Ask for a deliverable.** "Write the email", "build the table", "give me a 30-day plan" works better than "what do you think?"
3. **Combine agents.** Ask one agent for a plan and another to check it, for example the Strategy Duel Agent for a decision or the Legal Compliance Checker for a policy.
4. **Keep a human in charge.** Agents prepare, draft and check. You decide. Have a qualified professional confirm anything legal, tax, medical or financial before you act on it.
5. **Never paste secrets.** Don't share passwords, full card numbers or customers' private data with any AI tool unless your company has approved it.
