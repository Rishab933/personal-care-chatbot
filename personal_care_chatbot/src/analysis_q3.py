import pandas as pd

DATA_PATH = "../data/myntra_scraped_q2.csv"
OUTPUT_PATH = "../data/q3_insights.csv"

def load_data():
    print("Loading dataset...")
    df = pd.read_csv(DATA_PATH)
    print(f"Total products loaded: {len(df)}\n")
    return df


def top_rated(df):
    print("Top 10 Highest Rated Products:\n")
    result = df.sort_values(by="rating", ascending=False).head(10)
    print(result[["brand", "product_name", "rating"]], "\n")
    return result


def most_affordable(df):
    print("Top 10 Most Affordable Products:\n")
    result = df.sort_values(by="price").head(10)
    print(result[["brand", "product_name", "price"]], "\n")
    return result


def value_for_money(df):
    print("Top 10 Best Value for Money (Rating / Price):\n")

    df["value_score"] = df["rating"] / df["price"]

    result = df.sort_values(by="value_score", ascending=False).head(10)
    print(result[["brand", "product_name", "rating", "price", "value_score"]], "\n")
    return result


def brand_distribution(df):
    print("Brand-wise Product Count:\n")
    result = df["brand"].value_counts().reset_index()
    result.columns = ["brand", "count"]

    print(result, "\n")
    return result


def save_all_insights(top_rated_df, affordable_df, value_df, brand_df):
    print("Saving insights to CSV...")

    # Add section labels for readability
    top_rated_df["section"] = "Top Rated"
    affordable_df["section"] = "Affordable"
    value_df["section"] = "Value for Money"
    brand_df["section"] = "Brand Count"

    # Combine everything
    final_df = pd.concat([top_rated_df, affordable_df, value_df, brand_df], ignore_index=True)

    final_df.to_csv(OUTPUT_PATH, index=False)
    print(f"Insights saved → {OUTPUT_PATH}\n")


if __name__ == "__main__":
    df = load_data()

    top_rated_df = top_rated(df)
    affordable_df = most_affordable(df)
    value_df = value_for_money(df)
    brand_df = brand_distribution(df)

    save_all_insights(top_rated_df, affordable_df, value_df, brand_df)

    print("Q3 Analysis Completed Successfully!")
