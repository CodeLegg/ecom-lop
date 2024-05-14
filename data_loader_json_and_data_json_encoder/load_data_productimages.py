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

# Function to insert product images into the store_productimage table
def insert_product_images(conn, product_images):
    try:
        cur = conn.cursor()
        for image in product_images:
            cur.execute("""
                INSERT INTO store_productimage 
                (id, product_id, image) 
                VALUES (%s, %s, %s)
            """, (image['id'], image['product_id'], image['image']))
        
        conn.commit()
        print("Product images inserted successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting product images.")
        print(e)

def load_data_from_json(file_path):
    conn = connect_to_database()
    if conn:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'productimage' in data:  # Check if 'productimage' key exists in the JSON data
                insert_product_images(conn, data['productimage'])
            else:
                print("No product image data found in JSON.")
        
        conn.close()

if __name__ == "__main__":
    load_data_from_json("data.json")
