import json
import codecs

file_n = codecs.open("js/input.json", "r", "utf_8_sig")
file_n_data = json.load(file_n)

file_m = codecs.open("js/massa.json", "r", "utf_8_sig")
file_m_data = json.load(file_m)

name = input("Введите имя:")
PHONE = '79631704420'


def phone_check():
    global PHONE
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
        print("Некорректный ввод. Вы уверены, что ввели число?")
        phone_check()
    PHONE = '7' + str(phone_select)

phone_check()
n_id = int(file_m_data["massa"]) + 1

new = {
    "id": n_id,
    "name": name,
    "number": PHONE
}

file_m_data.update({"massa": n_id})
file_n_data.append(new)

file_m.close()
file_n.close()

file_n = codecs.open("js/input.json", "w", "utf_8_sig")
file_m = codecs.open("js/massa.json", "w", "utf_8_sig")
file_m.close()
file_n.close()

file_n = codecs.open("js/input.json", "w", "utf_8_sig")
file_m = codecs.open("js/massa.json", "w", "utf_8_sig")

file_m.write(str(file_m_data).replace("'", '"'))
file_n.write(str(file_n_data).replace("'", '"'))

file_m.close()
file_n.close()

print("DONE")
