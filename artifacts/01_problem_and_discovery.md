# 1 · Problem and discovery plan

## Problem statement

> Independent event organizers choose dates and venues mostly on gut feeling and venue availability. They only learn whether a date was good when tickets do or don't sell, which is too late to change it.

**Who:** independent and small organizers (concerts, meetups, workshops, conferences under 2 000 attendees) who already use EventCast to publish or ticket events.
**When:** in the planning phase, typically 1 to 6 months before the event, while comparing a few candidate dates.
**Cost of the problem:** an empty room, a loss on the venue deposit, or a clash with a bigger event on the same night.

## Assumption map

Before building anything, list what has to be true for the feature to succeed, and rank by how risky and how unknown each assumption is.

| # | Assumption | Type | Risk if wrong | What we know | Test first? |
|---|---|---|---|---|---|
| A1 | Organizers compare several dates before committing | Desirability | High: no decision to support | Anecdotal | **Yes** |
| A2 | They would trust a range from EventCast over their own judgement | Desirability | High | Nothing | **Yes** |
| A3 | Competing events on the same night are a real worry | Desirability | Medium | Organizers raise it often | Yes |
| A4 | Our event pool and public demand data are enough to make a useful range | Feasibility | High | A prototype on Stockholm data exists | Yes |
| A5 | A better date choice changes ticket sales enough to notice | Viability | Medium | Industry intuition only | Later, via accuracy tracking |
| A6 | Organizers would pay for it, or it brings them to free ticketing | Viability | Medium | Nothing | After launch |

## Interview guide (30 minutes, 8 to 10 organizers)

Goal: learn how dates are chosen today, not pitch the feature.

1. Tell me about the last event you organised. How did you pick the date?
2. What other dates did you consider? What made you drop them?
3. What information did you wish you had at that point?
4. Has an event ever done worse than expected? What do you think happened?
5. How did you find out about other events on the same night, if at all?
6. Who else is involved in choosing the date (venue, sponsors, co organisers)?
7. *(Show a rough mockup of a forecast range.)* What would you do with this? What would make you not trust it?

**Avoid:** "Would you use a tool that...?" Hypothetical questions get polite yeses.

## Cheapest tests before building

| Test | Assumption | Signal we need |
|---|---|---|
| Interviews above | A1, A2, A3 | At least 6 of 10 compare two or more dates; at least half describe a clash or a bad date |
| Concierge forecast: send 5 organizers a hand made forecast for their next event | A2, A4 | At least 3 change or confirm their date because of it |
| Fake door: "Forecast this date" button on the add event page, leading to a waitlist | A1 | Over 15% of organizers creating an event click it |
| Backtest the prototype on past events with known attendance | A4 | Forecast range contains actual attendance in at least 70% of cases |
