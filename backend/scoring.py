def credit_score(ratios, risk_signals):

    score = 100

    profit_margin = ratios.get("profit_margin", 0)
    debt_ratio = ratios.get("debt_ratio", 0)

    # Profitability evaluation
    if profit_margin < 0.05:
        score -= 30
    elif profit_margin < 0.1:
        score -= 15

    # Debt evaluation
    if debt_ratio > 0.7:
        score -= 30
    elif debt_ratio > 0.5:
        score -= 15

    # External risk penalty
    if len(risk_signals) > 0:
        score -= 25

    return score


def loan_decision(score):

    if score >= 80:
        return "APPROVE"

    elif score >= 65:
        return "APPROVE WITH CONDITIONS"

    elif score >= 50:
        return "REVIEW"

    else:
        return "REJECT"