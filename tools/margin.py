SPEC = {
    "name": "margin",
    "description": "Gross margin from revenue and cost: the profit and the margin percentage.",
    "args": {
        "revenue": {"type": "number", "description": "Revenue in dollars."},
        "cost": {"type": "number", "description": "Cost in dollars. Must not be negative."},
    },
    "readOnly": True,
}


def run(revenue, cost):
    if cost < 0:
        raise ValueError(f"margin refuses a negative cost ({cost})")
    if revenue == 0:
        raise ValueError("margin needs a non-zero revenue")
    profit = revenue - cost
    return {"profit": profit, "margin_pct": round(100 * profit / revenue, 1), "source": "margin"}
