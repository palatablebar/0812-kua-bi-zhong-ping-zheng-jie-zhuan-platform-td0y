from app.business import DomainIssue, by_kind, prepared, single


def prepare(rows):
    close = single(rows, "close")
    day = close["day"]
    rates = {}
    postings = []
    for rate in by_kind(rows, "rate"):
        if rate["day"] > day:
            continue
        key = (rate["currency"], rate["day"])
        value = rate["rate_ppm"]
        if key in rates and rates[key] != value:
            raise DomainIssue("RATE_CONFLICT")
        if not value:
            raise DomainIssue("ZERO_RATE")
        rates[key] = value
    for row in rows:
        if row["kind"] not in ("debit", "credit"):
            continue
        if row["day"] != day:
            raise DomainIssue("WRONG_POSTING_DAY")
        candidates = [k for k in rates if k[0] == row["currency"]]
        if row["currency"] and not candidates:
            raise DomainIssue("RATE_UNAVAILABLE")
        value = rates[max(candidates)] if row["currency"] else 1_000_000
        postings.append((row["kind"], row["amount_cents"], value))
    if not postings:
        raise DomainIssue("POSTING_REQUIRED")
    return prepared(
        len(postings),
        {"day": day, "quotes": len(rates)},
        (postings, close["tolerance_cents"]),
    )
