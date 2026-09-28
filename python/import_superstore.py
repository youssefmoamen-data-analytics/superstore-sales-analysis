# Import Libarays
import os
from dotenv import load_dotenv
import pandas as pd
import mysql.connector 
from mysql.connector import Error
from sqlalchemy import create_engine


# Resolve the project root folder (one level above /python)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables from the .env file in the project root
load_dotenv(os.path.join(BASE_DIR, ".env"))


# ============================================================
# OLD APPROACH: Manual mysql.connector method (kept for learning reference)
# ============================================================

# try:
#     connection = mysql.connector.connect(
#         host= os.getenv("DB_HOST"),
#         user = os.getenv("DB_USER"),
#         password = os.getenv("DB_PASSWORD")
#     )

#     if connection.is_connected():
#         # Sanity Check      
#         print("Connceted to MySQL Successfuly!")

#         cursor = connection.cursor()

#         # Create the DataBase if it doesn't already exist
#         cursor.execute("CREATE DATABASE IF NOT EXISTS superstore_db")

#         # Select the DataBase to work inside
#         cursor.execute("USE superstore_db")

#         # Delete th table if it already exists (start fresh)
#         cursor.execute("DROP TABLE IF EXISTS sales")

#         # Create the sales table with proper column types
#         create_table_query = """
#         CREATE TABLE sales (
#             `Row ID` INT,
#             `Order ID` VARCHAR(30),
#             `Order Date` DATE,
#             `Ship Date` DATE,
#             `Ship Mode` VARCHAR(50),
#             `Customer ID` VARCHAR(30),
#             `Customer Name` VARCHAR(100),
#             `Segment` VARCHAR(50),
#             `Country` VARCHAR(100),
#             `City` VARCHAR(100),
#             `State` VARCHAR(100),
#             `Postal Code` VARCHAR(20),
#             `Region` VARCHAR(50),
#             `Product ID` VARCHAR(30),
#             `Category` VARCHAR(50),
#             `Sub-Category` VARCHAR(50),
#             `Product Name` VARCHAR(500),
#             `Sales` DECIMAL(15,4),
#             `Shipping Duration` INT
#         )
#         """

#         cursor.execute(create_table_query)

#         # convert data columns to proper data fromat (without time)
#         df["Order Date"] = pd.to_datetime(df['Order Date']).dt.date
#         df["Ship Date"] = pd.to_datetime(df['Ship Date']).dt.date

#         # Replace missing values (NaN) with None, because MySQL understands
#         # None as NULL, but doesn't understand pandas' NaN
#         df = df.astype(object).where(pd.notna(df), None) 

#         # SQL query template for inserting one row of data
#         insert_query = """
#         INSERT INTO sales (
#             `Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`,
#             `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`,
#             `State`, `Postal Code`, `Region`, `Product ID`, `Category`,
#             `Sub-Category`, `Product Name`, `Sales`, `Shipping Duration`
#         )
#         VALUES (
#             %s, %s, %s, %s, %s,
#             %s, %s, %s, %s, %s,
#             %s, %s, %s, %s, %s,
#             %s, %s, %s, %s
#         )
#         """

#         # Convert the DataFrame rows into a list of tuples
#         data = list(df.itertuples(index=False, name=None))

#         # Insert all rows at once (executemany is much faster than a loop)
#         cursor.executemany(insert_query, data)
#         connection.commit()

#         print(f"Inserted {cursor.rowcount} rows successfully!")

# except Error as e:
#     print("MySQL Error:")
#     print(e)


# ============================================================
# NEW APPROACH: Short professional method using SQLAlchemy
# ============================================================

# Load the cleaned CSV file
# Build the CSV path relative to this script's location,
# so the code works no matter where the project folder is placed
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "cleaned_superstore.csv")

df = pd.read_csv(csv_path)

# Convert date columns (same reason as before - MySQL needs real DATE type)
df["Order Date"] = pd.to_datetime(df["Order Date"]).dt.date
df["Ship Date"] = pd.to_datetime(df["Ship Date"]).dt.date

# Build the connection string
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")

connection_string = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/superstore_db"
engine = create_engine(connection_string)

# Upload the DataFrame directly to MySQL (creates the table automatically)
df.to_sql("sales", engine, if_exists="replace", index=False)

print(f"Inserted {len(df)} rows successfully!")