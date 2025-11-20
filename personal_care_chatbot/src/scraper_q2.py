import requests
import pandas as pd

# Myntra Search API for Personal Care
API_URL = "https://www.myntra.com/gateway/v2/search/personal-care"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape_myntra_api():
    print("Fetching data from Myntra API...")

    response = requests.get(API_URL, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch data:", response.status_code)
        return []

    data = response.json()

    products = data["products"]  # Contains product list

    extracted = []

    for item in products:
        extracted.append({
            "brand": item.get("brand", "N/A"),
            "product_name": item.get("productName", "N/A"),
            "price": item.get("price", {}).get("discounted", "N/A"),
            "mrp": item.get("price", {}).get("mrp", "N/A"),
            "rating": item.get("rating", "N/A"),
            "ratingCount": item.get("ratingCount", "N/A"),
            "product_link": "https://www.myntra.com/" + item.get("landingPageUrl", "")
        })

    return extracted


def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("../data/myntra_scraped_q2.csv", index=False)
    print("Saved → ../data/myntra_scraped_q2.csv")


if __name__ == "__main__":
    products = scrape_myntra_api()
    print("Total products fetched:", len(products))
    save_to_csv(products)
    print("Scraping complete!")