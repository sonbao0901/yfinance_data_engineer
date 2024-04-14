import pyodbc as odbc
import pandas as pd
#define server and database
server = 'DESKTOP-6LM94UI'
database = 'stock_db'
#connect to sql server
conn = odbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')