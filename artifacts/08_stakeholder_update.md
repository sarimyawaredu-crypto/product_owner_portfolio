# 8 · Stakeholder update (example)

*A worked example of the format, written as if sprint 1 had just finished. The feature is a portfolio exercise; these results are illustrative, not real.*

**To:** Founders, engineering, organizer success
**Subject:** Organizer forecast · sprint 1 review · on track

**TL;DR:** Competing events are live in the add event flow. The first revenue range works for Stockholm and is behind a feature flag. We're on track for release 1 at the end of sprint 2.

| | Status |
|---|---|
| Sprint goal | ✅ Met |
| Committed points | 18 of 18 done, stretch not started |
| Release 1 | 🟢 On track |

**What shipped**
* Organizers see similar events on the same evening while creating an event, deduplicated across sources.
* Forecast endpoint and panel for Stockholm, behind a flag for internal testing.

**What we learned**
* In internal testing, the most common reaction to the range was "why is it this wide?". This supports pulling the plain language explanation (F5) forward to early release 2.

**Decisions needed**
1. OK to invite 20 organizers to a closed beta of the forecast in sprint 2? *(Recommended: yes.)*

**Risks**
* Demand data for cities beyond Stockholm isn't loaded yet. Release 1 stays Stockholm only.

**Next sprint:** finish release 1, add analytics events, start the closed beta.
