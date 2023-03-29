# Execute multiple SQL query from folder and save as excel #

import os
import pyodbc
import pandas as pd
import datetime
import time

conn_str = 'Driver={SQL Server};Server=LAPTOP-SOF46G0M;DATABASE=AdventureWorks2014;Trusted_Connection=yes'
conn = pyodbc.connect(conn_str)

# Define folder path containing SQL scripts
script_folder = r'C:\Users\prash\Desktop\Project\SQLQuery'

# Loop through files in folder and run SQL scripts
for file in os.listdir(script_folder):
    if file.endswith('.sql'):
        script_path = os.path.join(script_folder, file)
        with open(script_path, 'r') as f:
            sql_script = f.read()
        try:
            # Execute SQL script and save results to DataFrame
            start_time = time.time()
            cursor = conn.cursor()
            cursor.execute(sql_script)
            data = cursor.fetchall()
            df = pd.DataFrame.from_records(data, columns=[column[0] for column in cursor.description])
            end_time = time.time()
            exec_time = end_time - start_time
            print(f'{file} executed successfully in {exec_time:.2f} seconds')
            # Export DataFrame to Excel file with timestamp in filename
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            output_file = os.path.join(script_folder, f'{file}_{timestamp}.xlsx')
            df.to_excel(output_file, index=False)
            print(f'Results exported to {output_file}')
        except pyodbc.Error as e:
            print(f'Error executing {file}: {e}')
# Close database connection
conn.close()
#
#
# inner.sql executed successfully in 10.91 seconds
# Results exported to C:\Users\prash\Desktop\Project\SQLQuery\inner.sql_2023-03-29_23-34-02.xlsx
# innerp.sql executed successfully in 9.94 seconds
# Results exported to C:\Users\prash\Desktop\Project\SQLQuery\innerp.sql_2023-03-29_23-34-17.xlsx