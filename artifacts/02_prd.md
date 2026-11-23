# 2 · PRD: Organizer revenue forecast

| | |
|---|---|
| **Status** | Draft for review |
| **Owner** | Product |
| **Stakeholders** | Engineering, data, design, organizer success |
| **Target release** | Release 1 and 2 (see roadmap) |

## Summary

When an organizer is choosing a date, EventCast shows an expected attendance and revenue range for that date, city and venue, the competing events on the same night, and how the date compares with the alternatives they're considering.

## Goals

1. Help organizers pick a better date **before** they commit to a venue.
2. Make EventCast part of the planning phase, not only the publishing phase.
3. Turn the event pool, our biggest asset, into a reason for organizers to come back.

## Non goals

* Setting ticket prices for the organizer (later; low confidence today).
* Forecasting individual ticket sales curves over time.
* Guaranteeing an outcome. The forecast is a range, always shown with its uncertainty.

## Users and scenarios

**Primary:** Lina runs a 400 person indie concert series in Stockholm. She's choosing between three Fridays in March and wants to avoid clashing with a big arena show.
**Secondary:** A meetup organizer deciding whether December is worth it or whether to wait until January.

## Requirements

| ID | Requirement | Priority |
|---|---|---|
| R1 | Organizer enters city, date, venue capacity, ticket price and category | Must |
| R2 | Show expected attendance and revenue as a low, expected and high range | Must |
| R3 | List competing events in the same city, category and evening, from the event pool | Must |
| R4 | Explain the main drivers in one or two sentences ("July is a peak month; 2 similar events that night") | Must |
| R5 | Compare up to 3 candidate dates side by side | Should |
| R6 | Look up venue capacity automatically when the venue is known | Should |
| R7 | After the event, ask for actual attendance and show forecast accuracy | Should |
| R8 | Export as PDF for sponsors | Could |

## How the forecast works (v1)

`attendance = capacity × base sell through × seasonal demand index ^ elasticity × competition factor`, capped at capacity, with a range from the uncertainty in the demand model. Inputs: city visitor demand by month (official accommodation statistics), competing events from the EventCast pool, and the organizer's own capacity and price. A working prototype is in [event_demand_forecast](https://github.com/sarimyawaredu-crypto/event_demand_forecast).

## Success metrics

| Metric | Target after 8 weeks |
|---|---|
| Organizers creating an event who open the forecast | 30% |
| Forecast users who compare two or more dates | 40% |
| Organizers who return to EventCast within 30 days (forecast users vs others) | +10 points |
| Forecast range contains actual attendance (where reported) | 70% |

**Guardrail:** event publishing completion rate must not drop. The forecast must not become friction in the publishing flow.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| A confident looking number that turns out wrong damages trust | Always show a range and its drivers; track accuracy publicly to organizers |
| Thin data in smaller cities | Show the forecast only when data quality passes a threshold; otherwise show competing events only |
| Organizers read the forecast as a promise | Clear wording: "expected range based on..." and no single headline number |

## Open questions

1. Should the forecast be free for everyone or part of a future paid tier?
2. Do we ask for actual attendance automatically after the event via ticketing data, or manually?
