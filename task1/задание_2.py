print("сейчас вам нужно будет ввести любое число и код операции. 1-для работы с нечетными числами.2-для работы с четными числами.")
try:
    user_variable = int(input("Введите любое число-"))
    operation_code = int(input("Введите код операци-"))
except:
    print("Вы ввели не верные параметры")
else:
    if operation_code == 1:
        if user_variable % 2 != 0:
            counter = user_variable
            while counter >= 0:
                print(counter,end = '.')
                counter -= 2
    else:
        if operation_code == 2:
            counter = user_variable
            while counter >= 0:
                print(counter, end = '.')
                counter -= 2 
        else:
            print("Вы ввели не верный код операции")