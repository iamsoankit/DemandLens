import pandas as pd

from build_dataset import build_dataset


def analyze_price_demand(df):
    df = df.copy()

    group = df.groupby(["store_id", "item_id"])

    df["previous_price"] = group["sell_price"].shift(1)
    df["previous_demand"] = group["demand"].shift(1)

    df["price_change_pct"] = (
        (df["sell_price"] - df["previous_price"])
        / df["previous_price"]
    )

    df["demand_change_pct"] = (
        (df["demand"] - df["previous_demand"])
        / df["previous_demand"]
    )

    valid = df[
        df["sell_price"].notna()
        & df["previous_price"].notna()
        & df["previous_price"].gt(0)
        & df["previous_demand"].gt(0)
        & df["price_change_pct"].notna()
        & df["demand_change_pct"].notna()
    ].copy()

    valid = valid[
        valid["price_change_pct"].abs() > 0.01
    ]

    valid = valid[
        (valid["price_change_pct"].abs() < 1.0)
        & (valid["demand_change_pct"].abs() < 5.0)
    ]

    valid["price_direction"] = (
        valid["price_change_pct"] > 0
    ).map(
        {
            True: "price_increase",
            False: "price_decrease",
        }
    )

    summary = (
        valid.groupby("price_direction")
        .agg(
            observations=("demand_change_pct", "count"),
            avg_price_change=("price_change_pct", "mean"),
            median_price_change=("price_change_pct", "median"),
            avg_demand_change=("demand_change_pct", "mean"),
            median_demand_change=("demand_change_pct", "median"),
        )
        .reset_index()
    )

    return valid, summary


def main():
    print("Loading data...")

    df = build_dataset(n_items=30)

    valid, summary = analyze_price_demand(df)

    print("\nPrice-demand analysis")
    print(summary.to_string(index=False))

    print("\nValid observations:", len(valid))

    summary.to_csv(
        "results/price_demand_summary.csv",
        index=False,
    )

    valid[
        [
            "date",
            "store_id",
            "item_id",
            "sell_price",
            "previous_price",
            "demand",
            "previous_demand",
            "price_change_pct",
            "demand_change_pct",
            "price_direction",
        ]
    ].to_csv(
        "results/price_demand_observations.csv",
        index=False,
    )

    print("\nSaved:")
    print("results/price_demand_summary.csv")
    print("results/price_demand_observations.csv")


if __name__ == "__main__":
    main()