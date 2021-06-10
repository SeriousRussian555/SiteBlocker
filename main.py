# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
import tkinter.messagebox
from tkinter import *

from tkinter import messagebox
import MySQLdb
import pymysql
from tkinter import ttk

# connection = pymysql.connect(
#     host='141.8.193.236',
#     user='f0537851_123',
#     password='123456',
#     db='f0537851_123',
#     charset='utf8',
#     cursorclass=pymysql.cursors.DictCursor
# )
# print("успешное подключение")
# print("#" * 20)

connection = MySQLdb.connect('141.8.193.236', 'f0537851_123', '123456', 'f0537851_123')
cur = connection.cursor()
cur.execute("SELECT * FROM website_list")
for website_list in cur.fetchall():
    print(website_list)

Window_host = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

# # create table
# with connection.cursor() as cur:
#     create_table_query = "CREATE TABLE `website_list`(id int AUTO_INCREMENT," \
#                          "name varchar(50), PRIMARY KEY (id));"
#     cur.execute(create_table_query)
#     print("Таблица создана")

# insert data
# with connection.cursor() as cur:
#     insert_query = "INSERT INTO `website_list`(name) VALUES ('instagram.com');"
#     cur.execute(insert_query)
#     connection.commit()

# update data
# with connection.cursor() as cur:
#     update_query = "UPDATE `website_list` SET name = 'youtube.com' WHERE id = 1;"
#     cur.execute(update_query)
#     connection.commit()

# delete data
# with connection.cursor() as cur:
#     delete_query = "DELETE FROM `website_list` WHERE id = 2;"
#     cur.execute(delete_query)
#     connection.commit()

# select all data from table
# with connection.cursor() as cur:
#     sellect_all_rows = "SELECT * FROM `website_list`"
#     cur.execute(sellect_all_rows)
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#     print("#" * 20)

def ins_list():
    if entry.get()=='':
        tkinter.messagebox.showinfo('Предупреждение', 'Не оставляйте поле ввода пустым')
    else:
        with connection.cursor() as cur:
            insert_query = f"INSERT INTO `website_list`(name) VALUES ('{entry.get()}');"
            cur.execute(insert_query)
            connection.commit()
        lbox.insert(END, entry.get())
        entry.delete(0, END)

# def select_item(event):
#     value = (lbox.get(lbox.curselection()))
#     print(value)

def upd_list():
    if entry.get()=='':
        tkinter.messagebox.showinfo('Предупреждение', 'Не оставляйте поле ввода пустым')
#    elif lbox.curselection()[0]==' ':
#        tkinter.messagebox.showinfo('Предупреждение', 'Выбирите поле, которые хотите заменить')
    else:
        with connection.cursor() as cur:
            insert_query = f"UPDATE `website_list` SET name=('{entry.get()}') WHERE id=('{lbox.curselection()[0]+1}');"
            cur.execute(insert_query)
            connection.commit()
            sellect_all_rows = "SELECT name FROM `website_list`"
            cur.execute(sellect_all_rows)
            rows = cur.fetchall()
            lbox.delete(0, 'end')
            for row in rows:
                lbox.insert('end', row)
        entry.delete(0, END)

def upd_all():
    with connection.cursor() as cur:
        sellect_all_rows = "SELECT name FROM `website_list`"
        cur.execute(sellect_all_rows)
        rows = cur.fetchall()
        lbox.delete(0, 'end')
        for row in rows:
            lbox.insert('end', row)
    print("Данные обновлены")

def del_list():
    with connection.cursor() as cur:
        insert_query = f"DELETE FROM `website_list` WHERE id=('{lbox.curselection()[0]+1}');"
        cur.execute(insert_query)
        connection.commit()
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)

def search():
    if entry.get()=='':
        tkinter.messagebox.showinfo('Предупреждение', 'Введите значение, которое хотите найти')
    else:
        with connection.cursor() as cur:
            insert_query = f"SELECT (name) FROM `website_list` WHERE (name) LIKE ('%{entry.get()}%');"
            cur.execute(insert_query)
            rows = cur.fetchall()
            lbox.delete(0, 'end')
            for row in rows:
                lbox.insert('end', row)
        entry.delete(0, END)

def get_entry():
    print("Сайты заблокированы")
    with open(Window_host, "r+") as hostfile:
        hosts = hostfile.read()
        i=0
        for i in lbox.get(i, 'end'):
            for site in i:
                if site not in hosts:
                    hostfile.write(redirect + " " + site + "\n")

def unblock():
    cur = connection.cursor()
    cur.execute("SELECT name FROM website_list")
    with open(Window_host, "r+") as hostfile:
        hosts = hostfile.readlines()
        hostfile.seek(0)
        i=0
        for host in hosts:
            for i in lbox.get(i, 'end'):
                if not any(site in host for site in i):
                    hostfile.write(host)
                    hostfile.truncate()
    print("Сайты разблокированы")

def quit():
    connection.close()
    print("Подключение закрыто")
    window.destroy()

window = Tk()
h = 1000
w = 300
photo = tk.PhotoImage(file = 'nam.png')
window.iconphoto(False, photo)
window.title("Блокировщик сайтов")
window.geometry(f"{h}x{w}+500+150")
window.minsize(385, 355)
window.maxsize(385, 355)
window.resizable(True, True)

scrollbar = Scrollbar()

lbox = Listbox(width = 30, height = 15, yscrollcommand=scrollbar.set)
lbox.grid(row = 2, column = 1, columnspan=1, rowspan=3, sticky='sn')
# lbox.bind('<<ListboxSelect>>', select_item)

scrollbar.grid(row = 2, column = 2, rowspan=3, sticky='sn')
scrollbar.config(command=lbox.yview)

with connection.cursor() as cur:
    sellect_all_rows = "SELECT name FROM `website_list`"
    cur.execute(sellect_all_rows)
    rows = cur.fetchall()
    for row in rows:
        lbox.insert('end', row)

btn_add = tk.PhotoImage(file='plus.png')
bttn1 = Button(window, text = "Добавить",
               command = ins_list, compound=tk.TOP, image=btn_add).grid(row = 0, column = 0, rowspan=2, sticky = 'we')

btn_upd = tk.PhotoImage(file='pencil.png')
bttn2 = Button(window, text = "Редактировать",
               command = upd_list, compound=tk.TOP, image=btn_upd).grid(row = 2, column = 0, sticky = 'we')

btn_del = tk.PhotoImage(file='trash.png')
bttn3 = Button(window, text = "Удалить",
               command = del_list, compound=tk.TOP, image=btn_del).grid(row = 3, column = 0, sticky = 'we')

btn_len = tk.PhotoImage(file='lens.png')
bttn4 = Button(window, text = "Поиск",
               command = search, compound=tk.TOP, image=btn_len).grid(row = 4, column = 0, sticky = 'we')

btn_new = tk.PhotoImage(file='new.png')
bttn5 = Button(window, text = "Обновить",
               command = upd_all, compound=tk.TOP, image=btn_new).grid(row = 0, column = 3, rowspan=2, sticky = 'we')

btn_opn = tk.PhotoImage(file='locked.png')
bttn6 = Button(window, text = "Заблокировать",
               command = get_entry, compound=tk.TOP, image=btn_opn).grid(row = 2, column = 3, sticky = 'we')

btn_blc = tk.PhotoImage(file='opened.png')
bttn7 = Button(window, text = "Разблокировать",
               command = unblock, compound=tk.TOP, image=btn_blc).grid(row = 3, column = 3, sticky = 'we')

btn_exit = tk.PhotoImage(file='exit.png')
bttn8 = Button(window, text = "Выход",
               command = quit, compound=tk.TOP, image=btn_exit).grid(row = 4, column = 3, sticky = 'we')

tk.Label(window, text = 'Введите название сайта: ').grid(row = 0, column = 1, columnspan=2, sticky='we')
entry = tk.Entry(window)
entry.grid(row = 1, column = 1, columnspan=2, sticky='we')

window.mainloop()