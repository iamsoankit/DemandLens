import pandas as pd

from build_dataset import build_dataset


def create_features(df):
    df = df.copy()

    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    df["weekend"] = (df["day_of_week"] >= 5).astype(int)

    group = df.groupby(["store_id", "item_id"])["demand"]

    df["lag_1"] = group.shift(1)
    df["lag_7"] = group.shift(7)
    df["lag_28"] = group.shift(28)

    df["rolling_mean_7"] = (
        df.groupby(["store_id", "item_id"])["demand"]
        .transform(lambda x: x.shift(1).rolling(7).mean())
    )

    df["rolling_mean_28"] = (
        df.groupby(["store_id", "item_id"])["demand"]
        .transform(lambda x: x.shift(1).rolling(28).mean())
    )

    df["rolling_std_7"] = (
        df.groupby(["store_id", "item_id"])["demand"]
        .transform(lambda x: x.shift(1).rolling(7).std())
    )

    df["price_change"] = (
        df.groupby(["store_id", "item_id"])["sell_price"]
        .pct_change(fill_method=None)
    )

    df["target"] = (
        df.groupby(["store_id", "item_id"])["demand"]
        .shift(-1)
    )

    df["price_missing"] = df["sell_price"].isna().astype(int)
    df["price_change"] = df["price_change"].fillna(0)

    return df


if __name__ == "__main__":
    df = build_dataset(n_items=30)
    df = create_features(df)

    feature_columns = [
        "date",
        "store_id",
        "item_id",
        "cat_id",
        "sell_price",
        "price_missing",
        "day_of_week",
        "month",
        "weekend",
        "lag_1",
        "lag_7",
        "lag_28",
        "rolling_mean_7",
        "rolling_mean_28",
        "rolling_std_7",
        "price_change",
        "target",
    ]

    df = df[feature_columns]

    print("Feature dataset:", df.shape)

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nSample:")
    print(df.tail().to_string(index=False))