"""
generate_data.py
Generates all synthetic data files for the data-storytelling-workshop.
Run from repo root: python scripts/generate_data.py

Intentional data quality issues are pedagogical, not bugs.
"""

import csv
import json
import random
import os
from datetime import date, timedelta

random.seed(42)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COFFEE_DIR = os.path.join(ROOT, "data", "coffee-shops")
JOB_DIR = os.path.join(ROOT, "data", "job-market")


# ─── Helpers ────────────────────────────────────────────────────────────────

def jitter(base, pct=0.15):
    return round(base * (1 + random.uniform(-pct, pct)), 2)

def date_str(d, fmt="iso"):
    """Return date as ISO (YYYY-MM-DD) or US (MM/DD/YYYY) format."""
    if fmt == "iso":
        return d.strftime("%Y-%m-%d")
    return d.strftime("%m/%d/%Y")

def write_csv(path, rows, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"  Wrote {len(rows)} rows -> {os.path.relpath(path, ROOT)}")


# ─── Coffee shops metadata ───────────────────────────────────────────────────

# Shop names with INTENTIONAL INCONSISTENCY across files
SHOPS = [
    {"id": "S1", "canonical": "HUB Coffee",        "aliases": ["HUB Coffee", "The HUB", "hub-coffee", "HUB"]},
    {"id": "S2", "canonical": "Odegaard Cafe",      "aliases": ["Odegaard Cafe", "Odegaard", "ode-cafe"]},
    {"id": "S3", "canonical": "Suzzallo Roasters",  "aliases": ["Suzzallo Roasters", "Suzzallo", "suzzallo-roasters"]},
    {"id": "S4", "canonical": "UW Medical Brew",    "aliases": ["UW Medical Brew", "Med Brew", "uw-medical"]},
    {"id": "S5", "canonical": "Portage Bay Espresso","aliases": ["Portage Bay Espresso", "Portage Bay", "portage-bay"]},
]

CATEGORIES = ["Espresso", "Drip Coffee", "Tea", "Cold Brew", "Pastry", "Sandwich", "Smoothie"]

START_DATE = date(2024, 7, 1)
END_DATE   = date(2024, 12, 31)


# ─── 1. shop-sales.csv ───────────────────────────────────────────────────────

def generate_shop_sales():
    rows = []
    sale_id = 1
    current = START_DATE
    while current <= END_DATE:
        for shop in SHOPS:
            # S3 (Suzzallo) has suspiciously flat sales — data collection error
            is_flat = shop["id"] == "S3"
            # Use inconsistent name (rotate through aliases)
            name_alias = random.choice(shop["aliases"])
            n_transactions = random.randint(30, 80) if not is_flat else random.randint(28, 32)
            for _ in range(n_transactions):
                cat = random.choice(CATEGORIES)
                unit_price = {
                    "Espresso": 4.75, "Drip Coffee": 2.50, "Tea": 3.25,
                    "Cold Brew": 5.25, "Pastry": 3.50, "Sandwich": 8.75, "Smoothie": 6.50
                }[cat]
                qty = random.choices([1, 2, 3], weights=[70, 25, 5])[0]
                # Date format: ISO for most, US format for ~15% of rows (intentional inconsistency)
                fmt = "us" if random.random() < 0.15 else "iso"
                rows.append({
                    "sale_id": f"TXN-{sale_id:05d}",
                    "date": date_str(current, fmt),
                    "shop_name": name_alias,
                    "category": cat,
                    "item": f"{cat} Item {random.randint(1,5)}",
                    "quantity": qty,
                    "unit_price": unit_price,
                    "total": round(unit_price * qty, 2),
                    "payment_method": random.choice(["Card", "Cash", "Mobile", "Card", "Card"]),
                })
                sale_id += 1
        current += timedelta(days=1)
    path = os.path.join(COFFEE_DIR, "shop-sales.csv")
    fields = ["sale_id","date","shop_name","category","item","quantity","unit_price","total","payment_method"]
    write_csv(path, rows, fields)


# ─── 2. menu-catalog.json ────────────────────────────────────────────────────

def generate_menu_catalog():
    items = []
    item_id = 1
    for cat in CATEGORIES:
        n = random.randint(8, 14)
        for i in range(1, n + 1):
            base_price = {
                "Espresso": 4.75, "Drip Coffee": 2.50, "Tea": 3.25,
                "Cold Brew": 5.25, "Pastry": 3.50, "Sandwich": 8.75, "Smoothie": 6.50
            }[cat]
            cogs_pct = random.uniform(0.25, 0.42)
            items.append({
                "item_id": f"ITM-{item_id:03d}",
                "category": cat,
                "name": f"{cat} {['Classic','Reserve','House','Seasonal','Signature'][i % 5]} {['Blend','Style','Roast','Special','Select'][item_id % 5]}",
                "price": round(jitter(base_price, 0.2), 2),
                "cost_of_goods": round(jitter(base_price * cogs_pct, 0.1), 2),
                "available_shops": random.sample([s["canonical"] for s in SHOPS], random.randint(2, 5)),
                "seasonal": random.choice([True, False, False]),
                "calories": random.randint(0, 450) if cat not in ["Espresso","Drip Coffee","Tea"] else random.randint(5, 200),
            })
            item_id += 1
    path = os.path.join(COFFEE_DIR, "menu-catalog.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"items": items, "last_updated": "2024-12-15", "total_items": len(items)}, f, indent=2)
    print(f"  Wrote {len(items)} items -> {os.path.relpath(path, ROOT)}")


# ─── 3. social-signals.csv ───────────────────────────────────────────────────

def generate_social_signals():
    rows = []
    current = START_DATE
    week = 1
    while current <= END_DATE:
        for shop in SHOPS:
            name_alias = shop["canonical"]  # consistent here — different from sales file
            followers = random.randint(800, 4000)
            posts = random.randint(2, 8)
            likes = jitter(posts * random.randint(30, 120))
            comments = jitter(likes * 0.08)
            shares = jitter(likes * 0.03)

            # Week 18 (shop S1 HUB Coffee) has a viral post — outlier
            if shop["id"] == "S1" and week == 18:
                likes = round(likes * 47)
                shares = round(shares * 85)
                comments = round(comments * 30)

            rows.append({
                "week_start": date_str(current),
                "shop_id": shop["id"],
                "shop_name": name_alias,
                "platform": random.choice(["Instagram", "TikTok", "Instagram", "X"]),
                "followers": followers,
                "posts_published": posts,
                "total_likes": int(likes),
                "total_comments": int(comments),
                "total_shares": int(shares),
                "engagement_rate": round((int(likes) + int(comments)) / max(followers, 1), 4),
            })
        current += timedelta(weeks=1)
        week += 1
    path = os.path.join(COFFEE_DIR, "social-signals.csv")
    fields = ["week_start","shop_id","shop_name","platform","followers","posts_published",
              "total_likes","total_comments","total_shares","engagement_rate"]
    write_csv(path, rows, fields)


# ─── 4. vendor-bids.csv ─────────────────────────────────────────────────────

def generate_vendor_bids():
    vendors = ["PacificBean Supply", "Seattle Roast Co.", "CampusBev Distributors", "Northwest Grains", "EspressoEdge LLC"]
    line_items = [
        ("Coffee Beans (lb)", 8.50),
        ("Milk (gallon)", 3.20),
        ("Paper Cups (case/500)", 18.00),
        ("Espresso Machine Service (annual)", 850.00),
        ("Cold Brew Kegs (5L)", 42.00),
        ("Pastry Delivery (weekly)", 120.00),
        ("Syrup Bottles (case/12)", 54.00),
        ("Cleaning Supplies (monthly)", 65.00),
    ]
    rows = []
    bid_id = 1
    for vendor in vendors:
        for item, base_price in line_items:
            # INTENTIONAL: some vendors don't quote all line items (missing values)
            if random.random() < 0.22:
                price_quoted = ""
                notes = "No quote submitted"
            else:
                price_quoted = round(jitter(base_price, 0.25), 2)
                notes = random.choice(["", "", "", "Volume discount available", "Lead time 3 days", "Preferred supplier"])
            rows.append({
                "bid_id": f"BID-{bid_id:03d}",
                "vendor": vendor,
                "line_item": item,
                "unit": item.split("(")[1].rstrip(")") if "(" in item else "unit",
                "price_quoted": price_quoted,
                "delivery_days": random.randint(1, 7) if price_quoted else "",
                "contract_term_months": random.choice([6, 12, 24]) if price_quoted else "",
                "notes": notes,
                "bid_date": date_str(date(2024, 10, random.randint(1, 28))),
            })
            bid_id += 1
    path = os.path.join(COFFEE_DIR, "vendor-bids.csv")
    fields = ["bid_id","vendor","line_item","unit","price_quoted","delivery_days","contract_term_months","notes","bid_date"]
    write_csv(path, rows, fields)


# ─── 5. shop-profiles.md ────────────────────────────────────────────────────

def generate_shop_profiles():
    content = """# UW Campus Coffee Shop Profiles

Operational snapshots for academic year 2024-2025. Used for contextual analysis alongside transactional data.

---

## HUB Coffee (S1)

**Location**: Husky Union Building, Ground Floor  
**Capacity**: 48 seats, high foot traffic corridor  
**Hours**: Mon-Fri 7:00-19:00, Sat 8:00-16:00, Sun Closed  
**Espresso Machines**: 2x La Marzocca Linea PB (2021, good condition)  
**Grinders**: 3x Mazzer Kony (2020)  
**Staff FTE**: 4.5  
**Annual Lease Cost**: $48,000  
**Notes**: Highest foot traffic on campus. Serves main student hub, event venue nearby. Social media presence strongest of all shops.

---

## Odegaard Cafe (S2)

**Location**: Odegaard Undergraduate Library, Level 1  
**Capacity**: 24 seats, study corridor  
**Hours**: Mon-Thu 7:30-22:00, Fri 7:30-18:00, Sat-Sun 10:00-18:00  
**Espresso Machines**: 1x Nuova Simonelli Aurelia (2019, needs service)  
**Grinders**: 2x Mazzer Super Jolly (2018)  
**Staff FTE**: 3.0  
**Annual Lease Cost**: $32,000  
**Notes**: Late-night demand spike during finals weeks. Single machine creates bottleneck during peak hours.

---

## Suzzallo Roasters (S3)

**Location**: Suzzallo Library, Reading Room Entrance  
**Capacity**: 18 seats, heritage building  
**Hours**: Mon-Fri 8:00-17:00, Sat 9:00-15:00, Sun Closed  
**Espresso Machines**: 1x Victoria Arduino Black Eagle (2022, excellent)  
**Grinders**: 2x Eureka Atom (2022)  
**Staff FTE**: 2.5  
**Annual Lease Cost**: $28,500  
**Notes**: Premium positioning, lower volume by design. Sales data shows suspiciously consistent daily totals — possible POS sync issue since October 2024. Flag for IT audit.

---

## UW Medical Brew (S4)

**Location**: Health Sciences Building, Lobby  
**Capacity**: 30 seats, clinical environment  
**Hours**: Mon-Fri 6:30-18:00, Sat 7:00-14:00, Sun Closed  
**Espresso Machines**: 2x Rancilio Specialty RS1 (2020, fair condition)  
**Grinders**: 2x Anfim Caimano (2019)  
**Staff FTE**: 3.5  
**Annual Lease Cost**: $36,000  
**Notes**: Strong morning rush from medical staff. Higher average ticket due to food add-ons. Machine #2 had downtime in September 2024 (5 days).

---

## Portage Bay Espresso (S5)

**Location**: Portage Bay Building, Street Level  
**Capacity**: 22 seats, neighborhood-facing  
**Hours**: Mon-Fri 7:00-17:00, Sat 8:00-14:00, Sun Closed  
**Espresso Machines**: 1x Synesso MVP (2021, good)  
**Grinders**: 2x Mahlkonig EK43 (2021)  
**Staff FTE**: 2.5  
**Annual Lease Cost**: $26,000  
**Notes**: Lowest lease cost, moderate volume. Serves graduate student population. Newer build, minimal maintenance history.
"""
    path = os.path.join(COFFEE_DIR, "shop-profiles.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Wrote shop-profiles.md -> {os.path.relpath(path, ROOT)}")


# ─── 6. job-postings.csv ────────────────────────────────────────────────────

def generate_job_postings():
    companies = [
        "Amazon", "Microsoft", "Boeing", "Expedia", "Zillow", "Tableau", "Accenture",
        "Deloitte", "McKinsey", "KPMG", "Nordstrom", "REI", "Starbucks", "Costco",
        "T-Mobile", "Convoy", "Remitly", "Highspot", "Auth0", "Outreach",
        "PwC", "EY", "IQVIA", "Providence Health", "Seattle Children's",
    ]
    # INTENTIONAL: inconsistent title variants
    title_groups = [
        ["Data Analyst", "Jr. Data Analyst", "Analyst, Data", "Associate Data Analyst", "Data Analyst I"],
        ["Business Intelligence Analyst", "BI Analyst", "Business Intelligence Developer", "BI Developer"],
        ["Data Scientist", "Jr. Data Scientist", "Associate Data Scientist", "Data Scientist I"],
        ["Data Engineer", "Jr. Data Engineer", "Associate Data Engineer", "Analytics Engineer"],
        ["Marketing Analyst", "Digital Marketing Analyst", "Marketing Data Analyst", "Growth Analyst"],
        ["Product Analyst", "Product Data Analyst", "Associate Product Analyst"],
        ["Financial Analyst", "Finance Analyst", "FP&A Analyst", "Associate Financial Analyst"],
        ["Operations Analyst", "Business Operations Analyst", "Ops Analyst"],
    ]
    skills_pool = [
        "SQL", "Python", "R", "Excel", "Tableau", "Power BI", "Looker",
        "Spark", "dbt", "Snowflake", "BigQuery", "AWS", "Azure", "GCP",
        "Statistics", "Machine Learning", "A/B Testing", "Data Modeling",
        "Communication", "Stakeholder Management",
    ]
    work_types = ["Remote", "Hybrid", "On-site"]
    locations = ["Seattle, WA", "Bellevue, WA", "Redmond, WA", "Kirkland, WA", "Remote"]
    rows = []
    for i in range(1, 401):
        group = random.choice(title_groups)
        title = random.choice(group)
        company = random.choice(companies)
        post_date = date(2024, random.randint(6, 12), random.randint(1, 28))
        # INTENTIONAL: ~30% missing salary ranges
        if random.random() < 0.30:
            salary_min = ""
            salary_max = ""
        else:
            base = random.choice([55000, 65000, 72000, 80000, 90000, 100000, 115000])
            salary_min = base
            salary_max = base + random.choice([10000, 15000, 20000, 25000])
        # INTENTIONAL: ~8% expired listings (old dates, still in feed)
        if random.random() < 0.08:
            post_date = date(2023, random.randint(1, 12), random.randint(1, 28))
        # INTENTIONAL: ~5% duplicate postings (same title+company, slightly different date)
        is_dup = random.random() < 0.05
        job_skills = random.sample(skills_pool, random.randint(3, 7))
        uw_partnership = company in ["Amazon", "Microsoft", "Boeing", "Deloitte", "Accenture", "PwC"] and random.random() < 0.4
        rows.append({
            "posting_id": f"JOB-{i:04d}",
            "title": title,
            "company": company,
            "location": random.choice(locations),
            "work_type": random.choice(work_types),
            "salary_min": salary_min,
            "salary_max": salary_max,
            "required_skills": "; ".join(job_skills),
            "experience_years": random.choice([0, 1, 1, 2, 2, 3]),
            "posted_date": date_str(post_date),
            "uw_partnership": uw_partnership,
            "is_duplicate_flag": is_dup,
            "status": "Active" if post_date >= date(2024, 6, 1) else "Expired",
        })
    path = os.path.join(JOB_DIR, "job-postings.csv")
    fields = ["posting_id","title","company","location","work_type","salary_min","salary_max",
              "required_skills","experience_years","posted_date","uw_partnership","is_duplicate_flag","status"]
    write_csv(path, rows, fields)


# ─── 7. internship-programs.csv ──────────────────────────────────────────────

def generate_internship_programs():
    companies = [
        "Amazon", "Microsoft", "Boeing", "Expedia", "Zillow", "Tableau",
        "Accenture", "Deloitte", "McKinsey", "KPMG", "Nordstrom",
        "T-Mobile", "Remitly", "Highspot", "Auth0", "IQVIA", "PwC", "EY",
    ]
    roles = [
        "Data Analytics Intern", "Business Intelligence Intern", "Data Science Intern",
        "Marketing Analytics Intern", "Finance Analytics Intern", "Product Analytics Intern",
        "Operations Analytics Intern", "Strategy Analyst Intern",
    ]
    rows = []
    for i, company in enumerate(companies * 6, start=1):
        if i > 100: break
        role = random.choice(roles)
        duration = random.choice([10, 12, 14, 16])
        base_weekly = random.choice([800, 900, 1000, 1100, 1200, 1400, 1600, 2000, 2200])
        compensation = f"${base_weekly}/week" if random.random() > 0.1 else "Unpaid / Credit"
        uw_partner = company in ["Amazon", "Microsoft", "Boeing", "Deloitte", "Accenture", "PwC", "McKinsey"]
        rows.append({
            "intern_id": f"INT-{i:03d}",
            "company": company,
            "role": role,
            "duration_weeks": duration,
            "compensation": compensation,
            "location": random.choice(["Seattle, WA", "Bellevue, WA", "Remote", "Hybrid"]),
            "start_term": random.choice(["Summer 2025", "Fall 2025", "Winter 2026", "Spring 2026"]),
            "uw_partnership": uw_partner,
            "application_deadline": date_str(date(2025, random.randint(1, 4), random.randint(1, 28))),
            "openings": random.randint(1, 8),
        })
    path = os.path.join(JOB_DIR, "internship-programs.csv")
    fields = ["intern_id","company","role","duration_weeks","compensation","location",
              "start_term","uw_partnership","application_deadline","openings"]
    write_csv(path, rows, fields)


# ─── 8. skills-demand.csv ────────────────────────────────────────────────────

def generate_skills_demand():
    skills = [
        ("SQL", "Technical"),
        ("Python", "Technical"),
        ("Excel", "Technical"),
        ("Tableau", "Visualization"),
        ("Power BI", "Visualization"),
        ("R", "Technical"),
        ("Statistics", "Analytical"),
        ("Machine Learning", "Analytical"),
        ("A/B Testing", "Analytical"),
        ("Communication", "Soft"),
        ("Data Modeling", "Technical"),
        ("Looker", "Visualization"),
        ("dbt", "Technical"),
        ("Snowflake", "Technical"),
        ("BigQuery", "Technical"),
        ("AWS", "Cloud"),
        ("Azure", "Cloud"),
        ("Spark", "Technical"),
        ("Stakeholder Management", "Soft"),
        ("Problem Solving", "Soft"),
        ("Presentation", "Soft"),
        ("SQL Advanced", "Technical"),
        ("GCP", "Cloud"),
        ("Data Cleaning", "Analytical"),
        ("Dashboard Design", "Visualization"),
        ("ETL/ELT", "Technical"),
        ("Business Acumen", "Soft"),
        ("Git / Version Control", "Technical"),
        ("Data Governance", "Analytical"),
        ("API Integration", "Technical"),
    ]
    role_cats = ["Data Analyst", "Business Intelligence", "Data Scientist", "Data Engineer", "Marketing Analytics", "Finance Analytics"]
    rows = []
    for skill_name, skill_cat in skills:
        for role in role_cats:
            base_freq = random.randint(15, 95)
            rows.append({
                "skill": skill_name,
                "skill_category": skill_cat,
                "role_category": role,
                "posting_count": base_freq,
                "pct_of_postings": round(base_freq / 400 * 100, 1),
                "yoy_change_pct": round(random.uniform(-15, 35), 1),
                "median_salary_premium": random.choice([0, 0, 2000, 5000, 8000, 12000]),
            })
    path = os.path.join(JOB_DIR, "skills-demand.csv")
    fields = ["skill","skill_category","role_category","posting_count","pct_of_postings","yoy_change_pct","median_salary_premium"]
    write_csv(path, rows, fields)


# ─── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Generating coffee shop data...")
    generate_shop_sales()
    generate_menu_catalog()
    generate_social_signals()
    generate_vendor_bids()
    generate_shop_profiles()

    print("\nGenerating job market data...")
    generate_job_postings()
    generate_internship_programs()
    generate_skills_demand()

    print("\nAll data files generated successfully.")
