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

# Function to insert product data into the Product table
def insert_products(conn, products):
    try:
        cur = conn.cursor()
        for product in products:
            cur.execute("""
                INSERT INTO store_product 
                (name, price, category_id, description, about_this_product, what_type, material, is_sale, sale_price,
                dimension_h, dimension_d, dimension_w, dimension_dff) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                product['name'], product['price'], product['category_id'], product['description'],
                product['about_this_product'], product['what_type'], product['material'], product['is_sale'],
                product['sale_price'], product['dimension_h'], product['dimension_d'], product['dimension_w'],
                product['dimension_dff']
            ))
        
        conn.commit()
        print("Products inserted successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting products.")
        print(e)

def load_data_from_json(file_path):
    conn = connect_to_database()
    if conn:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'product' in data:  # Check if 'product' key exists in the JSON data
                insert_products(conn, data['product'])
            else:
                print("No product data found in JSON.")
        
        conn.close()

if __name__ == "__main__":
    load_data_from_json("data.json")
