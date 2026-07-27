#!/usr/bin/env python3
"""
Lead Quality Dashboard Generator

Takes normalised lead data (JSON) and produces an interactive HTML dashboard
with 3/7/14/30 day rolling views, ad creative performance, lead-level detail,
and SQIBNT scoring.

Usage:
    python build_dashboard.py --data leads.json --client "Client Name" --output dashboard.html
    python build_dashboard.py --data leads.json --meta-csv ads.csv --client "Client Name" --output dashboard.html
    python build_dashboard.py --update dashboard.html --data new_leads.json

Input format (leads.json):
    See canonical schema in SKILL.md. Array of lead objects.

Meta CSV (optional):
    Meta Ads Manager export. Used for spend/click data only.
"""

import json
import argparse
import os
from datetime import datetime, timedelta
from collections import defaultdict

def load_leads(path):
    with open(path, 'r') as f:
        return json.load(f)

def load_meta_csv(path):
    """Parse Meta Ads Manager CSV for spend data only."""
    import csv
    ads = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ads.append({
                'campaign': row.get('Campaign name', ''),
                'spend': float(row.get('Amount spent (USD)', 0) or 0),
                'impressions': int(row.get('Impressions', 0) or 0),
                'link_clicks': int(row.get('Link clicks', 0) or 0),
                'ctr': float(row.get('CTR (link click-through rate)', 0) or 0),
                'reach': int(row.get('Reach', 0) or 0),
                'frequency': float(row.get('Frequency', 0) or 0),
            })
    return ads

def parse_date(d):
    """Parse various date formats to datetime."""
    if not d:
        return None
    if isinstance(d, datetime):
        return d
    for fmt in ['%Y-%m-%d', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%dT%H:%M:%S',
                '%Y-%m-%dT%H:%M:%SZ UTC%z', '%m/%d/%Y', '%d/%m/%Y']:
        try:
            return datetime.strptime(d.split(' UTC')[0].split('T')[0], '%Y-%m-%d')
        except (ValueError, IndexError):
            continue
    return None

def calculate_metrics(leads, meta_ads, window_days, ref_date=None):
    """Calculate all funnel metrics for a given time window."""
    if ref_date is None:
        ref_date = datetime.now()

    window_start = ref_date - timedelta(days=window_days)

    # Filter leads by generated_date for "this period's leads"
    period_leads = [l for l in leads if parse_date(l.get('generated_date')) and
                    parse_date(l['generated_date']) >= window_start and
                    parse_date(l['generated_date']) <= ref_date and
                    not l.get('is_fu_call') and not l.get('is_recurring')]

    # Filter for cash collected in this period (by close_date)
    period_cash_leads = [l for l in leads if parse_date(l.get('close_date')) and
                         parse_date(l['close_date']) >= window_start and
                         parse_date(l['close_date']) <= ref_date]

    # Basic counts
    total_leads = len(period_leads)
    outcomes = defaultdict(int)
    for l in period_leads:
        outcomes[l.get('outcome', 'Unknown')] += 1

    closes = outcomes.get('Closed/Won', 0)
    deposits = outcomes.get('Deposit', 0)
    pitched_nc = outcomes.get('Pitched No Close', 0)
    dq = outcomes.get('Disqualified', 0)
    no_show = outcomes.get('No-Show', 0)
    cancelled = outcomes.get('Cancelled', 0)
    rescheduled = outcomes.get('Rescheduled', 0)

    held = closes + deposits + pitched_nc + dq  # calls that actually happened
    qualified = closes + deposits + pitched_nc  # calls that reached pitch stage

    # Revenue - THREE DISTINCT NUMBERS
    new_cash = sum(float(l.get('cash_collected', 0) or 0) for l in period_leads
                   if l.get('outcome') in ('Closed/Won', 'Deposit'))
    all_cash = sum(float(l.get('cash_collected', 0) or 0) for l in period_cash_leads)
    total_cash = sum(float(l.get('cash_collected', 0) or 0) for l in leads
                     if l.get('outcome') in ('Closed/Won', 'Deposit', 'Remainder Collection (no call)'))
    new_revenue = sum(float(l.get('revenue', 0) or 0) for l in period_leads
                      if l.get('outcome') in ('Closed/Won', 'Deposit'))

    # Spend from Meta
    total_spend = sum(a['spend'] for a in meta_ads) if meta_ads else 0
    total_clicks = sum(a['link_clicks'] for a in meta_ads) if meta_ads else 0
    total_impressions = sum(a['impressions'] for a in meta_ads) if meta_ads else 0

    # Rates
    show_rate = (held / total_leads * 100) if total_leads > 0 else 0
    qual_rate_held = (qualified / held * 100) if held > 0 else 0
    qual_rate_booked = (qualified / total_leads * 100) if total_leads > 0 else 0
    close_rate_qual = (closes / qualified * 100) if qualified > 0 else 0
    close_rate_held = (closes / held * 100) if held > 0 else 0
    cost_per_call = total_spend / total_leads if total_leads > 0 else 0
    cost_per_close = total_spend / closes if closes > 0 else 0
    new_cash_roas = new_cash / total_spend if total_spend > 0 else 0
    all_cash_roas = all_cash / total_spend if total_spend > 0 else 0
    revenue_roas = new_revenue / total_spend if total_spend > 0 else 0
    ctr = total_clicks / total_impressions * 100 if total_impressions > 0 else 0
    cpc = total_spend / total_clicks if total_clicks > 0 else 0

    # Sales cycle
    cycles = []
    for l in leads:
        gd = parse_date(l.get('generated_date'))
        cd = parse_date(l.get('close_date'))
        if gd and cd and l.get('outcome') == 'Closed/Won':
            cycles.append((cd - gd).days)
    avg_sales_cycle = sum(cycles) / len(cycles) if cycles else 0

    # PP completion
    pp_leads = [l for l in leads if l.get('payment_plan') and l.get('outcome') == 'Closed/Won']
    pp_cash = sum(float(l.get('cash_collected', 0) or 0) for l in pp_leads)
    pp_revenue = sum(float(l.get('revenue', 0) or 0) for l in pp_leads)
    pp_completion = (pp_cash / pp_revenue * 100) if pp_revenue > 0 else 0

    # Pipeline
    pipeline = outcomes.get('Pitched No Close', 0) + outcomes.get('Deposit', 0) + outcomes.get('Rescheduled', 0)
    bad_leads = dq + no_show + cancelled

    return {
        'window_days': window_days,
        'total_leads': total_leads,
        'closes': closes,
        'deposits': deposits,
        'pitched_nc': pitched_nc,
        'dq': dq,
        'no_show': no_show,
        'cancelled': cancelled,
        'rescheduled': rescheduled,
        'held': held,
        'qualified': qualified,
        'pipeline': pipeline,
        'bad_leads': bad_leads,
        'new_cash': round(new_cash, 2),
        'all_cash': round(all_cash, 2),
        'total_cash': round(total_cash, 2),
        'new_revenue': round(new_revenue, 2),
        'total_spend': round(total_spend, 2),
        'show_rate': round(show_rate, 1),
        'qual_rate_held': round(qual_rate_held, 1),
        'qual_rate_booked': round(qual_rate_booked, 1),
        'close_rate_qual': round(close_rate_qual, 1),
        'close_rate_held': round(close_rate_held, 1),
        'cost_per_call': round(cost_per_call, 2),
        'cost_per_close': round(cost_per_close, 2),
        'new_cash_roas': round(new_cash_roas, 2),
        'all_cash_roas': round(all_cash_roas, 2),
        'revenue_roas': round(revenue_roas, 2),
        'ctr': round(ctr, 2),
        'cpc': round(cpc, 2),
        'avg_sales_cycle': round(avg_sales_cycle, 1),
        'pp_completion': round(pp_completion, 1),
    }

def calculate_ad_metrics(leads, window_days, ref_date=None, spend_data=None):
    """Calculate per-ad-creative metrics. spend_data is a list of dicts with
    'creative' and 'spend' keys from the aggregated report — includes ads that
    had spend but generated zero leads (invisible in the leads data alone)."""
    if ref_date is None:
        ref_date = datetime.now()
    window_start = ref_date - timedelta(days=window_days)

    period_leads = [l for l in leads if parse_date(l.get('generated_date')) and
                    parse_date(l['generated_date']) >= window_start and
                    parse_date(l['generated_date']) <= ref_date and
                    not l.get('is_fu_call') and not l.get('is_recurring')]

    ads = defaultdict(lambda: {
        'leads': [], 'closes': 0, 'dq': 0, 'no_show': 0, 'pipeline': 0,
        'new_cash': 0, 'revenue': 0, 'lqs_scores': [], 'spend': 0
    })

    # Seed with spend-only ads from aggregated report so they appear even with 0 leads
    if spend_data:
        for sd in spend_data:
            creative = sd.get('creative', '')
            if creative and creative != 'Total':
                ads[creative]['spend'] = float(sd.get('spend', 0) or 0)

    for l in period_leads:
        creative = l.get('utm_content') or l.get('ad_set_name') or 'Unattributed'
        ads[creative]['leads'].append(l)
        outcome = l.get('outcome', '')
        if outcome == 'Closed/Won':
            ads[creative]['closes'] += 1
            ads[creative]['new_cash'] += float(l.get('cash_collected', 0) or 0)
            ads[creative]['revenue'] += float(l.get('revenue', 0) or 0)
        elif outcome == 'Disqualified':
            ads[creative]['dq'] += 1
        elif outcome == 'No-Show':
            ads[creative]['no_show'] += 1
        elif outcome in ('Deposit', 'Pitched No Close', 'Rescheduled'):
            ads[creative]['pipeline'] += 1

        lqs = l.get('lqs')
        if lqs is not None:
            ads[creative]['lqs_scores'].append(float(lqs))

        ads[creative]['spend'] += float(l.get('ad_spend_attributed', 0) or 0)

    result = []
    for creative, data in ads.items():
        lead_count = len(data['leads'])
        avg_lqs = sum(data['lqs_scores']) / len(data['lqs_scores']) if data['lqs_scores'] else None
        dream_pct = sum(1 for s in data['lqs_scores'] if s >= 4.0) / len(data['lqs_scores']) * 100 if data['lqs_scores'] else 0
        bad_pct = sum(1 for s in data['lqs_scores'] if s < 2.0) / len(data['lqs_scores']) * 100 if data['lqs_scores'] else 0
        held = sum(1 for l in data['leads'] if l.get('outcome') in ('Closed/Won', 'Deposit', 'Pitched No Close', 'Disqualified'))
        show_rate = (held / lead_count * 100) if lead_count > 0 else 0
        roas = data['new_cash'] / data['spend'] if data['spend'] > 0 else None

        # Action recommendation
        if lead_count == 0 and data['spend'] > 0:
            action = 'SPEND ONLY — NO LEADS'
        elif data['spend'] < 200 and data['spend'] > 0:
            action = 'EARLY DATA'
        elif roas is not None and roas >= 1.5 and (avg_lqs is None or avg_lqs >= 3.5):
            action = 'SCALE'
        elif roas is not None and roas >= 1.0:
            action = 'MONITOR'
        elif roas is not None and roas >= 0.7:
            action = 'WATCH'
        elif avg_lqs is not None and avg_lqs < 2.0:
            action = 'KILL'
        elif roas is not None and roas < 0.7:
            action = 'KILL'
        elif lead_count > 0 and data['spend'] == 0:
            action = 'ORGANIC / NO SPEND'
        else:
            action = 'MONITOR'

        result.append({
            'creative': creative,
            'spend': round(data['spend'], 2),
            'leads': lead_count,
            'closes': data['closes'],
            'new_cash': round(data['new_cash'], 2),
            'revenue': round(data['revenue'], 2),
            'roas': round(roas, 2) if roas is not None else None,
            'avg_lqs': round(avg_lqs, 1) if avg_lqs is not None else None,
            'dream_pct': round(dream_pct, 1),
            'bad_pct': round(bad_pct, 1),
            'show_rate': round(show_rate, 1),
            'dq': data['dq'],
            'no_show': data['no_show'],
            'pipeline': data['pipeline'],
            'action': action,
            'lead_details': [{
                'name': l.get('lead_name', ''),
                'generated': l.get('generated_date', ''),
                'closed': l.get('close_date', ''),
                'outcome': l.get('outcome', ''),
                'closer': l.get('closer', ''),
                's': l.get('sqibnt', {}).get('s'),
                'q': l.get('sqibnt', {}).get('q'),
                'i': l.get('sqibnt', {}).get('i'),
                'b': l.get('sqibnt', {}).get('b'),
                'n': l.get('sqibnt', {}).get('n'),
                't': l.get('sqibnt', {}).get('t'),
                'lqs': l.get('lqs'),
                'notes': (l.get('closer_notes', '') or '')[:200],
                'why_bought': l.get('why_bought', ''),
                'why_didnt_buy': l.get('why_didnt_buy', ''),
                'objection': l.get('primary_objection', ''),
            } for l in data['leads']]
        })

    result.sort(key=lambda x: x['new_cash'], reverse=True)
    return result

def calculate_closer_metrics(leads, window_days, ref_date=None):
    """Calculate per-closer performance metrics."""
    if ref_date is None:
        ref_date = datetime.now()
    window_start = ref_date - timedelta(days=window_days)

    period_leads = [l for l in leads if parse_date(l.get('generated_date')) and
                    parse_date(l['generated_date']) >= window_start and
                    parse_date(l['generated_date']) <= ref_date and
                    not l.get('is_fu_call') and not l.get('is_recurring')]

    closers = defaultdict(lambda: {'leads': 0, 'closes': 0, 'cash': 0, 'revenue': 0, 'lqs_scores': []})
    for l in period_leads:
        closer = l.get('closer', 'Unknown')
        closers[closer]['leads'] += 1
        if l.get('outcome') == 'Closed/Won':
            closers[closer]['closes'] += 1
            closers[closer]['cash'] += float(l.get('cash_collected', 0) or 0)
            closers[closer]['revenue'] += float(l.get('revenue', 0) or 0)
        lqs = l.get('lqs')
        if lqs is not None:
            closers[closer]['lqs_scores'].append(float(lqs))

    result = []
    for name, data in closers.items():
        avg_lqs = sum(data['lqs_scores']) / len(data['lqs_scores']) if data['lqs_scores'] else None
        close_rate = (data['closes'] / data['leads'] * 100) if data['leads'] > 0 else 0
        avg_deal = data['cash'] / data['closes'] if data['closes'] > 0 else 0
        result.append({
            'closer': name,
            'leads': data['leads'],
            'closes': data['closes'],
            'close_rate': round(close_rate, 1),
            'cash': round(data['cash'], 2),
            'revenue': round(data['revenue'], 2),
            'avg_deal': round(avg_deal, 2),
            'avg_lqs_received': round(avg_lqs, 1) if avg_lqs is not None else None,
        })
    result.sort(key=lambda x: x['cash'], reverse=True)
    return result

def detect_patterns(leads, ad_metrics, metrics, spend_only_ads=None):
    """
    Bottleneck-depth pattern detection.

    Follows the Theory of Constraints approach:
    1. Identify the primary funnel bottleneck (where leads are dropping off)
    2. Flag spend-only ads (burning budget with zero leads/calls)
    3. Per-creative diagnostics with dollar impact
    4. Objection and DQ pattern clustering
    5. Prioritised recommendations with owner tags and projected impact
    """
    patterns = []

    total_leads = len([l for l in leads if not l.get('is_fu_call') and not l.get('is_recurring')])
    total_spend = metrics.get('total_spend', 0)

    # ================================================================
    # 1. FUNNEL BOTTLENECK DIAGNOSIS
    # ================================================================

    # Show rate bottleneck
    show_rate = metrics.get('show_rate', 0)
    no_shows = sum(1 for l in leads if l.get('outcome') == 'No-Show' and not l.get('is_fu_call'))
    if total_leads > 5 and show_rate < 60:
        cost_per_call = metrics.get('cost_per_call', 0)
        wasted_spend = no_shows * cost_per_call if cost_per_call else 0
        extra_calls_10pct = round(total_leads * 0.10)
        patterns.append({
            'type': 'danger',
            'title': f"PRIMARY BOTTLENECK: Show rate is {show_rate}% ({no_shows} no-shows of {total_leads} booked)",
            'detail': f"At ${cost_per_call:,.0f} cost per booked call, {no_shows} no-shows represent ~${wasted_spend:,.0f} in wasted ad spend. "
                      f"A 10% show rate improvement would yield ~{extra_calls_10pct} additional held calls. "
                      f"At current close rate ({metrics.get('close_rate_held', 0)}%), that's ~{max(1, round(extra_calls_10pct * metrics.get('close_rate_held', 0) / 100))} additional closes. "
                      f"Fix: Implement pre-call confirmation sequence (SMS + email 24hr and 1hr before). Add GC participation gate — non-responders predict no-shows.",
            'owner': 'Setter SOP — Priority 1'
        })
    elif total_leads > 5 and show_rate < 70:
        patterns.append({
            'type': 'warning',
            'title': f"Show rate is {show_rate}% — room for improvement",
            'detail': f"{no_shows} no-shows out of {total_leads} booked calls. Benchmark: 65-75% for VSL funnels, 25-35% for webinars.",
            'owner': 'Setter SOP'
        })

    # Close rate bottleneck
    close_rate = metrics.get('close_rate_qual', 0)
    qualified = metrics.get('qualified', 0)
    closes = metrics.get('closes', 0)
    if qualified > 5 and close_rate < 10:
        missed_rev = (qualified - closes) * (metrics.get('new_cash', 0) / max(closes, 1))
        patterns.append({
            'type': 'danger',
            'title': f"Close rate is {close_rate}% on {qualified} qualified calls — below 15% benchmark",
            'detail': f"{qualified} qualified calls produced only {closes} closes. Pipeline value from pitched-no-close: "
                      f"~${missed_rev:,.0f} if 20% converted on follow-up. "
                      f"Investigate: Is this a closer skill issue, lead quality issue, or offer-market fit issue? "
                      f"Check SQIBNT scores — if avg Intent (I) is high but Budget (B) is low, the problem is financial qualification, not selling.",
            'owner': 'Closer / Sales Manager'
        })

    # ================================================================
    # 2. SPEND-ONLY ADS (burning budget, zero leads)
    # ================================================================

    if spend_only_ads:
        total_wasted = sum(a.get('spend', 0) for a in spend_only_ads)
        if total_wasted > 0:
            ad_list = ', '.join(f"{a['creative'][:40]} (${a['spend']:,.0f})" for a in spend_only_ads[:5])
            remaining = len(spend_only_ads) - 5 if len(spend_only_ads) > 5 else 0
            patterns.append({
                'type': 'danger',
                'title': f"${total_wasted:,.0f} spent on {len(spend_only_ads)} ads with ZERO leads booked",
                'detail': f"These ads had spend but generated no calls or conversions in this period: {ad_list}"
                          + (f" + {remaining} more" if remaining else "")
                          + f". Review hooks and CTAs — spend without leads means clicks are not converting to bookings, or the ads are not generating clicks at all.",
                'owner': 'Media Buyer — Kill or revise immediately'
            })

    # ================================================================
    # 3. PER-CREATIVE DIAGNOSTICS
    # ================================================================

    # High volume, zero closes (Ad#51 pattern)
    volume_no_close = [a for a in ad_metrics if a['leads'] >= 5 and a['closes'] == 0 and a['spend'] > 200]
    for ad in sorted(volume_no_close, key=lambda x: x['leads'], reverse=True)[:3]:
        qual_count = sum(1 for l in ad.get('lead_details', []) if l.get('outcome') in ('Pitched No Close', 'Deposit'))
        qual_rate = round(qual_count / ad['leads'] * 100) if ad['leads'] > 0 else 0
        patterns.append({
            'type': 'warning',
            'title': f"INVESTIGATE: {ad['creative'][:50]} — {ad['leads']} leads, ${ad['spend']:,.0f} spend, 0 closes",
            'detail': f"High volume but no conversions. {qual_count} qualified calls ({qual_rate}% qual rate), "
                      f"{ad['no_show']} no-shows, {ad['dq']} DQs. "
                      + (f"Qualify rate of {qual_rate}% is {'strong' if qual_rate > 50 else 'weak'} — "
                         + ("the ad is bringing quality leads that aren't closing. Review Fathom recordings for pitched-NC calls to find the pattern." if qual_rate > 50
                            else "the ad is attracting low-intent leads. Test a qualifying hook variant with friction to filter."))
                      + f" Pipeline value: {ad['pipeline']} leads still active.",
            'owner': 'Media Buyer + Closer Review'
        })

    # Top performer to scale
    scalable = sorted([a for a in ad_metrics if a['closes'] > 0 and a['roas'] is not None and a['roas'] >= 1.0],
                      key=lambda x: x['new_cash'], reverse=True)
    if scalable:
        top = scalable[0]
        patterns.append({
            'type': 'success',
            'title': f"SCALE: {top['creative'][:50]} — {top['roas']}x ROAS, {top['closes']} closes, ${top['new_cash']:,.0f}",
            'detail': f"Best performing creative. {top['leads']} leads, {top['show_rate']}% show rate"
                      + (f", avg LQS {top['avg_lqs']}" if top['avg_lqs'] else "")
                      + f". Action: Increase budget 15-20% over 3 days. Duplicate to new audience. Begin iterating hooks (3 variations) and images (2 variations).",
            'owner': 'Media Buyer'
        })

    # Ads with good pipeline but no close yet (patience signal)
    pipeline_ads = [a for a in ad_metrics if a['pipeline'] >= 3 and a['closes'] == 0 and a['spend'] > 200]
    for ad in pipeline_ads[:2]:
        patterns.append({
            'type': 'info',
            'title': f"PIPELINE: {ad['creative'][:50]} — {ad['pipeline']} leads in follow-up, 0 closes yet",
            'detail': f"${ad['spend']:,.0f} spent with {ad['pipeline']} leads still in pipeline. Don't kill based on zero closes alone — "
                      f"revisit in 7 days. If pipeline converts at 20%, that's ~{max(1, round(ad['pipeline'] * 0.20))} close(s).",
            'owner': 'Media Buyer — Hold'
        })

    # ================================================================
    # 4. OBJECTION & DQ PATTERN CLUSTERING
    # ================================================================

    # Financial DQ
    fin_leads = [l for l in leads if l.get('primary_objection') == 'Financial' or
                 (l.get('closer_notes') and any(kw in (l['closer_notes'] or '').lower()
                  for kw in ['budget', 'afford', 'money', 'financial', 'under 1k', 'under $1k', 'limited funds',
                             'can\'t invest', 'liquid', 'paycheck', 'tax return']))]
    if len(fin_leads) >= 3:
        fin_creatives = defaultdict(int)
        for l in fin_leads:
            c = l.get('utm_content') or l.get('ad_set_name') or 'Unknown'
            fin_creatives[c] += 1
        top_fin = sorted(fin_creatives.items(), key=lambda x: x[1], reverse=True)[:3]
        creative_list = ', '.join(f"{c[:30]} ({n})" for c, n in top_fin)
        patterns.append({
            'type': 'warning',
            'title': f"Financial DQ cluster: {len(fin_leads)} leads with budget objections",
            'detail': f"Leads are getting to calls without adequate budget. Top creatives producing these: {creative_list}. "
                      f"Each financial DQ wastes a closer's call slot (~${metrics.get('cost_per_call', 0):,.0f} in ad spend + closer time). "
                      f"Fix: Add pre-call financial qualifier ('Do you have access to at least $X to invest?') to booking form.",
            'owner': 'Setter SOP'
        })

    # Timing/not ready objection
    timing_leads = [l for l in leads if l.get('primary_objection') == 'Timing' or
                    (l.get('closer_notes') and any(kw in (l['closer_notes'] or '').lower()
                     for kw in ['not ready', 'timing', 'next month', 'summer', 'later', 'after', 'waiting']))]
    if len(timing_leads) >= 3:
        patterns.append({
            'type': 'info',
            'title': f"Timing stall: {len(timing_leads)} leads want to buy but aren't ready now",
            'detail': f"These leads have intent but timing is wrong. They need a structured re-engagement sequence: "
                      f"warm check-in at agreed time + social proof drop + soft re-open. Do not hard close. "
                      f"Track conversion rate of timing-stall leads at 14 and 30 days.",
            'owner': 'Closer / CRM'
        })

    # Trust/scepticism
    trust_leads = [l for l in leads if l.get('primary_objection') == 'Trust' or
                   (l.get('closer_notes') and any(kw in (l['closer_notes'] or '').lower()
                    for kw in ['trust', 'scam', 'skeptic', 'sceptic', 'don\'t trust', 'suspicious', 'spam']))]
    if len(trust_leads) >= 2:
        patterns.append({
            'type': 'warning',
            'title': f"Trust objection: {len(trust_leads)} leads with trust/scepticism issues",
            'detail': f"Leads are arriving with trust barriers. Check: Is the pre-call content building enough credibility? "
                      f"Are multi-number outreach attempts triggering spam concerns? Is recording disclosure clear in pre-call materials?",
            'owner': 'Content / Setter SOP'
        })

    # No-show clustering by creative
    no_show_leads = [l for l in leads if l.get('outcome') == 'No-Show' and not l.get('is_fu_call')]
    if len(no_show_leads) >= 3:
        ns_creatives = defaultdict(int)
        for l in no_show_leads:
            c = l.get('utm_content') or l.get('ad_set_name') or 'Unknown'
            ns_creatives[c] += 1
        top_ns = sorted(ns_creatives.items(), key=lambda x: x[1], reverse=True)[:3]
        worst = top_ns[0]
        worst_total = sum(1 for l in leads if (l.get('utm_content') or l.get('ad_set_name') or 'Unknown') == worst[0]
                         and not l.get('is_fu_call') and not l.get('is_recurring'))
        worst_rate = round(worst[1] / worst_total * 100) if worst_total > 0 else 0
        patterns.append({
            'type': 'warning',
            'title': f"No-show concentration: {worst[0][:40]} has {worst[1]} no-shows ({worst_rate}% of its leads)",
            'detail': f"This creative is attracting leads who don't show up. Possible causes: "
                      f"low-intent hook (curiosity click, no buying intent), same-day bookers with zero nurture time, "
                      f"or pre-call messaging not setting expectations. "
                      f"Action: Review the hook — does it attract buyers or browsers?",
            'owner': 'Media Buyer'
        })

    # ================================================================
    # 5. CREATIVE GAP ANALYSIS
    # ================================================================

    if ad_metrics:
        performing = [a for a in ad_metrics if a['closes'] > 0 and (a['roas'] or 0) >= 1.0]
        underperforming = [a for a in ad_metrics if a['leads'] >= 3 and a['closes'] == 0]
        total_creatives = len(ad_metrics)
        hit_rate = round(len(performing) / total_creatives * 100) if total_creatives > 0 else 0

        patterns.append({
            'type': 'info',
            'title': f"Creative hit rate: {len(performing)}/{total_creatives} ads producing closes ({hit_rate}%)",
            'detail': f"Performing: {len(performing)} ads with confirmed closes. "
                      f"Underperforming: {len(underperforming)} ads with 3+ leads and 0 closes. "
                      f"Next batch priority: Iterate hooks on top {min(3, len(performing))} performers (80% of new ads). "
                      f"Test 1-2 completely new concepts (20% of new ads).",
            'owner': 'Media Buyer / Creative'
        })

    return patterns

def generate_html(client_name, leads, metrics_by_window, ad_metrics_by_window,
                  closer_metrics, patterns, ref_date_str):
    """Generate the full interactive HTML dashboard."""

    dashboard_data = {
        'client': client_name,
        'generated': ref_date_str,
        'leads': [{k: v for k, v in l.items() if k != 'call_summary'} for l in leads],
        'metrics': metrics_by_window,
        'ad_metrics': ad_metrics_by_window,
        'closer_metrics': closer_metrics,
        'patterns': patterns,
    }

    data_json = json.dumps(dashboard_data, default=str, indent=None)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{client_name} — Lead Quality Dashboard</title>
<style>
:root {{
  --navy: #1a3a2a;
  --navy-light: #234d38;
  --navy-mid: #2d5f46;
  --slate: #475569;
  --slate-light: #94a3b8;
  --border: #e2e8f0;
  --bg: #f8fafc;
  --surface: #ffffff;
  --green: #16a34a;
  --green-bg: #f0fdf4;
  --green-border: #bbf7d0;
  --blue: #2563eb;
  --blue-bg: #eff6ff;
  --blue-border: #bfdbfe;
  --amber: #d97706;
  --amber-bg: #fffbeb;
  --amber-border: #fde68a;
  --red: #dc2626;
  --red-bg: #fef2f2;
  --red-border: #fecaca;
  --grey: #64748b;
  --grey-bg: #f1f5f9;
  --radius: 8px;
  --shadow: 0 1px 3px rgba(0,0,0,.06), 0 1px 2px rgba(0,0,0,.04);
  --shadow-md: 0 4px 6px rgba(0,0,0,.05), 0 2px 4px rgba(0,0,0,.03);
}}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--navy); font-size: 14px; line-height: 1.5; -webkit-font-smoothing: antialiased; }}
.wrap {{ max-width: 1440px; margin: 0 auto; padding: 24px 32px; }}

/* ── HEADER ── */
.hdr {{ background: var(--navy); color: #fff; padding: 28px 36px; border-radius: var(--radius); margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; }}
.hdr-left h1 {{ font-size: 22px; font-weight: 700; letter-spacing: -0.3px; }}
.hdr-left p {{ font-size: 13px; color: var(--slate-light); margin-top: 4px; }}
.hdr-right {{ display: flex; gap: 6px; }}
.wbtn {{ padding: 7px 14px; border: 1.5px solid rgba(255,255,255,.2); border-radius: 6px; background: transparent; color: rgba(255,255,255,.7); cursor: pointer; font-weight: 600; font-size: 13px; transition: all .15s; font-family: inherit; }}
.wbtn:hover {{ border-color: rgba(255,255,255,.5); color: #fff; }}
.wbtn.on {{ background: #fff; color: var(--navy); border-color: #fff; }}

/* ── METRIC CARDS ── */
.cards {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 14px; margin-bottom: 24px; }}
@media (max-width: 1200px) {{ .cards {{ grid-template-columns: repeat(3, 1fr); }} }}
.kcard {{ background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 18px 20px; }}
.kcard .kl {{ font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: .6px; color: var(--slate-light); }}
.kcard .kv {{ font-size: 26px; font-weight: 800; margin-top: 6px; letter-spacing: -0.5px; color: var(--navy); }}
.kcard .kv.pos {{ color: var(--green); }}
.kcard .kv.neg {{ color: var(--red); }}
.kcard .kv.warn {{ color: var(--amber); }}

/* ── SECTION PANELS ── */
.panel {{ background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); margin-bottom: 24px; overflow: hidden; }}
.panel-hdr {{ background: var(--navy); color: #fff; padding: 14px 24px; font-size: 15px; font-weight: 700; letter-spacing: -0.2px; display: flex; justify-content: space-between; align-items: center; }}
.panel-hdr .sub {{ font-size: 12px; font-weight: 400; color: var(--slate-light); }}

/* ── TABLES ── */
table {{ width: 100%; border-collapse: collapse; }}
thead th {{ padding: 10px 14px; text-align: left; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .5px; color: var(--slate); background: var(--bg); border-bottom: 2px solid var(--border); cursor: pointer; white-space: nowrap; user-select: none; }}
thead th:hover {{ color: var(--navy); }}
tbody td {{ padding: 11px 14px; border-bottom: 1px solid var(--border); font-size: 13px; vertical-align: middle; }}
tbody tr:last-child td {{ border-bottom: none; }}
tbody tr:hover {{ background: #f1f5f9; }}

/* ── PILLS ── */
.p {{ display: inline-block; padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 700; letter-spacing: .2px; white-space: nowrap; }}
.p-scale {{ background: var(--green-bg); color: var(--green); border: 1px solid var(--green-border); }}
.p-monitor {{ background: var(--blue-bg); color: var(--blue); border: 1px solid var(--blue-border); }}
.p-watch {{ background: var(--amber-bg); color: var(--amber); border: 1px solid var(--amber-border); }}
.p-kill {{ background: var(--red-bg); color: var(--red); border: 1px solid var(--red-border); }}
.p-early {{ background: var(--grey-bg); color: var(--grey); border: 1px solid var(--border); }}
.p-spend {{ background: var(--navy); color: #fff; border: 1px solid var(--navy); }}
.p-closed {{ background: var(--green-bg); color: var(--green); border: 1px solid var(--green-border); }}
.p-pipeline {{ background: var(--amber-bg); color: var(--amber); border: 1px solid var(--amber-border); }}
.p-bad {{ background: var(--red-bg); color: var(--red); border: 1px solid var(--red-border); }}
.p-noshow {{ background: var(--grey-bg); color: var(--grey); border: 1px solid var(--border); }}

/* ── LQS COLOURS ── */
.q-dream {{ color: var(--green); font-weight: 700; }}
.q-qual {{ color: var(--blue); font-weight: 700; }}
.q-marg {{ color: var(--amber); font-weight: 700; }}
.q-bad {{ color: var(--red); font-weight: 700; }}

/* ── EXPANDABLE DETAIL ── */
.xrow {{ display: none; }}
.xrow.open {{ display: table-row; }}
.xwrap {{ padding: 16px 24px; background: var(--bg); }}
.dtable {{ width: 100%; font-size: 12px; }}
.dtable th {{ background: var(--navy-light); color: #fff; font-size: 10px; padding: 8px 10px; text-transform: uppercase; letter-spacing: .5px; }}
.dtable td {{ padding: 7px 10px; font-size: 12px; border-bottom: 1px solid var(--border); }}
.dtable tr:last-child td {{ border-bottom: none; }}
.notes-cell {{ max-width: 260px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: var(--slate); font-size: 12px; }}
.notes-cell:hover {{ white-space: normal; overflow: visible; background: #fff; position: relative; z-index: 2; box-shadow: var(--shadow-md); border-radius: 4px; padding: 8px; }}

/* ── CLICKABLE ROWS ── */
.clik {{ cursor: pointer; transition: background .1s; }}
.clik:hover {{ background: var(--blue-bg) !important; }}
.clik td:first-child {{ position: relative; padding-left: 28px; }}
.clik td:first-child::before {{ content: ''; position: absolute; left: 12px; top: 50%; transform: translateY(-50%); width: 0; height: 0; border-left: 5px solid var(--slate-light); border-top: 4px solid transparent; border-bottom: 4px solid transparent; transition: transform .15s; }}
.clik.expanded td:first-child::before {{ transform: translateY(-50%) rotate(90deg); }}

/* ── PATTERN CARDS ── */
.pcard {{ padding: 16px 20px; border-radius: var(--radius); margin-bottom: 10px; border: 1px solid; }}
.pcard-success {{ background: var(--green-bg); border-color: var(--green-border); }}
.pcard-warning {{ background: var(--amber-bg); border-color: var(--amber-border); }}
.pcard-danger {{ background: var(--red-bg); border-color: var(--red-border); }}
.pcard-info {{ background: var(--blue-bg); border-color: var(--blue-border); }}
.pcard .pt {{ font-weight: 700; font-size: 14px; color: var(--navy); }}
.pcard .pd {{ font-size: 13px; color: var(--slate); margin-top: 6px; line-height: 1.6; }}
.pcard .po {{ display: inline-block; margin-top: 8px; padding: 3px 10px; background: var(--navy); color: #fff; border-radius: 4px; font-size: 11px; font-weight: 600; }}

/* ── CLOSER TABLE ── */
.mono {{ font-variant-numeric: tabular-nums; }}

/* ── RESPONSIVE ── */
@media (max-width: 900px) {{
  .wrap {{ padding: 12px 16px; }}
  .hdr {{ flex-direction: column; gap: 12px; align-items: flex-start; }}
  .cards {{ grid-template-columns: repeat(2, 1fr); }}
  table {{ font-size: 12px; }}
}}
</style>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
<div class="wrap">

<div class="hdr">
  <div class="hdr-left">
    <h1>{client_name}</h1>
    <p>Lead Quality Dashboard &middot; Generated {ref_date_str}</p>
  </div>
  <div class="hdr-right">
    <button class="wbtn" onclick="sw(3)" data-w="3">3D</button>
    <button class="wbtn" onclick="sw(7)" data-w="7">7D</button>
    <button class="wbtn on" onclick="sw(14)" data-w="14">14D</button>
    <button class="wbtn" onclick="sw(30)" data-w="30">30D</button>
  </div>
</div>

<div class="cards" id="cards"></div>

<div class="panel">
  <div class="panel-hdr">Ad Creative Performance <span class="sub">Click any row to expand lead detail</span></div>
  <div style="overflow-x:auto;">
  <table id="adTbl">
    <thead><tr>
      <th onclick="ss('creative')">Ad Creative</th>
      <th onclick="ss('leads')">Leads</th>
      <th onclick="ss('closes')">Closes</th>
      <th onclick="ss('new_cash')">Cash</th>
      <th onclick="ss('show_rate')">Show%</th>
      <th onclick="ss('close_rate')">Close%</th>
      <th>Pitched NC</th>
      <th>DQ</th>
      <th>No-Show</th>
      <th onclick="ss('avg_lqs')">LQS</th>
      <th>Action</th>
    </tr></thead>
    <tbody id="adBody"></tbody>
  </table>
  </div>
</div>

<div class="panel">
  <div class="panel-hdr">Closer Performance</div>
  <div style="overflow-x:auto;">
  <table>
    <thead><tr>
      <th>Closer</th><th>Leads</th><th>Closes</th><th>Close%</th><th>Cash</th><th>Revenue</th><th>Avg Deal</th><th>LQS Recv</th>
    </tr></thead>
    <tbody id="clBody"></tbody>
  </table>
  </div>
</div>

<div class="panel">
  <div class="panel-hdr">Patterns & Recommended Actions</div>
  <div id="patBox" style="padding:16px 20px;"></div>
</div>

</div>

<script>
const D={data_json};
let W=14, S={{c:'new_cash',d:'desc'}};

const $=x=>document.getElementById(x);
const fm=(n,p)=>{{if(n==null)return'-';if(p==='$')return'$'+Number(n).toLocaleString('en-US',{{maximumFractionDigits:0}});if(typeof n==='number'&&n%1!==0)return n.toFixed(1);return''+n;}};
const qc=s=>{{if(!s)return'';return s>=4?'q-dream':s>=3?'q-qual':s>=2?'q-marg':'q-bad';}};
const ap=a=>{{const m={{'SCALE':'p-scale','MONITOR':'p-monitor','WATCH':'p-watch','KILL':'p-kill','EARLY DATA':'p-early','SPEND ONLY — NO LEADS':'p-spend','ORGANIC / NO SPEND':'p-early','INVESTIGATE':'p-watch'}};return`<span class="p ${{m[a]||'p-early'}}">${{a}}</span>`;}};
const op=o=>{{const m={{'Closed/Won':'p-closed','Deposit':'p-pipeline','Pitched No Close':'p-pipeline','Disqualified':'p-bad','No-Show':'p-noshow','Cancelled':'p-noshow','Rescheduled':'p-pipeline','Remainder Collection (no call)':'p-pipeline'}};return`<span class="p ${{m[o]||'p-early'}}">${{o}}</span>`;}};
const sc=v=>{{if(!v)return'<td style="text-align:center;color:var(--slate-light)">-</td>';return`<td style="text-align:center" class="${{qc(v)}}">${{v}}</td>`;}};

function sw(d){{W=d;document.querySelectorAll('.wbtn').forEach(b=>b.classList.remove('on'));document.querySelector(`[data-w="${{d}}"]`).classList.add('on');R();}}
function ss(c){{S.c===c?S.d=S.d==='desc'?'asc':'desc':S={{c,d:'desc'}};R();}}
function tgl(i){{const r=$('xr-'+i),tr=$('ar-'+i);if(r){{r.classList.toggle('open');tr.classList.toggle('expanded');}}}}

function R(){{
  const m=D.metrics[W], ads=D.ad_metrics[W]||[], cls=D.closer_metrics||[], pats=D.patterns||[];

  // Cards
  const kv=(l,v,c)=>`<div class="kcard"><div class="kl">${{l}}</div><div class="kv ${{c||''}}">${{v}}</div></div>`;
  $('cards').innerHTML=[
    kv('New Cash (Period Leads)',fm(m.new_cash,'$')),
    kv('All Cash (This Period)',fm(m.all_cash,'$')),
    kv('Closes',m.closes),
    kv('Bad / DQ',m.bad_leads, m.bad_leads>5?'neg':''),
    kv('Pipeline',m.pipeline),
    kv('Show Rate',m.show_rate+'%', m.show_rate>=60?'pos':m.show_rate<50?'neg':'warn'),
    kv('Close Rate (Qual)',m.close_rate_qual+'%', m.close_rate_qual>=15?'pos':m.close_rate_qual<10?'neg':''),
    kv('Cost / Close',fm(m.cost_per_close,'$')),
    kv('New Cash ROAS',m.new_cash_roas+'x', m.new_cash_roas>=1.5?'pos':m.new_cash_roas<1?'neg':'warn'),
    kv('Avg Sales Cycle',m.avg_sales_cycle+'d'),
  ].join('');

  // Ad table
  let sa=[...ads];
  sa.sort((a,b)=>{{let va=a[S.c],vb=b[S.c];if(va==null)va=-1e9;if(vb==null)vb=-1e9;return S.d==='desc'?vb-va:va-vb;}});

  $('adBody').innerHTML=sa.map((a,i)=>{{
    const held=a.leads>0?a.leads-(a.no_show||0)-(sa.filter?0:0):0;
    const pitched_nc=(a.lead_details||[]).filter(l=>l.outcome==='Pitched No Close').length;
    const cr=held>0?((a.closes/held)*100).toFixed(1)+'%':'-';

    const det=(a.lead_details||[]).map(l=>`
      <tr>
        <td style="font-weight:500">${{l.name}}</td>
        <td class="mono">${{l.generated?l.generated.split('T')[0]:'-'}}</td>
        <td class="mono">${{l.closed?l.closed.split('T')[0]:'-'}}</td>
        <td>${{op(l.outcome)}}</td>
        <td>${{l.closer||'-'}}</td>
        ${{sc(l.s)}}${{sc(l.q)}}${{sc(l.i)}}${{sc(l.b)}}${{sc(l.n)}}${{sc(l.t)}}
        <td class="${{qc(l.lqs)}}" style="text-align:center">${{l.lqs||'-'}}</td>
        <td class="notes-cell" title="${{(l.notes||'').replace(/"/g,'&quot;')}}">${{l.notes||'-'}}</td>
      </tr>`).join('');

    return`
      <tr class="clik" id="ar-${{i}}" onclick="tgl(${{i}})">
        <td style="max-width:280px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:500" title="${{a.creative}}">${{a.creative.length>55?a.creative.substring(0,55)+'...':a.creative}}</td>
        <td class="mono">${{a.leads}}</td>
        <td class="mono" style="font-weight:700;${{a.closes>0?'color:var(--green)':''}}">${{a.closes}}</td>
        <td class="mono" style="font-weight:600">${{fm(a.new_cash,'$')}}</td>
        <td class="mono">${{a.show_rate}}%</td>
        <td class="mono">${{cr}}</td>
        <td class="mono">${{pitched_nc}}</td>
        <td class="mono" style="${{a.dq>0?'color:var(--red);font-weight:600':''}}">${{a.dq}}</td>
        <td class="mono" style="${{a.no_show>2?'color:var(--red);font-weight:600':''}}">${{a.no_show}}</td>
        <td class="${{qc(a.avg_lqs)}}">${{a.avg_lqs||'-'}}</td>
        <td>${{ap(a.action)}}</td>
      </tr>
      <tr class="xrow" id="xr-${{i}}">
        <td colspan="11">
          <div class="xwrap">
            <table class="dtable">
              <thead><tr><th>Lead</th><th>Generated</th><th>Closed</th><th>Outcome</th><th>Closer</th><th>S</th><th>Q</th><th>I</th><th>B</th><th>N</th><th>T</th><th>LQS</th><th>Notes</th></tr></thead>
              <tbody>${{det}}</tbody>
            </table>
          </div>
        </td>
      </tr>`;
  }}).join('');

  // Closer table
  $('clBody').innerHTML=cls.map(c=>`
    <tr>
      <td style="font-weight:600">${{c.closer}}</td>
      <td class="mono">${{c.leads}}</td>
      <td class="mono" style="font-weight:700;${{c.closes>0?'color:var(--green)':''}}">${{c.closes}}</td>
      <td class="mono">${{c.close_rate}}%</td>
      <td class="mono">${{fm(c.cash,'$')}}</td>
      <td class="mono">${{fm(c.revenue,'$')}}</td>
      <td class="mono">${{fm(c.avg_deal,'$')}}</td>
      <td class="${{qc(c.avg_lqs_received)}}">${{c.avg_lqs_received||'-'}}</td>
    </tr>`).join('');

  // Patterns
  $('patBox').innerHTML=pats.map(p=>`
    <div class="pcard pcard-${{p.type}}">
      <div class="pt">${{p.title}}</div>
      <div class="pd">${{p.detail}}</div>
      <span class="po">${{p.owner}}</span>
    </div>`).join('');
}}

R();
</script>
</body>
</html>"""

    return html


def main():
    parser = argparse.ArgumentParser(description='Build Lead Quality Dashboard')
    parser.add_argument('--data', required=True, help='Path to normalised leads JSON')
    parser.add_argument('--meta-csv', help='Path to Meta Ads Manager CSV (for spend data)')
    parser.add_argument('--client', required=True, help='Client name')
    parser.add_argument('--output', required=True, help='Output HTML file path')
    parser.add_argument('--ref-date', help='Reference date (YYYY-MM-DD). Defaults to today.')
    parser.add_argument('--update', help='Path to existing dashboard to update (merge data)')
    args = parser.parse_args()

    # Load data
    leads = load_leads(args.data)
    meta_ads = load_meta_csv(args.meta_csv) if args.meta_csv else []
    ref_date = datetime.strptime(args.ref_date, '%Y-%m-%d') if args.ref_date else datetime.now()
    ref_date_str = ref_date.strftime('%Y-%m-%d')

    # If updating, merge with existing data
    if args.update and os.path.exists(args.update):
        with open(args.update, 'r') as f:
            html = f.read()
        # Extract existing JSON data
        start = html.find('const DATA = ') + len('const DATA = ')
        end = html.find(';\n\nlet currentWindow')
        if start > 0 and end > 0:
            existing_data = json.loads(html[start:end])
            existing_leads = existing_data.get('leads', [])
            # Merge by email (dedup)
            existing_emails = {l['lead_email'] for l in existing_leads if l.get('lead_email')}
            new_leads = [l for l in leads if l.get('lead_email') not in existing_emails]
            leads = existing_leads + new_leads
            print(f"Merged: {len(existing_leads)} existing + {len(new_leads)} new = {len(leads)} total leads")

    # Parse spend data from aggregated report if provided
    spend_data = None
    if args.meta_csv:
        # Check if this is a Cortana aggregated report (has 'ROAS' column) or Meta export
        import csv
        with open(args.meta_csv, 'r') as f:
            reader = csv.DictReader(f)
            first = next(reader, {})
            if 'ROAS' in first:  # Cortana aggregated report
                f.seek(0)
                reader = csv.DictReader(f)
                spend_data = [{'creative': r.get('Name', ''), 'spend': float(r.get('Cost', 0) or 0)}
                              for r in reader if r.get('Name') != 'Total']

    # Calculate metrics for all windows
    metrics_by_window = {}
    ad_metrics_by_window = {}
    for window in [3, 7, 14, 30]:
        metrics_by_window[str(window)] = calculate_metrics(leads, meta_ads, window, ref_date)
        ad_metrics_by_window[str(window)] = calculate_ad_metrics(leads, window, ref_date, spend_data)

    closer_metrics = calculate_closer_metrics(leads, 30, ref_date)

    # Identify spend-only ads (had spend but zero leads in the period)
    spend_only_ads = [a for a in ad_metrics_by_window.get('30', [])
                      if a['leads'] == 0 and a['spend'] > 0]

    # Detect patterns (use 14-day window as default)
    patterns = detect_patterns(leads, ad_metrics_by_window['14'],
                               metrics_by_window['14'], spend_only_ads)

    # Generate HTML
    html = generate_html(args.client, leads, metrics_by_window, ad_metrics_by_window,
                        closer_metrics, patterns, ref_date_str)

    # Write output
    with open(args.output, 'w') as f:
        f.write(html)

    print(f"Dashboard generated: {args.output}")
    print(f"Total leads: {len(leads)}")
    print(f"14-day metrics: {metrics_by_window['14']['closes']} closes, ${metrics_by_window['14']['new_cash']:,.0f} new cash")

if __name__ == '__main__':
    main()
