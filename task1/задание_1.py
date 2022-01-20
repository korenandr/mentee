from base64 import encode
from turtle import end_fill


i = input("Введите любое число-")
if i == ("хрень"):
     print("-Вы попытались меня обмануть!")
if i == ("бред"):
     print("-Вы попытались меня обмануть!")
if i == ("фигня"):
    print("-Вы попытались меня обмануть!")
if int(i) % 2 == 0:
    print(i,"-Это четное число")
else:
    print(i,"-Это не четное число")