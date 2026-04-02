"""
category_map.py — Category keyword mapping and broad category groupings.

CATEGORY_MAP : keyword → canonical category name (as it appears in column A of the sheet)
BROAD_CATEGORIES : section name → list of sub-category names (order matches the sheet)
"""

CATEGORY_MAP: dict[str, list[str]] = {
    # Income
    "Salary": ["Salary", "Salart", "Calary"],
    "Agaf Hashikom": ["Agaf", "agaf", "shikom", "shikum", "shikumi", "shikomi", "agaf hashikom", "agaf hashikum"],
    "Miloim": ["Miloim", "Miluim", "miluim", "miloim"],
    "Avtala": ["avtala", "Avtala"],
    "Extra": ["extra", "Extra", "Xtra", "Money", "Extra money", "plus", "+"],

    # Savings
    "Vacation Fund": ["vacation fund", "vacation saving", "vacation savings", "vacasion savings"],
    "Transfer to Savings": ["savings", "saving", "ibi"],

    # Home
    "Rent": ["rent", "lease", "apartment fee"],
    "Electricity": ["electricity", "electric", "power", "energy", "utility"],
    "Gas": ["gas"],
    "Water": ["water", "water bill"],
    "Property Tax": ["Property Tax", "Tax", "Arnona"],
    "Internet": ["internet", "wifi", "network"],
    "House Committee": ["committee", "house committee", "vaad", "vahad", "vaad bait"],
    "Maintenance": ["maintenance", "improvement", "repair", "fix", "home", "flowers", "flower", "upgrade", "repairs"],
    "Phone Bill": ["Phone", "phone bill"],

    # Transportation
    "Fuel": ["Fuel", "diesel", "delek"],
    "Public Transportation": [
        "train", "taxi", "bus", "metro", "tram", "cab", "subway", "ride",
        "public", "transport", "bird", "lime", "tahbatz", "moovit", "movit", "movite",
    ],
    "Parking": ["parking", "pango", "cellopark", "cello", "hanaya"],
    "Other (Trans)": [
        "transportation other", "car insurance", "test", "car test", "garage", "musah", "car repair", "car",
    ],

    # Daily Living
    "Groceries": ["groceries", "supermarket", "market", "super", "store", "ampm", "victory"],
    "Coffee": ["coffee", "latte", "espresso", "cappuccino", "brew", "americano", "mocha", "cafe"],
    "Dinning Out": [
        "dining", "restaurant", "meal", "breakfast", "lunch", "dinner", "eat", "food",
        "takeout", "delivery", "wolt", "walt", "misada", "dinning", "dinning out", "dining out",
    ],
    "Beer / Wine": [
        "beer", "wine", "alcohol", "bar", "cocktail", "drink", "vodka",
        "whiskey", "liquor", "birra", "bira", "pub",
    ],
    "Cloths": [
        "cloths", "shirt", "pants", "dress", "clothes", "cloth", "tshirt",
        "t-shirt", "t shirt", "clothe", "clothse",
    ],
    "Haircut": ["haircut", "hair cut"],
    "Other (Daily)": [
        "daily living other", "other daily living", "Other (Daily)", "Other Daily",
        "other", "cosmetics", "personal", "gym", "personal care", "wedding",
    ],

    # Other
    "Vacation": ["vacation", "holiday", "trip", "travel", "hotel", "flight", "resort"],
    "Entertainment": ["entertainment", "movie", "theater", "show", "concert", "game", "festival", "fun", "games"],
    "Health": [
        "health", "doctor", "medicine", "hospital", "clinic", "checkup", "medical", "healthcare",
        "superpharm", "superfarm", "suplaments", "vaitamins", "vitamins", "vatimins",
    ],

    # Insurance
    "Life Insurance": ["life insurance", "life inshurance"],
    "Health Insurance": ["health insurance", "health inshurance"],

    # Personal
    "Moran": ["moran"],
    "Nadav": ["nadav"],
    "Fighter": ["fighter"],
}

# Broad categories used by /summary and the monthly report.
# Only sections that appear in the Google Sheet as summary rows are listed here.
BROAD_CATEGORIES: dict[str, list[str]] = {
    "Home": [
        "Rent",
        "Electricity",
        "Gas",
        "Water",
        "Property Tax",
        "Internet",
        "House Committee",
        "Maintenance",
        "Phone Bill",
    ],
    "Transportation": [
        "Fuel",
        "Public Transportation",
        "Parking",
        "Other (Trans)",
    ],
    "Daily Living": [
        "Groceries",
        "Coffee",
        "Dinning Out",
        "Beer / Wine",
        "Cloths",
        "Haircut",
        "Other (Daily)",
    ],
    "Other": [
        "Vacation",
        "Entertainment",
        "Health",
    ],
}

# ---------------------------------------------------------------------------
# Keyword index — built once at import time, used by the parser
# ---------------------------------------------------------------------------

KEYWORD_INDEX: dict[str, str] = {}
for _category, _keywords in CATEGORY_MAP.items():
    for _kw in _keywords:
        KEYWORD_INDEX[_kw.lower()] = _category
