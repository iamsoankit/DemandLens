from pathlib import Path

import pandas as pd


RAW_DATA = Path("data/raw")


def load_calendar():
    return pd.read_csv(RAW_DATA / "calendar.csv")


def load_sales():
    return pd.read_csv(RAW_DATA / "sales_train_validation.csv")


def load_prices():
    return pd.read_csv(RAW_DATA / "sell_prices.csv")


def prepare_calendar(calendar):
    calendar = calendar.copy()

    calendar["date"] = pd.to_datetime(calendar["date"])

    return calendar[
        [
            "date",
            "wm_yr_wk",
            "weekday",
            "wday",
            "month",
            "year",
            "event_name_1",
            "event_type_1",
            "snap_CA",
            "snap_TX",
            "snap_WI",
        ]
    ]

