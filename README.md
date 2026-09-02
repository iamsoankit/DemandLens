# QuickCart — Retail Demand Forecasting & Pricing Analysis

A demand forecasting and pricing analysis project built on historical retail sales data.

The project focuses on predicting short-term item-level demand across stores and using the forecasts to explore pricing scenarios under different demand-sensitivity assumptions.

## Why this project

Retail demand changes across products, stores, weekdays, seasons, and prices. A useful forecasting system needs to capture these patterns while providing a simple way to translate predictions into business decisions.

This project covers:

- Demand forecasting at store-item level
- Time-based feature engineering
- Baseline vs. machine learning evaluation
- Price-demand analysis
- Revenue sensitivity under different pricing assumptions

## Dataset

The project uses the [M5 Forecasting](https://www.kaggle.com/competitions/m5-forecasting-accuracy) retail sales dataset.

The dataset contains daily unit sales across products and stores, along with calendar information and historical selling prices.

For local development, the pipeline works with a configurable subset of products.

Raw CSV files are intentionally excluded from the repository.

Expected files:

```text
data/raw/
├── calendar.csv
├── sales_train_validation.csv
└── sell_prices.csv
