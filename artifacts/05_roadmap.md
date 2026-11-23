# 5 · Roadmap

Two week sprints, starting January 2027. Dates are a plan, not a promise. They move when we learn something.

```mermaid
gantt
    title Organizer revenue forecast
    dateFormat YYYY-MM-DD
    axisFormat %d %b
    section Discovery
    Interviews and concierge forecasts      :         d1, 2027-01-04, 14d
    Prototype backtest                     :         d2, 2027-01-11, 7d
    section Release 1
    F3 Competing events                    :         r1a, 2027-01-18, 10d
    F1 Revenue range                       :         r1b, 2027-01-18, 24d
    section Release 2
    F5 Explanation                         :         r2a, after r1b, 10d
    F2 Compare dates                       :         r2b, after r1b, 14d
    F4 Seasonality signal                  :         r2c, after r1b, 14d
    section Release 3
    F10 Venue capacity, F9 Accuracy, F6 PDF :        r3, after r2b, 24d
    section Decision point
    Review accuracy before pricing work    :milestone, m1, after r3, 0d
```

## Now / Next / Later

| Now (Q1 2027) | Next (Q2 2027) | Later |
|---|---|---|
| Competing events on the same night | Venue capacity lookup | Ticket price suggestion, once accuracy is proven |
| Revenue range for a date | Forecast accuracy tracking | Alerts when a competing event is announced |
| Plain language explanation | PDF export for sponsors | Forecasts for cities beyond the pilot |
| Compare candidate dates | | |

## Decision points

* **End of discovery:** if fewer than half of interviewed organizers compare dates, narrow the scope to competing events only.
* **After release 3:** if the forecast range contains actual attendance in under 70% of reported events, fix the model before starting price suggestions.
