# Personal Care Chatbot – Assignment 
A complete solution for building a **Personal Care Chatbot** along with **Myntra product scraping**, as required in the assignment.

This repository contains both:
- **Q1 → Chatbot POC** (Dummy product dataset + Redirect logic + OpenAI LLM response + PostgreSQL table)
- **Q2 → Web Scraper** (Scrapes personal care products from Myntra)
- **Q3 → Insights** (Product Analysis & Insights of Myntra Scraped data)

### Folder Structure
``` 
personal_care_chatbot/
│
├── data/
│ ├── dummy_products_q1.csv
│ ├── myntra_scraped_q2.csv
│ └── q3_insights.csv
│
├── src/
│ ├── chatbot_poc.py
│ ├── create_dummy_data.py
│ ├── insert_conversations.py
│ ├── scraper_q2.py
│ └── analysis_q3.py
```

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

---

## **Q3 – Product Analysis & Insights**

Using the scraped dataset from Q2 (`scraper_q2.csv`), this part performs data analysis to generate meaningful insights.

### Files Involved
- `src/analysis_q3.py`
- `data/q3_insights.csv`

### Insights Generated
The script analyzes the dataset and produces:

1. **Top 10 Highest Rated Products**  
2. **Top 10 Most Affordable Products**  
3. **Top 10 Best Value-for-Money Products**  
    - Based on the formula:  
      `value_score = rating / price`
4. **Brand-wise Product Count**
5. **All insights saved into a single CSV file:** 



