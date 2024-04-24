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

# Function to insert product data into the Product table
def insert_products(conn, products):
    try:
        cur = conn.cursor()
        for product in products:
            cur.execute("""
                INSERT INTO yourapp_product 
                (name, price, category_id, description, about_this_product, what_type, material, is_sale, sale_price,
                dimension_a, dimension_b, dimension_c, dimension_d) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                product['name'], product['price'], product['category_id'], product['description'],
                product['about_this_product'], product['what_type'], product['material'], product['is_sale'],
                product['sale_price'], product['dimension_a'], product['dimension_b'], product['dimension_c'],
                product['dimension_d']
            ))
            # Fetch the ID of the newly inserted product
            product_id = cur.fetchone()[0]

            # Insert colors for the product into the many-to-many table
            for color_id in product['colors']:
                cur.execute("""
                    INSERT INTO yourapp_product_colors (product_id, color_id) 
                    VALUES (%s, %s)
                """, (product_id, color_id))

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
            if 'products' in data:  # Check if 'products' key exists in the JSON data
                insert_products(conn, data['products'])
            else:
                print("No product data found in JSON.")
        
        conn.close()

if __name__ == "__main__":
    load_data_from_json("data.json")

