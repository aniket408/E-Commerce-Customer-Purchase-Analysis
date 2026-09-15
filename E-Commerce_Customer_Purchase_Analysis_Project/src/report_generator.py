import os

import pandas as pd

from reportlab.lib.pagesizes import A4

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib import colors

from src.config import GRAPH_PATH


def create_report(
    df,
    analysis,
    output_path
):

    os.makedirs(
        output_path,
        exist_ok=True
    )


    # Requirement 1: Clean Dataset

    clean_dataset_path = os.path.join(
        output_path,
        "cleaned_dataset.csv"
    )

    df.to_csv(
        clean_dataset_path,
        index=False
    )


    # Requirement 2: Statistical Summary

    statistical_summary = (
        df.describe()
        .transpose()
    )

    statistical_summary_path = os.path.join(
        output_path,
        "statistical_summary.csv"
    )

    statistical_summary.to_csv(
        statistical_summary_path
    )


    # Requirement 3: Business Insights Report

    insights_path = os.path.join(
        output_path,
        "business_insights.txt"
    )

    with open(
        insights_path,
        "w",
        encoding="utf-8"
    ) as file:

        for key, value in analysis.items():

            if isinstance(
                value,
                float
            ):

                value = round(
                    value,
                    2
                )

            file.write(
                f"{key}: {value}\n"
            )


    # Requirement 4: PDF Report

    pdf_path = os.path.join(
        output_path,
        "ecommerce_report.pdf"
    )

    document = SimpleDocTemplate(
        pdf_path,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    story = []


    # Title

    story.append(
        Paragraph(
            "E-Commerce EDA Report",
            styles["Title"]
        )
    )

    story.append(
        Spacer(
            1,
            20
        )
    )


    # Business Insights

    story.append(
        Paragraph(
            "Business Insights",
            styles["Heading2"]
        )
    )

    story.append(
        Spacer(
            1,
            10
        )
    )


    for key, value in analysis.items():

        if isinstance(
            value,
            float
        ):

            value = round(
                value,
                2
            )

        text = (
            f"<b>{key}:</b> {value}"
        )

        story.append(
            Paragraph(
                text,
                styles["Normal"]
            )
        )

        story.append(
            Spacer(
                1,
                8
            )
        )


    # Requirement 5: Statistical Summary in PDF

    story.append(
        Paragraph(
            "Statistical Summary",
            styles["Heading2"]
        )
    )

    story.append(
        Spacer(
            1,
            10
        )
    )


    summary_data = [

        [
            "Column",
            "Mean",
            "Min",
            "Max"
        ]

    ]


    for column in statistical_summary.index:

        mean_value = (
            statistical_summary.loc[
                column,
                "mean"
            ]
        )

        min_value = (
            statistical_summary.loc[
                column,
                "min"
            ]
        )

        max_value = (
            statistical_summary.loc[
                column,
                "max"
            ]
        )


        # Handle numeric values

        if pd.api.types.is_numeric_dtype(
            df[column]
        ):

            mean_value = round(
                mean_value,
                2
            )

            min_value = round(
                min_value,
                2
            )

            max_value = round(
                max_value,
                2
            )


        # Handle datetime values

        else:

            mean_value = str(
                mean_value
            )

            min_value = str(
                min_value
            )

            max_value = str(
                max_value
            )


        summary_data.append(

            [
                column,
                mean_value,
                min_value,
                max_value
            ]

        )


    summary_table = Table(
        summary_data
    )


    summary_table.setStyle(

        TableStyle(

            [

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.grey
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.black
                ),

                (
                    "ALIGN",
                    (1, 1),
                    (-1, -1),
                    "RIGHT"
                )

            ]

        )

    )


    story.append(
        summary_table
    )

    story.append(
        Spacer(
            1,
            20
        )
    )


    # Requirement 6: Charts in PDF

    story.append(
        Paragraph(
            "Data Visualizations",
            styles["Heading2"]
        )
    )

    story.append(
        Spacer(
            1,
            10
        )
    )


    chart_names = [

        "monthly_sales.png",

        "product_category.png",

        "revenue_histogram.png",

        "customer_spending.png",

        "scatter_plot.png",

        "pie_chart.png",

        "box_plot.png",

        "heatmap.png",

        "pair_plot.png",

        "top_customers.png"

    ]


    for chart_name in chart_names:

        chart_path = os.path.join(
            GRAPH_PATH,
            chart_name
        )


        if os.path.exists(
            chart_path
        ):

            story.append(

                Image(
                    chart_path,
                    width=450,
                    height=300
                )

            )

            story.append(

                Spacer(
                    1,
                    15
                )

            )


    # Generate PDF

    document.build(
        story
    )


    print(
        "Report generated successfully!"
    )