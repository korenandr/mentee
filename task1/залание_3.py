print("Сыграем в игру,я загадала число от 1 до 10,а у вас будет 3 попытки чтобы его отгадать,погнали...")
from random import randint
random_number = randint(1,10)
counter = 3
while counter >= 1:
    counter -= 1
    try:
        user_variable = int(input("Введите ваше число-"))
    except:
        print("Вы ввели не верный тип данных")
        break
    if user_variable == random_number:
        print("Вы отгадали,я загадала число-",random_number)
        break
    elif user_variable < random_number:
        print("Я загадал число больше чем ваше")
    else:
        print("Я загадала число меньше чем ваше")