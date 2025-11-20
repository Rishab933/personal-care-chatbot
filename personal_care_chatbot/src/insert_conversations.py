import psycopg2
from psycopg2.extras import execute_values

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="personal_care_db",
    user="postgres",
    password="Rishab933@",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Sample conversations to insert
sample_data = [
    ("user_1", "What is the best lipstick for dry lips?", "You may try a moisturizing lipstick with shea butter."),
    ("user_2", "Do you have any offers on lipsticks?", "Please contact our customer representative at: +91-9999999999"),
    ("user_3", "How can I return a damaged product?", "For returns, please contact customer support at +91-9999999999")
]

# Insert multiple rows at once
query = """
    INSERT INTO conversations (user_id, user_message, ai_response)
    VALUES %s
"""

execute_values(cur, query, sample_data)

conn.commit()

cur.close()
conn.close()

print("Sample conversations inserted successfully!")
