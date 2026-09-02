import os

import pandas as pd
import lightgbm as lgb

from sklearn.metrics import mean_absolute_error, mean_squared_error

from build_dataset import build_dataset
from features import create_features


RESULTS_DIR = "results"


def wape(actual, predicted):
    denominator = actual.abs().sum()

    if denominator == 0:
        return 0.0

    return (actual - predicted).abs().sum() / denominator


def prepare_data():
    df = build_dataset(n_items=30)
    df = create_features(df)

    df = df.dropna(
        subset=[
            "lag_1",
            "lag_7",
            "lag_28",
            "rolling_mean_7",
            "rolling_mean_28",
            "rolling_std_7",
            "target",
        ]
    )

    return df


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    df = prepare_data()

    cutoff = df["date"].max() - pd.Timedelta(days=28)

    train = df[df["date"] < cutoff].copy()
    test = df[df["date"] >= cutoff].copy()

    print("Train:", train.shape)
    print("Test:", test.shape)
    print("Cutoff:", cutoff.date())

    # ---------------------------------------------------------
    # Baseline
    # ---------------------------------------------------------

    baseline_pred = test["lag_7"]

    baseline_mae = mean_absolute_error(
        test["target"],
        baseline_pred,
    )

    baseline_rmse = mean_squared_error(
        test["target"],
        baseline_pred,
    ) ** 0.5

    baseline_wape = wape(
        test["target"],
        baseline_pred,
    )

    print("\n7-day baseline")
    print("MAE:", round(baseline_mae, 3))
    print("RMSE:", round(baseline_rmse, 3))
    print("WAPE:", round(baseline_wape * 100, 2), "%")

    # ---------------------------------------------------------
    # Keep original test information for predictions.csv
    # ---------------------------------------------------------

    test_metadata = test[
        [
            "date",
            "store_id",
            "item_id",
            "sell_price",
        ]
    ].copy()

    # ---------------------------------------------------------
    # Encode categorical variables
    # ---------------------------------------------------------

    categorical_columns = [
        "store_id",
        "item_id",
        "cat_id",
    ]

    train = pd.get_dummies(
        train,
        columns=categorical_columns,
    )

    test = pd.get_dummies(
        test,
        columns=categorical_columns,
    )

    train, test = train.align(
        test,
        join="left",
        axis=1,
        fill_value=0,
    )

    # ---------------------------------------------------------
    # Model features
    # ---------------------------------------------------------

    feature_columns = [
        "sell_price",
        "price_missing",
        "price_change",
        "day_of_week",
        "month",
        "weekend",
        "lag_1",
        "lag_7",
        "lag_28",
        "rolling_mean_7",
        "rolling_mean_28",
        "rolling_std_7",
    ]

    feature_columns += [
        col
        for col in train.columns
        if col.startswith("store_id_")
        or col.startswith("item_id_")
        or col.startswith("cat_id_")
    ]

    X_train = train[feature_columns]
    y_train = train["target"]

    X_test = test[feature_columns]
    y_test = test["target"]

    # ---------------------------------------------------------
    # LightGBM
    # ---------------------------------------------------------

    print("\nTraining LightGBM...")

    model = lgb.LGBMRegressor(
        objective="regression",
        n_estimators=300,
        learning_rate=0.05,
        num_leaves=31,
        subsample=0.8,
        colsample_bytree=0.8,
        reg_lambda=1.0,
        random_state=42,
        n_jobs=-1,
        verbosity=-1,
    )

    model.fit(
        X_train,
        y_train,
    )

    predictions = model.predict(X_test)

    # ---------------------------------------------------------
    # Evaluation
    # ---------------------------------------------------------

    mae = mean_absolute_error(
        y_test,
        predictions,
    )

    rmse = mean_squared_error(
        y_test,
        predictions,
    ) ** 0.5

    model_wape = wape(
        y_test,
        predictions,
    )

    improvement = (
        (baseline_mae - mae)
        / baseline_mae
        * 100
    )

    print("\nLightGBM")
    print("MAE:", round(mae, 3))
    print("RMSE:", round(rmse, 3))
    print("WAPE:", round(model_wape * 100, 2), "%")
    print(
        "MAE improvement:",
        round(improvement, 2),
        "%",
    )

    # ---------------------------------------------------------
    # Feature importance
    # ---------------------------------------------------------

    importance = pd.DataFrame(
        {
            "feature": feature_columns,
            "importance": model.feature_importances_,
        }
    )

    importance = importance.sort_values(
        "importance",
        ascending=False,
    )

    importance.to_csv(
        f"{RESULTS_DIR}/feature_importance.csv",
        index=False,
    )

    # ---------------------------------------------------------
    # Save predictions
    # ---------------------------------------------------------

    predictions_df = test_metadata.copy()

    predictions_df["actual_demand"] = y_test.values
    predictions_df["predicted_demand"] = predictions

    predictions_df.to_csv(
        f"{RESULTS_DIR}/predictions.csv",
        index=False,
    )

    # ---------------------------------------------------------
    # Save metrics
    # ---------------------------------------------------------

    metrics = pd.DataFrame(
        [
            {
                "model": "7_day_baseline",
                "mae": baseline_mae,
                "rmse": baseline_rmse,
                "wape": baseline_wape,
            },
            {
                "model": "lightgbm",
                "mae": mae,
                "rmse": rmse,
                "wape": model_wape,
            },
        ]
    )

    metrics.to_csv(
        f"{RESULTS_DIR}/metrics.csv",
        index=False,
    )

    # ---------------------------------------------------------
    # Print results
    # ---------------------------------------------------------

    print("\nTop features:")
    print(
        importance.head(10).to_string(
            index=False
        )
    )

    print("\nSaved:")
    print("results/metrics.csv")
    print("results/feature_importance.csv")
    print("results/predictions.csv")


if __name__ == "__main__":
    main()