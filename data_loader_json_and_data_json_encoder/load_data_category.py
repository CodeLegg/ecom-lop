import json
import psycopg2

# Function to connect to the Heroku PostgreSQL database
def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname="dfeagreasi55ct",
            user="uaqmav8jf03usa",
            password="pdd448d82156efd5f15e36a35dd815b7d50ac05db2e46fffce1538db7c9bfca73",
            host="c7u1tn6bvvsodf.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database.")
        print(e)
        return None

# Function to insert category data into the store_category table
def insert_categories(conn, categories):
    try:
        cur = conn.cursor()
        for category in categories:
            cur.execute("""
                INSERT INTO store_category 
                (id, name, description, image) 
                VALUES (%s, %s, %s, %s)
            """, (category['id'], category['name'], category['description'], category['image']))
        
        conn.commit()
        print("Categories inserted successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting categories.")
        print(e)

def load_data_from_json(file_path):
    conn = connect_to_database()
    if conn:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'category' in data:  # Check if 'category' key exists in the JSON data
                insert_categories(conn, data['category'])
            else:
                print("No category data found in JSON.")
        
        conn.close()

if __name__ == "__main__":
    load_data_from_json("data.json")
