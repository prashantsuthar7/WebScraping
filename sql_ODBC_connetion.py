## select data from sql database
import pyodbc
import pandas as pd
import os
from datetime import datetime
from plyer import notification

con = pyodbc.connect(
     driver = '{ODBC Driver 17 for SQL Server}',
    host = 'LAPTOP-SOF46G0M\SQLEXPRESS',
    database = 'Northwind',
    trusted_connection = 'yes'
)

# SQL Command to read the data
sqlQuery = "select top 10 * from Customers"


# Getting the data from sql into pandas dataframe
df = pd.read_sql(sql = sqlQuery, con = con)

# # Export the data on the Desktop
df.to_csv(os.environ["userprofile"] + "\\Desktop\\Project\\" + "SQL_Data_" +
 datetime.now().strftime("%m-%d-%Y_%H%M%S")
         + ".csv", index = False)

# # Display Notifiction to User
notification.notify(title="Report Status!!!",
                   message=f"data has been successfully saved into Excel.\
                   \nTotal Rows: {df.shape[0]}\nTotal Columns: {df.shape[1]}",
                   timeout = 10)
