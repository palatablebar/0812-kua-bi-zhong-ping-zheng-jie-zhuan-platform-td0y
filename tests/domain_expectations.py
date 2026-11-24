EXPECTED = {
    "0001": (2, 30, "READY"),
    "0002": (2, 2, "READY"),
    "0003": (0, None, "RATE_UNAVAILABLE"),
    "0004": (2, 14, "MISMATCH"),
}
EVIDENCE = {"0001": {"debit": 30, "credit": 30}, "0002": {"debit": 2, "credit": 1}}
