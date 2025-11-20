# 🧴 Personal Care Chatbot – Assignment Q1 & Q2  
A complete solution for building a **Personal Care Chatbot** along with **Myntra product scraping**, as required in the assignment.

This repository contains both:
- **Q1 → Chatbot POC** (Dummy product dataset + Redirect logic + OpenAI LLM response + PostgreSQL table)
- **Q2 → Web Scraper** (Scrapes personal care products from Myntra)

---

## **Q1 – Chatbot Features**
### 1. Chatbot using OpenAI (LLM)
- Responds to user messages  
- Natural language responses  

### 2. Redirect Logic (Mandatory)
If the message contains:
- "offer"
- "discount"
- "return"
- "refund"
- "exchange"

→ The chatbot replies with the support contact number.

### 3. Product Search Using CSV
- Dummy personal-care product dataset  
- Supports keyword-based search (e.g., "lipstick", "face wash")  
- Returns top matching products  

### 4. PostgreSQL Integration
- Sample conversation table created  
- Sample rows inserted  
- Verified using pgAdmin  

---

## **Q2 – Web Scraping (Myntra)**
Scrapes personal care product data from Myntra including:
- Product Name  
- Price  
- Rating  
- Number of Reviews  
- Link  

Saved into:

personal_care_chatbot/
│
├── data/
│ ├── dummy_products_q1.csv
│ └── myntra_scraped_q2.csv
│
├── src/
│ ├── chatbot_poc.py
│ ├── create_dummy_data.py
│ ├── insert_conversations.py
│ └── scrape_myntra.py
│
├── README.md
└── .gitignore
