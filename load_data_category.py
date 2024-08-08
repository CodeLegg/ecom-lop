import json
import psycopg2


# Function to connect to the PostgreSQL database
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


# Function to insert category data into the store_category table
def insert_categories(conn, categories):
    try:
        cur = conn.cursor()
        for category in categories:
            cur.execute(
                """
                INSERT INTO store_category 
                (id, name, parent_category_id, image, category_type, hierarchy_level) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """,
                (
                    category["id"],
                    category["name"],
                    category.get(
                        "parent_category_id"
                    ),  # Use get() to handle missing 'parent_category_id' gracefully
                    category["image"],
                    category["category_type"],
                    category.get(
                        "hierarchy_level", 0
                    ),  # Use get() to handle missing 'hierarchy_level' gracefully
                ),
            )

        conn.commit()
        print("Categories inserted successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting categories.")
        print(e)


def load_data_from_json(file_path):
    conn = connect_to_database()
    if conn:
        with open(file_path, "r") as file:
            data = json.load(file)
            if "category" in data:  # Check if 'category' key exists in the JSON data
                insert_categories(conn, data["category"])
            else:
                print("No category data found in JSON.")

        conn.close()


if __name__ == "__main__":
    load_data_from_json("data.json")
