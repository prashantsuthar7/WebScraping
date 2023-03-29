# import pyodbc
# import pandas as pd
# import datetime
#
# # Connect to SQL Server database
# con = pyodbc.connect("Driver={SQL Server};"
#                       "Server=LAPTOP-SOF46G0M;"
#                       "Database=AdventureWorks2014;")
# # Define stored procedure name and parameters
# stored_proc_name = '[dbo].[uspGetBillOfMaterials]'
# param1 = '2010-05-17'
# param2 = 717
#
# # Build dynamic SQL query with parameters
# sql_query = f"EXEC {stored_proc_name} @param1='{param2}', @param2={param1}"
#
# # Execute query and store results in pandas dataframe
# df = pd.read_sql(sql_query, con)
#
# # Create filename with datetime stamp
# filename = f'results_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.xlsx'
#
# # Export dataframe to Excel file
# df.to_excel(filename, index=False)
#
# # Close database connection
# con.close()

import pyodbc
import textwrap
import openpyxl

workbook = openpyxl.Workbook()
worksheet = workbook.active


cstring = 'Driver={SQL Server};Server=LAPTOP-SOF46G0M;DATABASE=AdventureWorks2014;Trusted_Connection=yes'
tsql =textwrap.dedent("""
SELECT top 2
    e.[BusinessEntityID]    ,p.[Title]    ,p.[FirstName]    ,p.[MiddleName]    ,p.[LastName]
    ,p.[Suffix]    ,e.[JobTitle]      ,pp.[PhoneNumber]
    ,pnt.[Name] AS [PhoneNumberType]
    ,ea.[EmailAddress]
    FROM [HumanResources].[Employee] e
    INNER JOIN [Person].[Person] p
    ON p.[BusinessEntityID] = e.[BusinessEntityID]
    INNER JOIN [Person].[BusinessEntityAddress] bea 
    ON bea.[BusinessEntityID] = e.[BusinessEntityID] 
    INNER JOIN [Person].[Address] a 
    ON a.[AddressID] = bea.[AddressID]
    INNER JOIN [Person].[StateProvince] sp 
    ON sp.[StateProvinceID] = a.[StateProvinceID]
    INNER JOIN [Person].[CountryRegion] cr 
    ON cr.[CountryRegionCode] = sp.[CountryRegionCode]
    LEFT OUTER JOIN [Person].[PersonPhone] pp
    ON pp.BusinessEntityID = p.[BusinessEntityID]
    LEFT OUTER JOIN [Person].[PhoneNumberType] pnt
    ON pp.[PhoneNumberTypeID] = pnt.[PhoneNumberTypeID]
    LEFT OUTER JOIN [Person].[EmailAddress] ea
    ON p.[BusinessEntityID] = ea.[BusinessEntityID]
    """)
conn = pyodbc.connect(cstring)
cursor = conn.cursor()
cursor.execute(tsql)
rows = cursor.fetchall()

details = []
for row in rows:
    details.append(list(row))
    #print(row, end='\n')
for r in details:
    worksheet.append(r)
    workbook.save('my_list.xlsx')

print(details)