import pandas as pd
from src.config import PROCESSED_DATA_PATH

def clean_data(df):

    df = df.copy()

    # Remove duplicates

    df = df.drop_duplicates()

    # clean column names
    df.columns = df.columns.str.strip()

    # Clean text columns

    text_columns = [

        "StockCode",
        "Description",
        "Country"
    ]

    for column in text_columns:
        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
        )

    # Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"],
        errors="coerce"
    )

    # Convert numeric columns
    numeric_columns = [
        "Quantity",
        "Price",
        "Customer ID"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Remove rows with missing Customer ID
    df = df.dropna(
        subset=["Customer ID"]
    )

    # Remove rows with missing Description
    df = df.dropna(
        subset=["Description"]
    )

    # Remove invalid dates
    df = df.dropna(
    subset=["InvoiceDate"]
    )

    # Remove invalid Quantity
    df = df[
        df["Quantity"] > 0
    ]

    # Remove invalid Price
    df = df[
        df["Price"] > 0
    ]

    # Create Sales column
    df["Sales"] = (
        df["Quantity"] * df["Price"]
    )

    # Reset index
    df = df.reset_index(
        drop=True
    )

    return df

def save_cleaned_data(df):

    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )