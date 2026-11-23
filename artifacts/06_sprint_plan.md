# 6 · Sprint 1 plan

**Sprint:** 18 to 29 January 2027 (10 working days)
**Sprint goal:** *An organizer creating an event in Stockholm can see every similar event on the same evening, and a first revenue range for their date.*

## Capacity

| Person | Role | Days available | Focus factor | Effective days |
|---|---|---|---|---|
| Dev A | Full stack | 10 | 0.7 | 7.0 |
| Dev B | Backend and data | 8 (2 days leave) | 0.7 | 5.6 |
| Designer | UI | 4 (shared with another team) | 0.8 | 3.2 |
| **Total** | | | | **15.8 days** |

The focus factor accounts for meetings, reviews and support. Last sprint's velocity was 21 points; with two days of leave I plan for about 18.

## Commitment

| Story | Points | Owner | Notes |
|---|---|---|---|
| F3a Query competing events by city, category and evening | 5 | Dev B | Reuses the search index |
| F3b Show competing events in the add event flow | 3 | Dev A, Designer | |
| F1a Forecast endpoint (demand index × capacity × competition) | 5 | Dev B | Port from the prototype |
| F1b Forecast panel with low, expected and high range | 3 | Dev A, Designer | |
| F1c "Not enough data" state | 2 | Dev A | |
| **Total committed** | **18** | | |
| *Stretch:* analytics events for forecast opened and dates compared | 2 | Dev A | Needed for metrics before launch |

## Risks

| Risk | Plan |
|---|---|
| Demand data for Stockholm not loaded in production yet | Dev B starts with the data load on day 1; fall back to competing events only if it slips |
| Designer only 4 days | Design F3b and F1b in the first three days; developers use the component library for the rest |

## Ceremonies

| | When | Length |
|---|---|---|
| Planning | Monday, day 1 | 2 hours |
| Daily standup | Every day | 15 minutes |
| Backlog refinement | Wednesday, week 2 | 1 hour |
| Review with organizer success | Friday, day 10 | 45 minutes |
| Retrospective | Friday, day 10 | 45 minutes |
