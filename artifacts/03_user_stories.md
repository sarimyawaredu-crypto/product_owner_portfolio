# 3 · Epics and user stories

Written to the INVEST criteria, with acceptance criteria in Given / When / Then form so they translate directly into tests.

## Epic E1 · Forecast core

### F1 · Revenue range for a chosen date
**As an** organizer planning an event, **I want** to see an expected attendance and revenue range for a date, **so that** I can judge whether the date is worth it before booking the venue.

```gherkin
Scenario: Forecast for a date with enough data
  Given I am creating an event in "Stockholm" with capacity 400 and ticket price 250 SEK
  When I choose the date "2027-03-12" and open the forecast
  Then I see expected attendance as a low, expected and high value
  And I see expected revenue calculated as attendance times ticket price
  And no value is higher than the capacity

Scenario: Not enough data for the city
  Given the city has less than 24 months of demand data
  When I open the forecast
  Then I see "Not enough data for a reliable forecast in this city yet"
  And I still see competing events for the date
```

### F3 · Competing events on the same night
**As an** organizer, **I want** to see similar events on the same evening, **so that** I can avoid splitting my audience.

```gherkin
Scenario: Show competing events
  Given there are 2 concerts in Stockholm on 2027-03-12 after 18:00
  When I forecast a concert on that date
  Then I see both events with title, venue, time and source
  And the forecast mentions "2 similar events that evening"

Scenario: Duplicates are not counted twice
  Given the same concert appears on two sources
  When I view competing events
  Then it is listed once
```

### F2 · Compare candidate dates
**As an** organizer choosing between dates, **I want** to compare up to three side by side, **so that** I can pick the best one in one view.

```gherkin
Scenario: Compare three dates
  Given I have added three candidate dates
  When I open the comparison
  Then I see each date's revenue range and number of competing events
  And the date with the highest expected revenue is highlighted
  And I cannot add a fourth date
```

## Epic E2 · Trust

### F5 · Explain the forecast
**As an** organizer, **I want** a plain language reason for the forecast, **so that** I understand and trust it.

```gherkin
Scenario: Explanation names the main drivers
  Given a forecast where the month is a peak month and there are 2 competing events
  When I view the forecast
  Then I see one or two sentences naming the season and the competition
  And no statistical terms are shown by default
```

### F9 · Forecast accuracy after the event
**As an** organizer, **I want** to see how close the forecast was after my event, **so that** I know how much to rely on it next time.

```gherkin
Scenario: Accuracy shown after actual attendance is known
  Given my event took place and actual attendance was 310
  And the forecast range was 280 to 340
  When I open the event
  Then I see "Actual attendance was within the forecast range"
```

## Definition of Ready
* Story follows the template and has acceptance criteria
* Dependencies identified and either done or planned in the same sprint
* Design available if there's UI
* Estimated by the team

## Definition of Done
* Acceptance criteria pass as automated tests
* Code reviewed and merged
* Works on web and mobile breakpoints
* Analytics events for the success metrics are in place
* Product owner has accepted it in the review
