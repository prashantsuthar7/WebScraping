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

##############################################
# import os
# import glob
# import pandas as pd
# from datetime import date, timedelta
#
# source_folder_path = r'P:\D Drive\1_Source'
# destination_folder_path = r'P:\D Drive\2_Dest'
#
# def create_directory():
#     today = date.today()
#     folder_name = today.strftime("%Y-%m-%d")
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)
#
# create_directory()
#
# os.chdir(source_folder_path)
#
# txt_files = sorted(glob.glob("*ChaseStatus_*.txt"), key=os.path.getmtime, reverse=True)
#
# for file in txt_files:
#     df = pd.read_csv(file, delimiter="|")
#     today = date.today()
#     year = today.strftime("%Y")
#     month = today.strftime("%b")
#     day = today.strftime("%Y%m%d")
#     filename = os.path.splitext(os.path.basename(file))[0] + '.xlsx'
#     file_path = os.path.join(destination_folder_path, year, month, day, filename)
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
#     df.to_excel(file_path, index=False)
#     print(f'Saved {file_path}')
#
# print('All files have been saved as Excel files.')
