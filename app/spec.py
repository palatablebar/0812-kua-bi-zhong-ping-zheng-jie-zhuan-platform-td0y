COLUMNS = ("day", "amount_cents", "rate_ppm", "currency", "tolerance_cents")
KINDS = ("rate", "debit", "credit", "close")
PROJECT = {
    "name": "跨币种凭证结转台",
    "actor": "财务共享中心总账员",
    "stages": [
        ("intake", "样例采信"),
        ("prepare", "有效汇率"),
        ("calculate", "凭证折算"),
        ("policy", "借贷平衡"),
        ("balance", "运行对账"),
    ],
    "chart": "本位币金额",
}
