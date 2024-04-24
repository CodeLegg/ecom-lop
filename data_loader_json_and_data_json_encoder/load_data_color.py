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

# Function to insert color data into the Color table
def insert_colors(conn, colors):
    try:
        cur = conn.cursor()
        for color in colors:
            cur.execute("""
                INSERT INTO yourapp_color 
                (name, hex_code) 
                VALUES (%s, %s)
            """, (color['name'], color['hex_code']))
        
        conn.commit()
        print("Colors inserted successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting colors.")
        print(e)

def load_data_from_json(file_path):
    conn = connect_to_database()
    if conn:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'colors' in data:  # Check if 'colors' key exists in the JSON data
                insert_colors(conn, data['colors'])
            else:
                print("No color data found in JSON.")
        
        conn.close()

if __name__ == "__main__":
    load_data_from_json("data.json")

