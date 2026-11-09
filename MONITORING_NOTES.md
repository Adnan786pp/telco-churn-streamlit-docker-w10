# Monitoring & Data Drift Notes

## 1. Data / Model Drift Description
* **Data Drift:** Real-world metrics shift (e.g., promotional campaigns pull in massive amounts of short term 'Month-to-month' contracts compared to stable baseline history).
* **Concept Drift:** Competitive marketplace behavior breaks original weights (e.g., customers charging higher fees leave significantly faster due to cheaper rival options).

## 2. Signals in Logs
* **Continuous Feature Shifts:** Rolling-window numeric average monitoring on `input_features.MonthlyCharges`.
* **Categorical Imbalance Tracking:** Tracking percentages of categorical metrics like `input_features.Contract`.
* **Output Skew Verification:** Spikes in output `predicted_probability` distribution profiles without clear seasonal trends.
