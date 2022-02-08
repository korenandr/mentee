counter = 1
while counter >= 1:
    counter -= 1
    try:
        user_variable = int(input("Введите любое число-"))
    except:
        print("Вы ввели не верный тип данных")
        break
    if user_variable % 2 == 0:
        print(user_variable,"-это четное число")
    else:
        print(user_variable,"-это не четное число")