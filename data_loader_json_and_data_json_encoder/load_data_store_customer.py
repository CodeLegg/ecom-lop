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

# Function to insert customer data into the store_customer table
def insert_customers(conn, customers):
    try:
        cur = conn.cursor()
        for customer in customers:
            cur.execute("""
                INSERT INTO store_customer 
                (id, first_name, last_name, phone, email, password) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (customer['id'], customer['first_name'], customer['last_name'], customer['phone'], customer['email'], customer['password']))
        
        conn.commit()
        print("Customers inserted successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting customers.")
        print(e)

def load_data_from_json(file_path):
    conn = connect_to_database()
    if conn:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'customers' in data:  # Check if 'customers' key exists in the JSON data
                insert_customers(conn, data['customers'])
            else:
                print("No customer data found in JSON.")
        
        conn.close()

if __name__ == "__main__":
    load_data_from_json("data.json")

