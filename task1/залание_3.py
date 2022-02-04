from random import randint
random_chislo = randint(0,10)
user_variable_1 = input("Сейчас у вас будет 3 попытки отгадать число.Введите любое число от 1 до 10-")
if user_variable_1.isdigit():
    if int(user_variable_1) == random_chislo:
        print("Вы отгадали,я загадала число-",random_chislo)
    else:
        if random_chislo < int(user_variable_1):
            print("Я загадала число меньше чем ваше")
        else:
            print("Я загадала число больше чем ваше")
else:
    print("Вы попытались меня обмануть!")
user_variable_2 = input("Вторая попытка-")
if user_variable_2.isdigit():
    if int(user_variable_2) == random_chislo:
        print("Вы отгадали,я загадала число-",random_chislo)
    else:
        if random_chislo < int(user_variable_2):
            print("Я загадала число меньше чем ваше")
        else:
            print("Я загадала число больше чем ваше")
else:
    print("Вы попытались меня обмануть!")
user_variable_3 = input("Третья попытка-")
if user_variable_3.isdigit():
    if int(user_variable_3) == random_chislo:
        print("Вы отгадали,я загадала число-",random_chislo)
    else:
        if random_chislo < int(user_variable_3):
            print("Я загадала число меньше чем ваше-",random_chislo)
        else:
            print("Я загадала число больше чем ваше-",random_chislo)
else:
    print("Вы попытались меня обмануть!")