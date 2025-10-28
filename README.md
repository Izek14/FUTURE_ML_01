# 📈 Sales Forecasting Dashboard — Future Interns Project

This project was built as part of my **Future Interns** internship, where the task was to create a dashboard that predicts **future sales trends** based on historical retail data.

It combines **Python forecasting** and **Power BI visualization** to turn raw sales data into meaningful business insights.

---

## 🚀 Project Overview

**Goal:**  
Build a sales forecasting system that uses historical sales data to predict future trends and visualize them in an interactive Power BI dashboard.

**Key Features:**
- Forecast future sales using **Facebook Prophet**
- Display trends, seasonality, and predictions
- Merge historical and forecast data for Power BI
- Generate ready-to-use CSVs for reporting

---

## 🧠 Tools & Technologies

| Category | Tools |
|-----------|--------|
| Forecasting | Prophet |
| Data Handling | Pandas |
| Visualization | Power BI |
| Other | chardet, datetime, warnings, os |

---


## ⚙️ How It Works

1. **Load Data**  
   Reads your `superstore.csv` file safely using encoding detection.  

2. **Aggregate Sales**  
   Groups daily sales totals and prepares data for Prophet.

3. **Train Forecasting Model**  
   Uses Prophet with weekly and yearly seasonality enabled.

4. **Predict Future Sales**  
   Forecasts the next 15 days (configurable).

5. **Export Results**  
   Creates three CSVs — including a **Power BI-ready merged file** that combines historical and forecasted data.


---

## 📊 Sample Output

| Date | Sales | yhat | yhat_lower | yhat_upper |
|------|--------|------|-------------|-------------|
| 2024-01-01 | 482.4 | 478.9 | 432.1 | 528.6 |
| 2024-01-02 | 510.2 | 505.3 | 460.8 | 553.9 |
| 2024-01-03 | 495.1 | 499.7 | 452.3 | 548.0 |
| 2024-01-04 | 523.7 | 519.2 | 472.6 | 566.5 |
| 2024-01-05 | 538.4 | 533.5 | 487.9 | 581.7 |
| 2024-01-06 | 562.9 | 556.8 | 509.4 | 606.3 |
| 2024-01-07 | 545.3 | 541.1 | 494.2 | 589.5 |
| 2024-01-08 | 489.6 | 492.4 | 447.1 | 539.8 |
| 2024-01-09 | 507.8 | 503.9 | 457.5 | 550.4 |
| 2024-01-10 | 520.4 | 518.7 | 471.6 | 567.2 |

🟢 *`yhat`* represents Prophet’s forecasted value,  
while *`yhat_lower`* and *`yhat_upper`* form the prediction uncertainty interval.

---
## 🧾 Requirements

Install dependencies:
```bash
pip install prophet pandas chardet
