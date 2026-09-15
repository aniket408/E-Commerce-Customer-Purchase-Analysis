# E-Commerce Customer Purchase Analysis

## Project Overview

This project performs E-Commerce customer purchase analysis using Python, Pandas (EDA), data visualization, and automatic report generation.

## Dataset

Source dataset: `data/raw/online_retail_II.xlsx`

The supplied dataset contains 8 columns:
- Invoice
- StockCode
- Description
- Quantity
- InvoiceDate
- Price
- Customer ID
- Country

## Completed Analysis

- Dataset loading and exploration
- Missing value handling
- Duplicate removal
- Customer behavior analysis
- Monthly sales trend
- Historical Customer Lifetime Value (CLV)
- Top customer analysis
- Revenue analysis
- Product revenue performance
- Business insights
- 10 requested visualization outputs
- Clean dataset CSV
- Statistical summary CSV
- Business insights TXT report
- PDF report with charts and statistical summary

## Dataset-Based Limitations

- The dataset does not contain a `Category` column. Product category analysis is therefore not fabricated or inferred.
- The dataset does not contain product cost data. Actual product profitability cannot be calculated; product revenue performance is provided instead.
- CLV is reported as historical customer revenue. Predictive CLV would require additional assumptions/data such as margin, churn probability, and expected future lifespan.

## Run the Project

Activate the virtual environment, install dependencies from `requirements.txt`, and run:

```bash
python main.py
```

Generated files are stored in the `outputs/` folder.
