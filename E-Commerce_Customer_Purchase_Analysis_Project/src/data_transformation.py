def transform_data(df):
    df = df.copy()

    # Revenue
    df["Revenue"] = df["Quantity"] * df["Price"]

    # Date features
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    df["Month_Name"] = df["InvoiceDate"].dt.month_name()
    df["Quarter"] = df["InvoiceDate"].dt.quarter
    df["Day"] = df["InvoiceDate"].dt.day
    df["Day_Name"] = df["InvoiceDate"].dt.day_name()

    # Cancellation flag
    df["Is_Cancelled"] = (
        df["Invoice"].astype(str).str.startswith("C")
    )

    return df
