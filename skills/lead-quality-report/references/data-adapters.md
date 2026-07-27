# Data Adapters — Column Mapping Reference

This file maps the column names from each data source to the canonical lead schema used by the Lead Quality Report skill. When ingesting data, read this file to determine which columns map to which canonical fields.

---

## Adapter 1 — Cortana S3 Sales Export

**File pattern:** `*S3-SALES Export*.csv`

| Cortana Column | Canonical Field | Notes |
|---------------|----------------|-------|
| Email | lead_email (dedup key) | |
| First Name | lead_name (part 1) | Combine with Last Name |
| Last Name | lead_name (part 2) | |
| Income | cash_collected | This is the payment amount |
| Date | close_date | Payment/close timestamp. Format: `2026-03-14T17:44:36Z UTC-04:00` |
| Phones | phone | May be blank |
| Sale Group | sale_group | Stripe charge ID — can be used for payment verification |
| Name | product_name | Describes what was sold. Parse for offer tier. |
| Origin Source | ad_set_name / utm_source | Maps to the ad set that first touched this lead. E.g. "AS001 - BROAD TARGETING - MULTIPLE ICPs - F+M - 25+" |
| Last Source | last_touch_source | Last ad set before conversion. May differ from Origin Source. |
| Status | payment_status | Usually "SENT" |
| Info | is_recurring | If "Recurring" → this is a repeat payment, not a new close |
| Order Name | order_ref | Additional reference |

**Dedup logic for sales:**
- Group by email
- First record per email (by date) where Info is NOT "Recurring" = the new close
- All subsequent records for the same email = recurring payments (tag `is_recurring = true`)
- Recurring payments count toward "All Cash" but NOT "New Cash" or close counts

---

## Adapter 2 — Cortana S3 Calls Export

**File pattern:** `*S3-CALLS Export*.csv`

| Cortana Column | Canonical Field | Notes |
|---------------|----------------|-------|
| Email | lead_email (dedup key) | Match to sales records |
| First Name | lead_name (part 1) | |
| Last Name | lead_name (part 2) | |
| Date | call_date | Timestamp of the call booking/event |
| Phones | phone | |
| State | call_state | QUALIFIED or CANCELLED |
| Status | notification_status | SENT or NO_ADSPEND_SOURCE |
| Name | call_type | Usually "Call-Discovery Call" |
| Origin Source | ad_set_name / utm_source | Same as sales export |
| Last Source | last_touch_source | |
| Extra data | extra_info | "Refund" = cancelled booking |

**Dedup logic for calls:**
- Group by email, sort by date ascending
- First QUALIFIED call per email = the initial sales call (use this date as `generated_date`)
- Subsequent QUALIFIED calls = follow-up calls (tag `is_fu_call = true`)
- CANCELLED calls with "Refund" in Extra data = cancelled bookings (outcome = Cancelled)
- Multiple cancelled + rebooked = use the final qualified call date

**Junk lead detection:**
- Profanity in name fields → flag as junk, exclude from metrics
- Fake/test emails (e.g., contains client domain name) → flag and exclude
- NO_ADSPEND_SOURCE status → lead came from non-paid source, tag as organic

---

## Adapter 3 — Cortana Aggregated Report

**File pattern:** `*Report*.csv` (with columns like Name, Cost, Revenue, ROAS)

| Cortana Column | Canonical Field | Notes |
|---------------|----------------|-------|
| Name | ad_creative_name | The ad creative / ad name |
| Status | ad_status | |
| Budget | budget | |
| Clicks | clicks | |
| Cost | ad_spend | Total spend on this creative |
| Total Revenue | total_revenue | Includes recurring revenue |
| Revenue | revenue | May differ from Total Revenue |
| Profit | profit | Revenue - Cost |
| Sales | closes | Number of closed deals from this creative |
| ROI | roi_percent | |
| ROAS | roas | Revenue / Cost |
| Calls | calls_booked | Calls attributed to this creative |
| Cost per Call | cost_per_call | |
| Leads | total_leads | |
| New Leads | new_leads | First-time leads (excluding returning) |

**Usage:** This is a convenience export — it gives you ad-level aggregated metrics without needing to calculate them yourself. Use it to cross-reference your calculations from the raw sales + calls exports. If numbers don't match, the raw exports are the source of truth.

**Note:** The "Name" column contains the ad creative name (e.g., "Your Email Could Be Worth $1M+ More Per Year"). Multiple rows may share the same Name — these are different ad variations or ad sets running the same creative. Aggregate by Name for creative-level analysis, or keep separate for ad-set-level analysis.

---

## Adapter 4 — Meta Ads Manager CSV

**File pattern:** `*.csv` with "Campaign name" and "Amount spent" columns

| Meta Column | Canonical Field | Notes |
|------------|----------------|-------|
| Reporting starts | period_start | |
| Reporting ends | period_end | |
| Campaign name | campaign_name | |
| Campaign delivery | delivery_status | active / inactive |
| Amount spent (USD) | ad_spend | **The only revenue-related number to trust from Meta** |
| Impressions | impressions | |
| Link clicks | link_clicks | |
| CTR (link click-through rate) | ctr | |
| CPC (cost per link click) (USD) | cpc | |
| Reach | reach | |
| Frequency | frequency | |
| CPM (cost per 1,000 impressions) (USD) | cpm | |
| Landing page views | landing_page_views | |
| Results | meta_reported_results | **DO NOT USE for conversion counts** |
| Cost per results | meta_cost_per_result | **DO NOT USE for ROAS calculations** |

**CRITICAL:** Meta's "Results" and conversion columns are unreliable. Use Meta ONLY for spend, clicks, impressions, reach, and frequency. All conversion data comes from Cortana/Hyros.

**Export levels:** This CSV may be at campaign level, ad set level, or ad level depending on how the user exported it. Ad-level is most useful. If campaign-level only, you'll need to allocate spend across creatives using the Cortana aggregated report's relative spend distribution.

---

## Adapter 5 — Airtable SRF Table (FL Model)

**Base:** `appHXwsSnX5TUGq0B` (Example Client)
**Table:** `tbl3Maf0bCgzFWeEP` (SRF)

| Airtable Field | Field ID | Canonical Field |
|---------------|----------|----------------|
| Client Full Name | fldzLO8MSId0kOeSe | lead_name |
| Call Date | fldDN39EnWeZhkcD7 | call_date / generated_date |
| Closer (linked) | fld6rWlY44e3vpasa / fldpYGjhUyxF1u7RP | closer |
| Setter (linked) | fld8zr5ae696GXReo / fld7Wjw7WDNMtTETf | setter |
| Call Outcome | fldwIkxqT0vGvqBdo | outcome |
| What Happened | fldbW67jGZi61QeGm | closer_notes |
| No Call Reason | fldyNvkNZkugMFWuk | no_show_reason |
| Program | fldqcxHUiMvhEzMLz | offer_tier |
| Lead Campaign | fldgrS6o3VE5uln7F | funnel_source |
| Ads? | fldVCGBGBU9r9scHE | is_paid |
| FU Call | fld5wXRse8dz0cThl | is_fu_call |
| Was A Call | fldc4dFfulnTDiXdB | is_actual_call |
| Cash Collected | fldGGIg8psGj8TKmc | cash_collected |
| Revenue | fldxsQG7MrV4ZI9w3 | revenue |
| Why did they buy | fldJau9qQ9xQd6zGv | why_bought |
| Client's main goal | fldC6FdDjyQAVf7S7 | main_goal |
| Client's main struggle | fldTeNJIjGS812YYR | main_struggle |
| Fathom URL | fldg6nVsxdphGdQ8f | fathom_url |
| UTM Source | fldk2tEzn3uwYEI1l | utm_source (linked to UTMs table) |
| UTM Medium | fldiSAW1F6GzOv5pd | utm_medium |
| UTM Campaign | fldqQF4IcYYrzXJy4 | utm_campaign (linked to UTMs table) |
| UTM Content | fldqtEWaaZ2nCmie9 | utm_content (linked to UTMs table) |
| Payment Plan | flduZU6KzRbXLyLZs | payment_plan |
| Payment Method | fldLmvw9hhm6V9See | payment_method |

**Outcome values:** Closed/Won, Deposit, Pitched No Close, Disqualified, No-Show, Cancelled, Rescheduled, Remainder Collection (no call)

**Program values:** Standard Program, DIY + DFY Niche, DIY Program (6-months), DIY Program (3-months), Consulting

**Lead Campaign values:** VSL Funnel, Webinar, DM Funnel, Free Community

**To pull via Airtable MCP:**
```
list_records_for_table(
  baseId="appHXwsSnX5TUGq0B",
  tableId="tbl3Maf0bCgzFWeEP",
  fieldIds=[all field IDs above],
  filters={date range on fldDN39EnWeZhkcD7}
)
```

---

## Adapter 6 — Slack Channel Parsing

### #booked-calls channel format
Bot name: `NEW CALL BOOKED [SDR]`

Parse these fields from the structured message:
```
Name: → lead_name
Email: → lead_email
Phone Number: → phone
Call Time: → generated_date
Budget: → budget_range
Closer: → closer
UTM Source: → utm_source
UTM Medium: → utm_medium (contains ad set name)
UTM Content: → utm_content (the ad creative identifier)
UTM Campaign: → utm_campaign
```

### #call-outcomes channel format

**Close messages** (contain "NEW CLOSE" emoji):
```
Lead Name: → lead_name
Lead Email: → lead_email
Closing Date: → close_date
Closer: → closer
Setter: → setter
Lead Source: → funnel_source
Program: → offer_tier
Cash Collected: → cash_collected (parse currency)
Revenue Generated: → revenue (parse currency)
What Happened on Call: → closer_notes
Client's Main Goal: → main_goal
```

**Outcome messages** (contain "CALL OUTCOME"):
```
Outcome: → outcome
Lead Name: → lead_name
Lead Email: → lead_email
Call Date: → call_date
Closer: → closer
Setter: → setter
Lead Source: → funnel_source
What Happened on Call: → closer_notes
Fathom link: → fathom_url
```

**No-call messages** (contain "NO CALL"):
```
Outcome: → outcome (No-Show / Cancelled / Rescheduled)
Reason/Next Steps: → no_show_reason
Lead Name: → lead_name
Lead Email: → lead_email
Call Date: → call_date
Closer: → closer
Setter: → setter
Lead Source: → funnel_source
```

**UTM follow-up messages** (contain "UTM Data for"):
```
Source: → utm_source
Campaign: → utm_campaign
Medium: → utm_medium
Content: → utm_content
```
Match to the lead by name (parsed from "UTM Data for [Name]:").

---

## Adapter 7 — Generic CSV (Manual Mapping)

For any CSV that doesn't match the above adapters, present the canonical field list and ask the user to map their columns:

```
Which column contains the lead's email address?
Which column contains the call/close date?
Which column contains the outcome (closed, DQ, no-show, etc.)?
Which column contains the ad creative identifier?
Which column contains the cash collected?
Which column contains the revenue/contract value?
Which column contains the closer name?
Which column contains the closer notes?
```

Build the mapping and proceed.
