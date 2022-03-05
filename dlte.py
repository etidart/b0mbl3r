import sqlite3
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
selected_id = ''


def id_check():
    global selected_id
    selected_id = input("Введите id:")
    try:
        selected_id = int(selected_id)
    except:
        print("\033[31mНеверный ввод. Повторите попытку\033[0m")
        id_check()
    cur.execute(f"SELECT * FROM numbers WHERE id='{str(selected_id)}'")
    fetch = cur.fetchall()
    if fetch == []:
        print("\033[31mНеверный ввод. Повторите попытку\033[0m")
        id_check()
    else:
        print("ID: " + str(fetch[0][0]) + '\nИМЯ: ' + str(fetch[0][1]) + '\nНОМЕР: +' + str(fetch[0][2]))
        check_agreement = input("Введите YES или NO\nВы хотите продолжить?")
        if check_agreement == "YES":
            return
        elif check_agreement == "NO":
            quit()
        else:
            print("\033[31mНеверный ввод. Повторите попытку\033[0m")
            id_check()


id_check()
# updating db
cur.execute(f"DELETE FROM numbers WHERE id='{selected_id}';")
conn.commit()

print("\033[32mDONE\033[0m")
