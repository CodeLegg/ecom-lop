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

