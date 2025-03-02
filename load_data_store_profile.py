import json
import psycopg2

# Function to connect to the Heroku PostgreSQL database
def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname="d6q1bvtlgb5786",
            user="u7m6p0im2iaf5d",
            password="p6aaebee5fe0c2d1a08cb291cea32482927c9029dcd1fbbcc6482a813f1131d3a",
            host="cav8p52l9arddb.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com",
            port="5432",
        )
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database.")
        print(e)
        return None

# Function to insert profile data into the store_profile table
def insert_profiles(conn, profiles):
    try:
        cur = conn.cursor()
        for profile in profiles:
            cur.execute("""
                INSERT INTO store_profile 
                (user_id, date_modified, phone, address1, address2, city, state, zipcode, country, old_cart) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                profile['user_id'], 
                profile['date_modified'], 
                profile['phone'], 
                profile['address1'], 
                profile['address2'], 
                profile['city'], 
                profile['state'], 
                profile['zipcode'], 
                profile['country'], 
                profile.get('old_cart')  # Use get() to allow for possible null values
            ))
        
        conn.commit()
        print("Profiles inserted successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting profiles.")
        print(e)

def load_data_from_json(file_path):
    conn = connect_to_database()
    if conn:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'profiles' in data:  # Check if 'profiles' key exists in the JSON data
                insert_profiles(conn, data['profiles'])
            else:
                print("No profile data found in JSON.")
        
        conn.close()

if __name__ == "__main__":
    load_data_from_json("data.json")
