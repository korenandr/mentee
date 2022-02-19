from ast import Return
from base64 import encode


try:
    user_variable = int(input("Введите любое число-"))
except:
    print("Вы ввели не верный тип данных")
else:
    if user_variable % 2 == 0:
        print("Вы ввели четное число")
    else:
        print("Вы ввели не четное число")
 
