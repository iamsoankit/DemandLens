import os

import pandas as pd


RESULTS_DIR = "results"


def simulate_prices(price, predicted_demand):
    price_changes = [-0.10, -0.05, 0.00, 0.05, 0.10]

    # Scenario assumptions rather than causal estimates.
    elasticity_scenarios = [-0.5, -1.0, -1.5]

    rows = []

    for elasticity in elasticity_scenarios:
        for price_change in price_changes:
            candidate_price = price * (1 + price_change)

            demand_change = elasticity * price_change

            estimated_demand = predicted_demand * (
                1 + demand_change
            )

            estimated_demand = max(estimated_demand, 0)

            estimated_revenue = (
                candidate_price * estimated_demand
            )

            rows.append(
                {
                    "elasticity": elasticity,
                    "price_change": price_change,
                    "candidate_price": candidate_price,
                    "predicted_demand": predicted_demand,
                    "estimated_demand": estimated_demand,
                    "estimated_revenue": estimated_revenue,
                }
            )

    return pd.DataFrame(rows)


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    print("Loading model predictions...")

    predictions = pd.read_csv(
        f"{RESULTS_DIR}/predictions.csv"
    )

    predictions["date"] = pd.to_datetime(
        predictions["date"]
    )

    predictions = predictions[
        predictions["sell_price"].notna()
        & predictions["predicted_demand"].gt(0)
    ].copy()

    if predictions.empty:
        raise ValueError(
            "No valid positive-demand predictions found."
        )

    # Use the latest valid out-of-sample prediction.
    selected = (
        predictions
        .sort_values("date")
        .iloc[-1]
    )

    current_price = selected["sell_price"]
    predicted_demand = selected["predicted_demand"]

    print("\nSelected prediction:")

    print("Date:", selected["date"].date())
    print("Store:", selected["store_id"])
    print("Item:", selected["item_id"])
    print(
        "Current price:",
        round(current_price, 2),
    )
    print(
        "Predicted demand:",
        round(predicted_demand, 3),
    )

    scenarios = simulate_prices(
        current_price,
        predicted_demand,
    )

    print("\nPricing scenarios:")
    print(
        scenarios.to_string(index=False)
    )

    best = (
        scenarios.loc[
            scenarios.groupby("elasticity")[
                "estimated_revenue"
            ].idxmax()
        ]
        .sort_values("elasticity")
    )

    print("\nBest scenario under each elasticity assumption:")

    print(
        best[
            [
                "elasticity",
                "price_change",
                "candidate_price",
                "estimated_demand",
                "estimated_revenue",
            ]
        ].to_string(index=False)
    )

    scenarios.to_csv(
        f"{RESULTS_DIR}/pricing_scenarios.csv",
        index=False,
    )

    best.to_csv(
        f"{RESULTS_DIR}/pricing_recommendations.csv",
        index=False,
    )

    print("\nSaved:")
    print("results/pricing_scenarios.csv")
    print("results/pricing_recommendations.csv")


if __name__ == "__main__":
    main()