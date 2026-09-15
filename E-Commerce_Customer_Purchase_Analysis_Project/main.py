import os

from src.config import (
    PROCESSED_DATA_PATH,
    GRAPH_PATH,
    ANALYSYS_PATH,
    REPORT_PATH
)

from src.data_loader import (
    load_data
)

from src.data_cleaning import (
    clean_data,
    save_cleaned_data
)

from src.data_transformation import (
    transform_data
)

from src.data_analysis import (
    explore_dataset,
    generate_analysis,
    save_business_insights
)

from src.data_visualization import (
    create_visualization
)

from src.report_generator import (
    create_report
)


def main():

    # Requirement 1: Load Dataset

    print("Loading data...")

    df = load_data()


    # Requirement 2: Explore Dataset

    print("Exploring dataset...")

    explore_dataset(df)


    # Requirement 3: Clean Dataset

    print("Cleaning data...")

    df = clean_data(df)

    save_cleaned_data(df)


    # Requirement 4: Transform Data

    print("Transforming data...")

    df = transform_data(df)


    # Requirement 5: Generate Analysis

    print("Generating analysis...")

    analysis = generate_analysis(df)


    # Requirement 6: Save Business Insights

    print("Saving business insights...")

    os.makedirs(
        os.path.dirname(ANALYSYS_PATH),
        exist_ok=True
    )

    save_business_insights(
        analysis,
        ANALYSYS_PATH
    )


    # Requirement 7: Create Visualizations

    print("Creating visualizations...")

    os.makedirs(
        GRAPH_PATH,
        exist_ok=True
    )

    create_visualization(
        df,
        GRAPH_PATH
    )


    # Requirement 8: Create PDF Report

    print("Creating PDF Report...")

    os.makedirs(
        os.path.dirname(REPORT_PATH),
        exist_ok=True
    )

    create_report(
        df,
        analysis,
        os.path.dirname(REPORT_PATH)
    )


    # Project Completed

    print(
        "\nE-Commerce EDA Completed Successfully!"
    )


if __name__ == "__main__":

    main()