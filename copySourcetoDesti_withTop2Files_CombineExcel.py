#copy top two lasted files from source folder and combine as excel save in destination folder
import os
import glob
import pandas as pd
import datetime

source_folder_path = r'D:\1_Source'
destination_folder_path = r'D:\2_Dest'

os.chdir(source_folder_path)

txt_files = sorted(glob.glob("*ChaseStatus_*.txt"), key=os.path.getmtime, reverse=True)

#file_list = glob.glob(folder_path + "/*ChaseStatu*.txt")

latest_files = txt_files[:2]

# print(source_folder_path)
# print(destination_folder_path)
# print(txt_files)
# print(latest_files)

dfs = []
for file in latest_files:
    df = pd.read_csv(file, delimiter="|")
    dfs.append(df)

combined_df = pd.concat(dfs)

current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
filename = f"ChaseStatus_{current_datetime}.xlsx"
file_path = os.path.join(destination_folder_path, filename)

combined_df.to_excel(file_path, index=False)
print('file has been uploaded on folder')