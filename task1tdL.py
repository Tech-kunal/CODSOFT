import tkinter as tk
from tkinter import messagebox
import sqlite3
import ttkbootstrap as ttk

Database = 'TodoList.db'

def CreateConnection():
    conn  = None
    try:
        conn = sqlite3.connect(Database)
    except sqlite3.Error as e:
        print(e)
    return conn

def CreateTable():
    conn = CreateConnection()
    create_table_sql = """CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY,
                            task TEXT NOT NULL,
                            completed BOOLEAN NOT NULL
                          );"""
    try:
        X = conn.cursor()
        X.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def AddTask():
    task = TaskEntry.get()
    if task:
        conn =  CreateConnection()
        sql = '''INSERT INTO tasks(task, completed) VALUES(?,?)'''
        cur = conn.cursor()
        cur.execute(sql, (task, False))
        conn.commit()
        conn.close()
        TaskEntry.delete(0, tk.END)
        update_task_listbox()
    else:
        messagebox.showwarning("Input Error", "Please enter at least one task.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    conn = CreateConnection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    for row in rows:
        status = "completed ~ _ ~ " if row[2] else "Not completed ` - `"
        task_listbox.insert(tk.END, f"{row[1]} : {status}")
    conn.close()

def CompleteTask():
    try:
        selected_index = task_listbox.curselection()[0]
        conn = CreateConnection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
        task_id = rows[selected_index][0]
        sql = '''UPDATE tasks SET completed = ? WHERE id = ?'''
        cur.execute(sql, (True, task_id))
        conn.commit()
        conn.close()
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task that you have completed.")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        conn = CreateConnection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
        task_id = rows[selected_index][0]
        sql = '''DELETE FROM tasks WHERE id = ?'''
        cur.execute(sql, (task_id,))
        conn.commit()
        conn.close()
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

app = ttk.Window(themename="darkly")
app.title("To-Do List Maker")
app.geometry("700x400")

TaskEntry = ttk.Entry(app, width=100 )
TaskEntry.pack(pady=10)

add_button = ttk.Button(app, text="Add Task", command=AddTask, bootstyle="success")
add_button.pack(pady=5)

complete_button = ttk.Button(app, text="Complete Task", command=CompleteTask, bootstyle="primary")
complete_button.pack(pady=5)

delete_button = ttk.Button(app, text="Delete Task", command=delete_task, bootstyle="danger")
delete_button.pack(pady=5)

task_listbox = tk.Listbox(app, width=100, height=10, bg="black", fg="white")
task_listbox.pack(pady=10)

CreateTable()
update_task_listbox()

app.protocol("WM_DELETE_WINDOW", app.destroy)
app.mainloop()
