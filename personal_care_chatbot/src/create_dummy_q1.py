import pandas as pd
import os

# Ensure data folder exists
os.makedirs("../data", exist_ok=True)

# Dummy sample products (for Question 1 only)
dummy_products = [
    {
        "product_name": "GlowCare Moisturizing Lipstick - Ruby Red",
        "price": "₹499",
        "rating": "4.3",
        "image_url": "",
        "product_url": "",
        "breadcrumbs": "Home/Personal Care/Lipstick"
    },
    {
        "product_name": "SilkMatte Lipstick - Bare Pink",
        "price": "₹399",
        "rating": "4.1",
        "image_url": "",
        "product_url": "",
        "breadcrumbs": "Home/Personal Care/Lipstick"
    },
    {
        "product_name": "Herbal Shine Lipstick - Coral",
        "price": "₹299",
        "rating": "4.0",
        "image_url": "",
        "product_url": "",
        "breadcrumbs": "Home/Personal Care/Lipstick"
    },
    {
        "product_name": "NightGloss Lipstick - Deep Plum",
        "price": "₹599",
        "rating": "4.5",
        "image_url": "",
        "product_url": "",
        "breadcrumbs": "Home/Personal Care/Lipstick"
    }
]

# Convert to DataFrame
df = pd.DataFrame(dummy_products)

# Save inside data folder
df.to_csv("../data/dummy_products_q1.csv", index=False)

print("Dummy dataset created successfully!")
print("Saved to: ../data/dummy_products_q1.csv")
