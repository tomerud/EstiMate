import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="112145",
    port=3306,
    database="cities"
)

# Create a cursor object
cursor = conn.cursor()

# SQL query to create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS top_touristic_cities (
    city VARCHAR(100) PRIMARY KEY,
    country VARCHAR(100),
    continent VARCHAR(100),
    language VARCHAR(100),
    religion VARCHAR(100),
    human_development_index FLOAT,
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6)
);
"""

# Execute the query to create the table
cursor.execute(create_table_query)

# Commit changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Table 'top_touristic_cities' created successfully.")
