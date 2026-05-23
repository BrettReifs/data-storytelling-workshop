# Coffee Shop Data — Dictionary

Synthetic data representing UW campus coffee shop operations, academic year 2024-2025. Data has intentional quality issues for pedagogical purposes.

---

## shop-sales.csv

Daily transaction records for 5 campus coffee shops, July 1 – December 31, 2024.

| Column | Type | Description |
|--------|------|-------------|
| `sale_id` | string | Unique transaction ID (TXN-00001 format) |
| `date` | string | Transaction date — **mixed formats** (ISO `YYYY-MM-DD` and US `MM/DD/YYYY`) |
| `shop_name` | string | Shop name — **inconsistent** (3+ variants per shop) |
| `category` | string | Product category (Espresso, Drip Coffee, Tea, Cold Brew, Pastry, Sandwich, Smoothie) |
| `item` | string | Item description |
| `quantity` | integer | Units sold |
| `unit_price` | float | Price per unit |
| `total` | float | Line total (quantity × unit_price) |
| `payment_method` | string | Card, Cash, or Mobile |

**Known Quality Issues:**
- `date`: ~15% of rows use MM/DD/YYYY instead of ISO 8601. Parse carefully.
- `shop_name`: "HUB Coffee" appears as "The HUB," "hub-coffee," and "HUB." Standardize before grouping.
- Shop S3 (Suzzallo Roasters): daily transaction count is suspiciously flat (28-32/day). Possible POS sync issue since October 2024.

See [`../QUALITY-ISSUES.md`](../QUALITY-ISSUES.md) for root cause analysis and real-world frequency assessment of all quality issues.

**Approximate volume:** ~46,000 rows

---

## menu-catalog.json

Menu items across all 5 shops with pricing and cost-of-goods data.

```json
{
  "items": [...],
  "last_updated": "2024-12-15",
  "total_items": 78
}
```

Each item:

| Field | Type | Description |
|-------|------|-------------|
| `item_id` | string | Unique item ID (ITM-001 format) |
| `category` | string | Product category |
| `name` | string | Item name |
| `price` | float | Retail price |
| `cost_of_goods` | float | Cost of goods sold (COGS) |
| `available_shops` | array | List of shop canonical names where item is sold |
| `seasonal` | boolean | Whether item is seasonal |
| `calories` | integer | Calorie count |

**Note:** `available_shops` uses canonical shop names. Cross-reference with `shop-sales.csv` requires normalization.

---

## social-signals.csv

Weekly social media metrics per shop, full 6-month window.

| Column | Type | Description |
|--------|------|-------------|
| `week_start` | string | ISO date of week start (Monday) |
| `shop_id` | string | Shop identifier (S1–S5) |
| `shop_name` | string | Canonical shop name |
| `platform` | string | Instagram, TikTok, or X |
| `followers` | integer | Follower count at week start |
| `posts_published` | integer | Posts published that week |
| `total_likes` | integer | Aggregate likes across posts |
| `total_comments` | integer | Aggregate comments |
| `total_shares` | integer | Aggregate shares |
| `engagement_rate` | float | (likes + comments) / followers |

**Known Quality Issues:**
- Week 18, HUB Coffee (S1): viral post caused extreme outlier. Total likes 47x baseline, shares 85x baseline.
- This is a real signal, not a data error — but it skews any average engagement rate calculation.

---

## vendor-bids.csv

Competitive bids from 5 vendors across 8 supply line items.

| Column | Type | Description |
|--------|------|-------------|
| `bid_id` | string | Unique bid ID |
| `vendor` | string | Vendor name |
| `line_item` | string | Supply category |
| `unit` | string | Unit of measure |
| `price_quoted` | float | Quoted price (empty if no quote submitted) |
| `delivery_days` | integer | Lead time (empty if no quote) |
| `contract_term_months` | integer | 6, 12, or 24 months |
| `notes` | string | Optional vendor notes |
| `bid_date` | string | ISO date of bid submission |

**Known Quality Issues:**
- `price_quoted` is empty (~22% of rows): vendors that didn't quote all line items.
- Empty = no bid submitted, not zero price. Exclude from pricing averages.

---

## shop-profiles.md

Operational metadata for each shop: location, capacity, hours, equipment, staff FTE, lease cost.

Format: free-form Markdown, one section per shop.

**Note:** The Suzzallo Roasters profile mentions a suspected POS sync issue — cross-reference with the flat-sales anomaly in `shop-sales.csv`.
