import json
import psycopg2

# Function to connect to the Heroku PostgreSQL database
def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname="den9b9tvad93o1",
            user="uf8d9f44uh7ea7",
            password="p3b08ff647e260d41ab381b391ff47e5a11106a6a1d1e080aba96f64e56927041",
            host="cav8p52l9arddb.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com",
            port="5432",
        )
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database.")
        print(e)
        return None

# Function to insert review data into the Review table
def insert_reviews(conn, reviews):
    try:
        cur = conn.cursor()
        for review in reviews:
            cur.execute("""
                INSERT INTO yourapp_review 
                (product_id, user_id, text, star_rating, date_posted) 
                VALUES (%s, %s, %s, %s, %s)
            """, (
                review['product_id'], review['user_id'], review['text'], review['star_rating'],
                review['date_posted']
            ))

        conn.commit()
        print("Reviews inserted successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting reviews.")
        print(e)

def load_data_from_json(file_path):
    conn = connect_to_database()
    if conn:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'reviews' in data:  # Check if 'reviews' key exists in the JSON data
                insert_reviews(conn, data['reviews'])
            else:
                print("No review data found in JSON.")
        
        conn.close()

if __name__ == "__main__":
    load_data_from_json("data.json")

