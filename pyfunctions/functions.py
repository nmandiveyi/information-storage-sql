# Define a function that sets up a connection with 
# a remote SQL db

# import the necessary modules
import mysql.connector as mysqlc
from mysql.connector import Error
import pandas as pd

def connect_to_server(host_name, db_name, username, password):
    connectivity = None
    try:
        connection = mysqlc.connect(
            host = host_name,
            database = db_name,
            user = user_name,
            passwd = password
        )
        print("Success: connection to remote database establised")
    except Error as err:
        print(f"Error: '{err}'")

    return connectivity

def parse_query(connectivity, query):
    cursor = connectivity.cursor()
    try:
        cursor.execute(query)
        print("Query successfullty executed")
    except Error as err:
        print(f"Erroe: '{err}'")
