# Import the MySQL connector library
import mysql.connector

# Connect to MySQL server (replace 'YOUR_MYSQL_PASSWORD' with your actual password)
connection = mysql.connector.connect(
    host="localhost",  # MySQL server is running on the local machine
    user="root",       # MySQL username
    password="passkb@123"  # MySQL password
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute SQL command to create the database if it does not exist
cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

# Print success message
print("Database 'alx_book_store' created successfully!")

# Close the cursor
cursor.close()

# Close the connection
connection.close()
