from pypresence import Presence
from time import time

import Setting.config
from Setting.config import SET

RPC = Presence(SET["CLIENT_ID"])
RPC.connect()

print("Discod RPC V1.0 by Sweet1e42\nСейчас ваше приложение: " + SET["CLIENT_NAME"])
print("----------------------------------------\n")

a = input("Введите первое значение: ")
b = input("Введите второе значение: ")

print("----------------------------------------\n")

g = input("Желаете добавить кнопки? [y/n]: ")
try:
    if g == "y":
        i = input("Сколько желаете добавить кнопок [1/2]: ")
        try:
            if i == "1":
                butn_1 = input("\nВведите название кнопки: ")
                butn_2 = input("Введите ссылку: ")

                button = [
                    {
                        "label": butn_1,
                        "url": butn_2
                    }
                ]

            elif i == "2":
                butn_1 = input("\nВведите название кнопки: ")
                butn_2 = input("Введите ссылку: ")

                butn_3 = input("\nВведите название кнопки: ")
                butn_4 = input("Введите ссылку: ")

                button = [
                    {
                        "label": butn_1,
                        "url": butn_2
                    },
                    {
                        "label": butn_3,
                        "url": butn_4                      
                    }
                ]
            else: pass
        except: pass

    elif g == "n":
        button  = None
        
    else: pass
except: pass

print("----------------------------------------\n")

img = input("Желаете добавить картинки? [y/n]: ")
try:
    if img == "y":
        d = input("\nВведите название большой картинки: ")
        c =  input("Введите название маленькой картинки: ")

        images = "\nBig Image: " + d + " " + "\nSmall Image: " + c

    elif img == "n":
        d = None
        c = None
    else: pass
except: pass

print("----------------------------------------\n")

print("Все готово, Приятного использования!")

RPC.update(
    state = f"{b}",
    details = f"{a}",
    start = time(),

    buttons = button,

    large_image = f"{d}",
    small_image = f"{c}"
)

if __name__ == "__main__":
    input("Что-бы отключится нажмите [ENTER]")