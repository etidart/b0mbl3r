import json
import codecs
from os import system

file_n = codecs.open("js/input.json", "r", "utf_8_sig")
file_n_data = json.load(file_n)

file_m = codecs.open("js/massa.json", "r", "utf_8_sig")
file_m_data = json.load(file_m)

def chck():
    het = input("\nСледующие действия: ")
    if het == "LOOK":
        print(file_n_data)
        chck()
    elif het == "CREATE":
        crte = system("python crte.py")
        chck()
    elif het == "DELETE":
        dlte = system("python dlte.py")
        chck()
    elif het == "QUIT":
        quit()
    else:
        chck()


chck()
