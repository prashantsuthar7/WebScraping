import pyodbc
import pandas as pd
from tkinter import *
from tkinter import messagebox
from threading import Thread

class DatabaseConnector:
    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';Trusted_Connection=yes;')
            self.cursor = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute_query(self, query, *parameters):
        try:
            self.cursor.execute(query, parameters)
            return self.cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return []

class OrderDetailsApp:
    def __init__(self):
        self.window = None
        self.order_id_entry = None
        self.details_text = None
        self.db_connector = None

    def run(self):
        self.create_window()
        self.db_connector = DatabaseConnector('LAPTOP-SOF46G0M', 'AdventureWorks2019')
        self.db_connector.connect()
        self.window.mainloop()
        self.db_connector.disconnect()

    def create_window(self):
        self.window = Tk()
        self.window.title("Order Details")

        order_id_label = Label(self.window, text="Order IDs (comma-separated):")
        order_id_label.pack()

        self.order_id_entry = Entry(self.window)
        self.order_id_entry.pack()

        get_details_button = Button(self.window, text="Get Details", command=self.get_order_details)
        get_details_button.pack()

        export_button = Button(self.window, text="Export to Excel", command=self.export_to_excel)
        export_button.pack()

        self.details_text = Text(self.window, width=80, height=20)
        self.details_text.pack()

    def get_order_details(self):
        order_ids = self.order_id_entry.get().split(",")
        query = "SELECT SalesOrderID, OrderDate, Status FROM Sales.SalesOrderHeader WHERE SalesOrderID IN ({})".format(",".join("?" * len(order_ids)))
        rows = self.db_connector.execute_query(query, *order_ids)
        if rows:
            details = ""
            for row in rows:
                details += f"Order ID: {row[0]}\nOrder Date: {row[1]}\nStatus: {row[2]}\n...\n\n"
            self.details_text.delete(1.0, END)
            self.details_text.insert(END, details)
        else:
            messagebox.showinfo("Order Details", "No orders found.")

    def export_to_excel(self):
        order_ids = self.order_id_entry.get().split(",")
        query = "SELECT SalesOrderID, OrderDate, Status FROM Sales.SalesOrderHeader WHERE SalesOrderID IN ({})".format(",".join("?" * len(order_ids)))
        rows = self.db_connector.execute_query(query, *order_ids)
        if rows:
            data = []
            for row in rows:
                data.append({
                    "Order ID": row[0],
                    "Order Date": row[1],
                    "Status": row[2],
                })
            df = pd.DataFrame(data)
            df.to_excel("order_details.xlsx", index=False)
            messagebox.showinfo("Export Successful", "Order details exported to 'order_details.xlsx'.")
        else:
            messagebox.showinfo("Order Details", "No orders found.")

if __name__ == "__main__":
    app = OrderDetailsApp()
    app.run()
