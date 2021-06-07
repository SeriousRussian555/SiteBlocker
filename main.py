# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
from tkinter import *

import pymysql.cursors
import time
from datetime import datetime as dt

connection = pymysql.connect(host='141.8.193.236',
                             user='f0537851_123',
                             password='123456',
                             db='f0537851_123',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
cur = connection.cursor()
cur.execute("SELECT * FROM website_list")
for website_list in cur.fetchall():
    print(website_list)

Window_host = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

def get_entry():
    print("Сайты заблокированы")
    with open(Window_host, "r+") as hostfile:
        hosts = hostfile.read()
        for site in website_list:
            if site not in hosts:
                hostfile.write(redirect + " " + site + "\n")

"""while(prefiks == 1):
    start_our = s_hour.get()
    end_our = e_hour.get()
    print("Сайты заблокированы")
    with open(Window_host, "r+") as hostfile:
        hosts = hostfile.read()
        for site in website_list:
            if site not in hosts:
                hostfile.write(redirect + " " + site + "\n")
    time.sleep(10)
while(prefiks == 0):
    with open(Window_host, "r+") as hostfile:
        hosts = hostfile.readlines()
        hostfile.seek(0)
        for host in hosts:
            if not any(site in host for site in website_list):
                hostfile.write(host)
        hostfile.truncate()
    print("Сайты разблокированы")
    time.sleep(10)"""

def delete_entry():
    s_hour.delete('0', 'end')
    e_hour.delete('0', 'end')

def add_value():
    textbox.delete('1.0', 'end')
    cur = connection.cursor()
    cur.execute("SELECT * FROM website_list")
    rows = cur.fetchall()
    for row in rows:
        textbox.insert(1.0, row)
        textbox.insert(1.0, '\n')

def unblock():
    with open(Window_host, "r+") as hostfile:
        hosts = hostfile.readlines()
        hostfile.seek(0)
        for host in hosts:
            if not any(site in host for site in website_list):
                hostfile.write(host)
                hostfile.truncate()
    print("Сайты разблокированы")

def quit():
    global window
    window.destroy()

window = Tk()
h = 1000
w = 300
photo = tk.PhotoImage(file = 'nam.png')
window.iconphoto(False, photo)
window.title("Блокировщик сайтов")
window.geometry(f"{h}x{w}+200-50")
window.minsize(500, 600)
window.maxsize(1000, 1200)
window.resizable(True, True)

'''while True:
    if (
            dt(dt.now().year, dt.now().month, dt.now().day, start_our)
            < dt.now()
            < dt(dt.now().year, dt.now().month, dt.now().day, end_our)
    ):
        print("Сайты заблокированы")
        with open(Window_host, "r+") as hostfile:
            hosts = hostfile.read()
            for site in website_list:
                if site not in hosts:
                    hostfile.write(redirect + " " + site + "\n")
    else:
        with open(Window_host, "r+") as hostfile:
            hosts = hostfile.readlines()
            hostfile.seek(0)
            for host in hosts:
                if not any(site in host for site in website_list):
                    hostfile.write(host)
                    hostfile.truncate()
        print("Сайты разблокированы")
        time.sleep(10)'''

textFrame = Frame(window, height = 150)

textbox = Text(textFrame)
scrollbar = Scrollbar(textFrame)

bttn2 = Button(window, text = "Показать список сайтов",
               command = add_value).grid(row = 0, column = 0, sticky = 'we')

bttn1 = Button(window, text = "Выход",
               command = quit).grid(row = 0, column = 2, sticky = 'we')

bttn3 = Button(window, text = "Заблокировать",
               command = get_entry).grid(row = 0, column = 1, sticky = 'we')

bttn4 = Button(window, text = "Разблокировать",
               command = unblock).grid(row = 1, column = 1, sticky = 'we')

bttn5 = Button(window, text = "Очистить поля",
               command = delete_entry).grid(row = 3, column = 2, sticky = 'we')

tk.Label(window, text = 'Время начала').grid(row = 2, column = 0)
s_hour = tk.Entry(window)
s_hour.grid(row = 2, column = 1)

tk.Label(window, text = 'Время конца').grid(row = 3, column = 0)
e_hour = tk.Entry(window)
e_hour.grid(row = 3, column = 1)

textFrame.grid()
textbox.grid()

value_s = s_hour.get()
value_e = e_hour.get()

window.mainloop()
start_our = 8
end_our = 23