import pyodbc
#import win32com.client as win32


# Connect to the SQL database using SQL authentication
conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-SOF46G0M;"
                      "Database=AdventureWorks2019;")
cursor = conn.cursor()

# Query the database to get the values you want
query = "select top 2 SS.UnitPrice From Sales.SalesOrderDetail SS where coNVERT(Date,  SS.ModifiedDate) ='2011-06-13'"
cursor.execute(query)
rows = cursor.fetchall()

if  rows:
    print("SQl Query exexuting....")
    for row in rows:
        message = int(row[0])
    if message == 0:
        print(f"Email{message}")
    else:
        print(f"Issue: {message}")
else:
    print("SQl Query exexuting Error....")
        # If there are any rows with a sum of 0, send an email using Microsoft Outlook
# if rows:
#     outlook = win32.Dispatch("Outlook.Application")
#     mail = outlook.CreateItem(0)
#     mail.To = "recipient@example.com"
#     mail.Subject = "Orders with a sum of 0"
#     message = "The following orders hadzzve a sum of 0:\n"
#     for row in rows:
#         message += f"Price: {row[0]}, Unit Price: {row[1]}\n"
#     mail.Body = message
#     mail.Send()

# Close the connection to the database
conn.close()
