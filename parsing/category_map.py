# Category map: canonical category name -> list of keywords that trigger it.
# Keys must exactly match the row names in column A of the Google Sheet.
# Keywords are matched case-insensitively.

CATEGORY_MAP = {

    # Transportation
    "Public Transportation": [
        "train", "taxi", "bus", "metro", "tram", "cab", "subway", "ride",
        "public", "transport",
    ],
    "Fuel":         ["fuel", "petrol", "diesel"],
    "Parking":      ["parking", "garage", "space", "charging", "park"],
    "Other (Trans)": [
        "transportation other", "other transportation", "other trans",
        "Other (Trans)", "Other Trans",
    ],

    # Home Expenses
    "Rent":         ["rent", "lease", "apartment fee", "monthly payment", "mortgage"],
    "Electricity":  ["electricity", "electric", "power", "energy", "bill", "utility"],
    "Gas/Oil":      ["gas", "oil", "heating"],          # "fuel" lives in Fuel to avoid conflict
    "Water":        ["water", "sewer", "trash", "garbage", "utilities", "waste"],
    "Property Tax": ["Property Tax", "Tax", "Arnona"],
    "Internet":     ["internet", "wifi", "broadband", "net", "phone"],
    "House Committee": ["committee", "house committee", "hoa", "maintenance fee"],
    "Maintenance/Improvements": [
        "maintenance", "improvement", "repair", "fix", "home",
        "flowers", "flower", "upgrade", "repairs",
    ],

    # Daily Living
    "Groceries":    ["groceries", "supermarket", "market", "super", "store", "shopping"],
    "Coffee":       ["coffee", "latte", "espresso", "cappuccino", "brew", "americano", "mocha", "cafe"],
    "Dining Out":   ["dining", "restaurant", "meal", "breakfast", "lunch", "dinner", "eat",
                     "takeout", "delivery",  "food", "wolt", "walt"],
    "Beer / Wine":  ["beer", "wine", "alcohol", "bar", "cocktail", "drink", "pub", "bear", "vodka", "whiskey", "liquor"],
    "Other (Daily)": [
        "daily living other", "other daily living", "haircut",
        "miscellaneous living", "Other (Daily)", "Other Daily", "other", "cosmetics", "laser",
        "cloths", "shirt", "pants", "dress", "clothes", "cloth", "tshirt", "t-shirt", "t shirt",
        "personal", "gym", "personal care",
    ],

    # Entertainment and Recreation
    "Entertainment": ["entertainment", "movie", "theater", "show", "concert", "game", "festival", "fun", "games"],
    "Vacation":      ["vacation", "holiday", "trip", "travel", "hotel", "flight", "beach", "resort"],

    # Education and Healthcare
    "Education":    ["books", "courses", "education", "school"],
    "Health":       [
        "health", "doctor", "medicine", "hospital", "clinic", "checkup",
        "pharm", "superpharm", "super pharm", "super-pharm", "pharmacy",
        "medical", "healthcare",
    ],                                                 # "insurance" lives in Life Insurance to avoid conflict

    # Savings and Insurance
    "Life Insurance":   ["life insurance", "policy", "premium", "coverage", "car insurance", "health insurance"],
    "Emergency Fund":   ["emergency fund", "savings", "rainy day"],

    # Personal
    "Omer": ["omer"],
    "Gil":  ["gil"],
}


# How categories are grouped into broad sections.
# Keys must match the broad-section header names in column A of the Google Sheet
# (case-insensitive match at runtime).
# Subcategory list order and count must reflect the actual sheet layout so
# /summary can correctly locate each section's total row.
BROAD_CATEGORIES = {
    "Home": [
        "Rent", "Mortgage",  # Mortgage row exists in the sheet; not loggable via bot
        "Electricity", "Gas/Oil", "Water",
        "Property Tax", "Internet", "House Committee", "Maintenance/Improvements",
    ],
    "Transportation": [
        "Public Transportation", "Fuel", "Parking", "Other (Trans)",
    ],
    "Daily Living": [
        "Groceries", "Coffee", "Dining Out", "Beer / Wine", "Other (Daily)",
    ],
    "Other": [
        "Entertainment", "Vacation", "Health", "Life Insurance",
        # Add "Education" and/or "Emergency Fund" here if they appear under this
        # section header in your sheet.
    ],
}
