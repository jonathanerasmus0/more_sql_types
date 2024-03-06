import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Lancaster017!",
    host="localhost",
    
);

# Create a cursor object 
cursor = conn.cursor()


create_table_query = '''
CREATE TABLE site_user (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    uuid UUID,
    avatar BYTEA, 
    role VARCHAR(20), 
    birthdate DATE,
    siblings TEXT[], 
    availability TIME[], 
    site_settings JSONB, 
    created_on TIMESTAMP,
    active_for INTERVAL
);
'''

# Execute the SQL command
cursor.execute(create_table_query)

# Commit your changes in the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
