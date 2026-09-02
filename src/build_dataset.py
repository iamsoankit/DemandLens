import pandas as pd

from data import load_calendar, load_sales, load_prices, prepare_calendar


def build_dataset(n_items=30):
    sales = load_sales()
    calendar = prepare_calendar(load_calendar())
    prices = load_prices()

    selected_items = sales["item_id"].drop_duplicates().head(n_items)
    sales = sales[sales["item_id"].isin(selected_items)].copy()

    id_columns = [
        "id",
        "item_id",
        "dept_id",
        "cat_id",
        "store_id",
        "state_id",
    ]

    sales_long = sales.melt(
        id_vars=id_columns,
        var_name="d",
        value_name="demand",
    )

    day_map = calendar.reset_index()
    day_map["d"] = "d_" + (day_map.index + 1).astype(str)

    sales_long = sales_long.merge(
        day_map[["d", "date", "wm_yr_wk"]],
        on="d",
        how="left",
    )

    sales_long = sales_long.merge(
        prices[
            ["store_id", "item_id", "wm_yr_wk", "sell_price"]
        ],
        on=["store_id", "item_id", "wm_yr_wk"],
        how="left",
    )

    sales_long["date"] = pd.to_datetime(sales_long["date"])

    sales_long = sales_long.sort_values(
        ["store_id", "item_id", "date"]
    )

    return sales_long


if __name__ == "__main__":
    df = build_dataset()

    print("Dataset shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nMissing values:")
    print(df.isna().sum())
    print("\nSample:")
    print(df.head())



