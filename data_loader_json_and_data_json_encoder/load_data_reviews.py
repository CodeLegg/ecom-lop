import json
import psycopg2

# Function to connect to the Heroku PostgreSQL database
def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname="dedvnlg0e4781j",
            user="jnkepkrrwcmpqc",
            password="965abad44a0344d66fe63349a982ce296bfce6928ddde2f94e6d3dfa2331074f",
            host="ec2-54-171-193-12.eu-west-1.compute.amazonaws.com",
            port="5432"
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

