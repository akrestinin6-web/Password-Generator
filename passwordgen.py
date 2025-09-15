import pyperclip
import sys
import time
import random

password = input("Введите ваш пароль и нажмите Enter: ")

while len(password) < 8:
    time.sleep(0.1)
    symbollist = ["!", "@", "#", "$", "%", "^", "&", "*",
                  "(", ")", "_", "+", "-", "=", "{", "}", "[", "]", ":", ";", "<", ">", ",", ".", "?", "/"]
    letterslist = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s",
                   "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    allcharacters = symbollist + letterslist + numbers
    randoms = random.choice(allcharacters)
    password += randoms

pyperclip.copy(password)
print("Ваш пароль скопирован в буфер обмена:", password)

print("Если вы хотите помочь нашему проекту расти и добавлять новые функции, вы можете пожертвовать здесь: https://www.tinkoff.ru/rm/r_uMxrlqubzO.MXddEFVisp/y2HvV79711. Скопируйте и вставьте эту ссылку в ваш браузер или нажмите на ссылку, удерживая ctrl + левую кнопку мыши.")

exit1 = input("Нажмите Enter, чтобы закрыть программу: ")
sys.exit("Остановка кода")
