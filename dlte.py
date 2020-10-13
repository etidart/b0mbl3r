import json
import codecs

file_n = codecs.open("js/input.json", "r", "utf_8_sig")
file_n_data = json.load(file_n)

file_m = codecs.open("js/massa.json", "r", "utf_8_sig")
file_m_data = json.load(file_m)

massa = int(file_m_data["massa"])

id_user = 0
id = 0

def phone_check():
    global id
    global id_user
    id_user = input("Введите id:")
    try:
        id_user = int(id_user)
    except:
        print("Некорректный ввод. Вы уверены, что ввели число?")
        phone_check()
    if int(id_user) >= 1 and int(id_user) <= massa:
        id_of = 0
		name = "A"
		number = "56"
		nap = 0
		for mip in range(massa):
			if file_n_data[int(mip)]["id"] == int(id_user):
				id_of = file_n_data[int(mip)]["id"]
				name = file_n_data[int(mip)]["name"]
				number = file_n_data[int(mip)]["number"]
				nap = mip

        print("ID: " + str(id_of) + '\nNAME: ' + name + '\nPHONE: +' + number)
        het = input("Вы уверены, что хотите продолжить?")
        if het == "YES":
            id = nap
        elif het == "NO":
            file_m.close()
            file_n.close()
            quit()
        else:
            print("ERROR")
            phone_check()
    else:
        print("Некорректный ввод. Вы уверены, что ввели число от 1 до " + str(massa) + "?")
        phone_check()

phone_check()

n_id = int(file_m_data["massa"])

file_m_data.update({"massa": n_id})
file_n_data.pop(int(id) - 1)

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

print("ГОТОВО")
