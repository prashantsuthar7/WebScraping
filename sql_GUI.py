##This APP use to select source folder SQL querys one by one and export into excel with dest folder
## with shwing progress bar

import os
import pyodbc
import pandas as pd
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class SqlScriptRunner:
    def __init__(self, script_folder, dest_folder):
        self.script_folder = script_folder
        self.dest_folder = dest_folder
        os.makedirs(self.dest_folder, exist_ok=True)
        self.conn_str = 'Driver={SQL Server};Server=LAPTOP-SOF46G0M;DATABASE=AdventureWorks2014;Trusted_Connection=yes'
        self.conn = pyodbc.connect(self.conn_str)

    def run_scripts(self, progress_bar):
        success_msgs = []
        error_msgs = []
        files = [file for file in os.listdir(self.script_folder) if file.endswith('.sql')]
        total_files = len(files)
        progress_bar["maximum"] = total_files
        for i, file in enumerate(files, 1):
            script_path = os.path.join(self.script_folder, file)
            with open(script_path, 'r') as f:
                sql_script = f.read()
            try:
                cursor = self.conn.cursor()
                cursor.execute(sql_script)
                df = pd.DataFrame.from_records(cursor.fetchall(), columns=[column[0] for column in cursor.description])
                output_file = os.path.join(self.dest_folder, f'{file}_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.xlsx')
                df.to_excel(output_file, index=False)
                success_msgs.append(f'{file} executed successfully and results exported to {output_file}')
            except pyodbc.Error as e:
                error_msgs.append(f'Error executing {file}: {e}')
            progress_bar["value"] = i
            progress_bar.update()
        self.conn.close()
        return success_msgs, error_msgs

def execute_scripts():
    script_folder = filedialog.askdirectory(title="Select Script Folder")
    if not script_folder:
        return
    dest_folder = filedialog.askdirectory(title="Select Destination Folder")
    if not dest_folder:
        return
    runner = SqlScriptRunner(script_folder, dest_folder)
    progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")
    progress_bar.pack(pady=10)
    success_msgs, error_msgs = runner.run_scripts(progress_bar)
    progress_bar.destroy()
    msg = "\n\n".join(success_msgs + error_msgs)
    if msg:
        messagebox.showinfo("Execution Results", msg)
    else:
        messagebox.showinfo("Execution Results", "No SQL scripts were found in the selected folder.")

def execute_with_input():
    script_folder = script_folder_entry.get()
    dest_folder = dest_folder_entry.get()
    if not script_folder or not dest_folder:
        messagebox.showwarning("Input Error", "Please enter both script and destination folders.")
        return
    runner = SqlScriptRunner(script_folder, dest_folder)
    progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")
    progress_bar.pack(pady=10)
    success_msgs, error_msgs = runner.run_scripts(progress_bar)
    progress_bar.destroy()
    msg = "\n\n".join(success_msgs + error_msgs)
    if msg:
        messagebox.showinfo("Execution Results", msg)
    else:
        messagebox.showinfo("Execution Results", "No SQL scripts were found in the selected folder.")

root = tk.Tk()
root.title("SQL Script Runner")

# Button to execute scripts using file dialog
tk.Button(root, text="EXECUTE WITH FILE DIALOG", command=execute_scripts).pack(pady=10)

# Entry fields to take user input for script and destination folders

script_folder_label = tk.Label(root, text="Script Folder: ")
script_folder_label.pack()
script_folder_entry = tk.Entry(root)
script_folder_entry.pack(pady=5)

dest_folder_label = tk.Label(root, text="Destination Folder: ")
dest_folder_label.pack()
dest_folder_entry = tk.Entry(root)
dest_folder_entry.pack(pady=5)

# Button to execute scripts using user input
tk.Button(root, text="EXECUTE WITH INPUT", command=execute_with_input).pack(pady=10)

root.mainloop()
