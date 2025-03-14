import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration from environment variables
DB_HOST = os.getenv("DB_HOST")  
DB_USER = os.getenv("DB_USER")  
DB_PASSWORD = os.getenv("DB_PASSWORD")  # Example: "your_secure_password"
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", 3306))  # Example: "book_recommender"

# Establish connection to MySQL
def get_connection():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("✅ Connected to the database successfully!")  # Debugging line
        return connection
    except Exception as e:
        print(f"❌ Database Connection Error: {e}")
        return None

# Ensure the contacts table exists
def create_table():
    connection = get_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS contacts (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        message TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                connection.commit()
                print("✅ Contacts table verified/created successfully!")
        except Exception as e:
            print(f"❌ Error creating table: {e}")
        finally:
            connection.close()

# Insert contact details
def insert_contact(name, email, message):
    connection = get_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, email, message))
                connection.commit()
                print("✅ Contact saved successfully!")
        except Exception as e:
            print(f"❌ Error saving contact: {e}")
        finally:
            connection.close()

# Run table creation on script execution
if __name__ == "__main__":
    create_table()
