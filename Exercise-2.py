# NOTE CHRIS THAT THIS CODE IS GIVING ME SO MANY ERRORS WHEN I RUN IT SO I GAVE UP!

import psycopg2
import json
from datetime import datetime

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Lancaster017!",
    host="localhost",
)

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Define the SQL statement for creating the site_user table
create_table_query = '''
CREATE TABLE site_user_1 (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    uuid UUID,
    avatar BYTEA,
    role VARCHAR(20),
    birthdate DATE,
    siblings TEXT[],
    availability TIME[],
    site_settings JSONB,
    created_on TIMESTAMP
);
'''

# Execute the SQL command to create the table
cursor.execute(create_table_query)

# Sample data for the site_settings field
site_settings_data_1 = {"background": "red", "notifications": False}
site_settings_data_2 = {"notifications": True}

# Convert the dictionaries to JSON strings
site_settings_json_1 = json.dumps(site_settings_data_1)
site_settings_json_2 = json.dumps(site_settings_data_2)

## Example of inserting data into the database

# **Corrected insert query:**
insert_query = """
    INSERT INTO site_user (name, uuid, role, birthdate, siblings, availability, site_settings, created_on)
    VALUES (%s, %s, %s, %s, %s, %s::TIME, %s, %s)
"""

# Function to convert time strings to time objects (if needed)
def convert_time_string(time_str):
    # Convert time string to time object (if necessary)
    # Replace with your specific time string conversion logic if needed
    return datetime.strptime(time_str, "%H:%M:%S").time()

# Data to insert with converted time objects (if needed)
data_to_insert = [
    ("Miriam Valira", "e41e1291-33b8-4316-8a86-28a618d5c338", "Admin", datetime(1995, 8, 29), ["Dani", "Louis"], [convert_time_string(t) for t in ['12:00:00', '15:00:00']], site_settings_json_1, datetime(2015, 9, 23, 8, 56)),
    ("Johann Müller", "d81331bf-a4f6-4ecd-8883-51dee509309e", "User", datetime(2002, 5, 9), [], [convert_time_string(t) for t in ['09:00:00', '14:00:00', '18:00:00', '20:00:00']], site_settings_json_2, datetime(2017, 5, 1, 13, 3)),
    ("Louise Clark", "e6168ec9-7306-44a5-9875-2c659e15740e", "Moderator", datetime(1992, 5, 3), ["Monique"], [convert_time_string(t) for t in ['09:00:00', '12:00:00', '13:00:00', '17:00:00']], site_settings_json_2, datetime(2007, 3, 21, 10, 31))
]

# Execute the insert queries once
for data in data_to_insert:
    cursor.execute(insert_query, data)

#
