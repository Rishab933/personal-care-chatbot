import os
import pandas as pd
from openai import OpenAI

# Load API key
client = OpenAI(api_key="your_API_key")

# Customer support contact number
CONTACT = "+91-9999999999"

# Load product data (scraped or dummy)
data_path = "../data/myntra_products.csv"

if not os.path.exists(data_path):
    data_path = "../data/dummy_products_q1.csv"

df = pd.read_csv(data_path)

def check_redirect_query(msg):
    msg = msg.lower()
    keywords = ["offer", "offers", "discount", "return", "refund", "exchange"]
    return any(word in msg for word in keywords)

def search_product(query):
    query = query.lower()
    results = df[df["product_name"].str.lower().str.contains(query.split()[0], na=False)]
    if results.empty:
        return "No product found matching your query."

    response = "Top matching products:\n"
    for _, row in results.head(5).iterrows():
        response += f"- {row['product_name']} | Price: {row['price']}\n"
    return response

def ask_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"LLM Error: {str(e)}"

def chatbot():
    print("\n--- Personal Care Chatbot ---")
    print("Type 'exit' to quit.\n")
    while True:
        user_msg = input("You: ")
        if user_msg.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        if check_redirect_query(user_msg):
            print(f"Chatbot: Please contact our representative at {CONTACT}")
            continue
        if "lipstick" in user_msg.lower() or "product" in user_msg.lower():
            print("Chatbot:", search_product(user_msg))
            continue
        print("Chatbot:", ask_llm(user_msg))

if __name__ == "__main__":
    chatbot()
