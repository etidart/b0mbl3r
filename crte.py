import sqlite3
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from colorama import init as colorama_init

colorama_init()

# variables to work with sqlite 3
conn = sqlite3.connect('numbers.db')
cur = conn.cursor()

# create a table if not exists
cur.execute("""CREATE TABLE IF NOT EXISTS numbers(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   number TEXT NOT NULL)
""")
conn.commit()

# main
name = input("Введите имя:")
phone = '71234567890'


def phone_check():
    global phone
    selected_phone = input("Введите номер телефона без 7 или 8:")
    try:
        selected_phone = int(selected_phone)
    except:
        print("\033[31mНеверный ввод. Повторите попытку\033[0m")
        phone_check()
    is_phone = carrier._is_mobile(number_type(phonenumbers.parse(str(selected_phone), "RU")))
    if is_phone == True:
        phone = '7' + str(selected_phone)
    else:
        print("\033[31mНеверный ввод. Повторите попытку\033[0m")
        phone_check()


phone_check()

# inserting data to db
cur.execute(f"INSERT INTO numbers(name, number) VALUES ('{name}', '{phone}');")
conn.commit()

print("\033[32mDONE\033[0m")
