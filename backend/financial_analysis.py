import re

def extract_financial_data(text):

    data = {}

    # Look for large financial numbers (at least 5 digits)
    revenue_match = re.search(r"Revenue[^$0-9]*\$?([\d,]{5,})", text, re.IGNORECASE)

    profit_match = re.search(
        r"(Net income|Net profit)[^$0-9]*\$?([\d,]{5,})",
        text,
        re.IGNORECASE
    )

    debt_match = re.search(
        r"(Total debt|Total liabilities)[^$0-9]*\$?([\d,]{5,})",
        text,
        re.IGNORECASE
    )

    if revenue_match:
        data["revenue"] = int(revenue_match.group(1).replace(",", ""))

    if profit_match:
        data["profit"] = int(profit_match.group(2).replace(",", ""))

    if debt_match:
        data["debt"] = int(debt_match.group(2).replace(",", ""))

    return data

def calculate_ratios(data):

    ratios = {}

    revenue = data.get("revenue")
    profit = data.get("profit")
    debt = data.get("debt")

    if revenue and profit:
        ratios["profit_margin"] = round(profit / revenue, 2)

    if revenue and debt:
        ratios["debt_ratio"] = round(debt / revenue, 2)

    return ratios