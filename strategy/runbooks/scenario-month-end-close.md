# 📒 Runbook: Month-End Close & Cash Review

> **Mode**: NEXUS-Micro | **Duration**: 5 business days each month | **Agents**: 6-9

---

## Scenario

Every month you need to know three things: did we make money, how much cash do we really have, and what is coming in the next 90 days. Today the books are late, numbers come from several places that don't agree, and the owner sees the result weeks after it could have changed a decision. This runbook gives you a calm, repeatable five-day close with a one-page result at the end.

> These agents prepare and check the work. They are not a substitute for a licensed accountant or tax adviser — keep a professional in the loop for filings, audits and anything regulatory.

## Before You Start

- Access (or exports) for: bank and card statements, accounting software, payment processors, payroll
- Last month's closed figures for comparison
- A list of known one-offs this month (big purchases, refunds, new loans)

## Agent Roster

### Close Core
| Agent | Role |
|-------|------|
| Bookkeeper & Controller | Runs the close: reconciliations, accruals, journal entries |
| Accounts Payable Agent | Bills received, matched, approved and scheduled |
| Data Consolidation Agent | Brings bank, sales and payroll data into one reconciled dataset |
| FP&A Analyst | Budget vs actual and the rolling 90-day cash forecast |
| Chief Financial Officer | Reviews the result; decides what needs action |

### Support
| Agent | Role |
|-------|------|
| Financial Analyst | Margin, unit economics and trend analysis |
| Tax Strategist | Flags tax timing issues and set-asides |
| Finance Tracker | Spend tracking by category and owner |
| Report Distribution Agent | Sends the final pack to the right people |

## Execution Plan

```
Day 1: Collect
├── Data Consolidation Agent → One dataset from every source
│   ├── Bank and card transactions
│   ├── Sales / payment processor payouts
│   ├── Payroll journal
│   └── Exceptions list (duplicates, missing, unmatched)
│
└── Accounts Payable Agent → Bill sweep
    ├── All bills for the month entered
    ├── Matched to purchase orders / receipts
    └── Unpaid bills and due dates listed

Day 2-3: Reconcile
├── Bookkeeper & Controller → Reconciliations
│   ├── Every bank and card account reconciled to statement
│   ├── Payment processor payouts matched to sales (fees separated)
│   ├── Accruals and prepayments posted
│   └── Customer invoices: who owes what, and how late (aged receivables)
│
└── Finance Tracker → Spend by category vs last month

Day 4: Analyse
├── FP&A Analyst → Budget vs actual + 90-day cash forecast
│   ├── Variances over ±10% explained in one line each
│   ├── Cash low point in the next 90 days
│   └── Base / downside scenarios
│
├── Financial Analyst → Gross margin and top cost movers
└── Tax Strategist → Tax set-aside and upcoming deadlines

Day 5: Decide & Distribute
├── Chief Financial Officer → Review and actions
│   ├── 3 things that went well, 3 that need attention
│   ├── Decisions needed from the owner (with a recommendation each)
│   └── Sign-off: books locked for the month
│
└── Report Distribution Agent → Pack sent to owner / partners / accountant
```

## The One-Page Result

| Section | Contents |
|---------|----------|
| Headline | Revenue, gross margin %, net profit, cash at month end |
| Versus | Last month and budget, with arrows |
| Cash | Cash today, cash low point next 90 days, months of runway |
| Money owed to us | Total, over 30 days, over 60 days, top 5 customers |
| Money we owe | Bills due in the next 30 days |
| Actions | Up to 5 decisions, each with owner and date |

## Close Metrics

| Metric | Target | Owner |
|--------|--------|-------|
| Days to close | ≤ 5 business days | Bookkeeper & Controller |
| Accounts reconciled | 100% | Bookkeeper & Controller |
| Unexplained variances | 0 over ±10% | FP&A Analyst |
| Bills paid late | 0 | Accounts Payable Agent |
| Receivables over 60 days | Trending down | Bookkeeper & Controller |
| Forecast accuracy (30-day cash) | Within ±10% | FP&A Analyst |

## Quality Gates

| Gate | When | Agent |
|------|------|-------|
| Exceptions list cleared or explained | End of Day 1 | Data Consolidation Agent |
| All reconciliations tie to statements | End of Day 3 | Bookkeeper & Controller |
| Variances explained | End of Day 4 | FP&A Analyst |
| Books locked; no edits after sign-off | Day 5 | Chief Financial Officer |

## Common Pitfalls

- **Treating payouts as sales.** Processor payouts are net of fees and refunds; record the gross sale and the fee separately.
- **Profit is not cash.** A profitable month can still leave you short; always read the cash low point.
- **Editing closed months.** Post corrections in the current month, so reported numbers stay stable.
- **Skipping the actions.** The close is only worth doing if it ends with decisions.
