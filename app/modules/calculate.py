from app.business import measured


def compute(data):
    postings, tolerance = data
    amounts = {"debit": 0, "credit": 0}
    for kind, amount, rate in postings:
        amounts[kind] += (amount * rate + 500000) // 1000000
    return measured(amounts["debit"], amounts["credit"], "分", amounts, tolerance)
