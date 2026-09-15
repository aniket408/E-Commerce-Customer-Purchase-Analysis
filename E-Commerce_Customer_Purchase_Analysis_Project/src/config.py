import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


RAW_DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "online_retail_II.xlsx"
)


PROCESSED_DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "cleaned_data.csv"
)


GRAPH_PATH = os.path.join(
    BASE_DIR,
    "outputs",
    "charts"
)


ANALYSYS_PATH = os.path.join(
    BASE_DIR,
    "outputs",
    "business_insights.txt"
)


REPORT_PATH = os.path.join(
    BASE_DIR,
    "outputs",
    "ecommerce_report.pdf"
)