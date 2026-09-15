import os

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def create_visualization(df, output_path):
    os.makedirs(output_path, exist_ok=True)

    # Requirement 1: Monthly Sales Trend
    monthly_revenue = (
        df.groupby(["Year", "Month", "Month_Name"])["Revenue"]
        .sum()
        .reset_index()
        .sort_values(["Year", "Month"])
    )

    monthly_revenue["Month_Year"] = (
        monthly_revenue["Month_Name"] + "-" + monthly_revenue["Year"].astype(str)
    )

    plt.figure(figsize=(10, 5))
    plt.plot(
        monthly_revenue["Month_Year"],
        monthly_revenue["Revenue"],
        marker="o",
    )
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "monthly_sales.png"))
    plt.close()

    # Requirement 2: Product Category Bar Chart
    # Dataset does not contain a Category column, so no artificial categories are created.
    if "Category" in df.columns:
        category_revenue = (
            df.groupby("Category")["Revenue"]
            .sum()
            .sort_values(ascending=False)
        )

        plt.figure(figsize=(10, 5))
        category_revenue.plot(kind="bar")
        plt.title("Revenue by Product Category")
        plt.xlabel("Product Category")
        plt.ylabel("Revenue")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(output_path, "product_category.png"))
        plt.close()
    else:
        # Keep an explanatory chart for the requested output while preserving data integrity.
        plt.figure(figsize=(10, 5))
        plt.axis("off")
        plt.text(
            0.5,
            0.5,
            "Product Category data is not available\nin the supplied dataset.",
            ha="center",
            va="center",
            fontsize=16,
        )
        plt.title("Product Category Analysis")
        plt.tight_layout()
        plt.savefig(os.path.join(output_path, "product_category.png"))
        plt.close()

    # Requirement 3: Revenue Histogram
    plt.figure(figsize=(8, 5))
    plt.hist(df["Revenue"].dropna(), bins=30)
    plt.title("Revenue Distribution")
    plt.xlabel("Revenue")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "revenue_histogram.png"))
    plt.close()

    # Requirement 4: Customer Spending Distribution
    customer_spending = (
        df.groupby("Customer ID")["Revenue"].sum().dropna()
    )

    plt.figure(figsize=(8, 5))
    plt.hist(customer_spending, bins=30)
    plt.title("Customer Spending Distribution")
    plt.xlabel("Customer Spending")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "customer_spending.png"))
    plt.close()

    # Requirement 5: Scatter Plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="Quantity", y="Price")
    plt.title("Quantity vs Price")
    plt.xlabel("Quantity")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "scatter_plot.png"))
    plt.close()

    # Requirement 6: Pie Chart
    country_revenue = (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(8, 8))
    plt.pie(
        country_revenue,
        labels=country_revenue.index,
        autopct="%1.1f%%",
    )
    plt.title("Revenue by Top 5 Countries")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "pie_chart.png"))
    plt.close()

    # Requirement 7: Box Plot
    plt.figure(figsize=(8, 5))
    plt.boxplot(df["Revenue"].dropna())
    plt.title("Revenue Box Plot")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "box_plot.png"))
    plt.close()

    # Requirement 8: Heatmap
    correlation = df[["Quantity", "Price", "Revenue"]].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "heatmap.png"))
    plt.close()

    # Requirement 9: Pair Plot
    pair_data = df[["Quantity", "Price", "Revenue"]].dropna()
    pair_data = pair_data.sample(min(1000, len(pair_data)), random_state=42)
    axes = pd.plotting.scatter_matrix(
        pair_data,
        figsize=(10, 10),
        diagonal="hist"
    )
    plt.suptitle("Pair Plot", y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "pair_plot.png"))
    plt.close("all")

    # Requirement 10: Top Customer Chart
    top_customers = (
        df.groupby("Customer ID")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 5))
    top_customers.plot(kind="bar")
    plt.title("Top 10 Customers")
    plt.xlabel("Customer ID")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "top_customers.png"))
    plt.close()

    print("All visualizations created successfully!")
