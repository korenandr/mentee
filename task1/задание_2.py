print("сейчас вам нужно будет ввести любое число и код операции. 1-для работы с нечетными числами.2-для работы с четными числами.")
try:
    min_range = int(input("Введите минимальный диапазон:"))
    max_range = int(input("Введите максимальный диапазон:"))
    operation_code = int(input("Введите код операци:"))
except:
    print("Вы ввели не верные параметры")
else:
    if operation_code == 1:
        if max_range % 2 != 0:
            counter = max_range
            while counter >= min_range:
                print(counter,end = ' ')
                counter -= 2
        else:
            print("Вы ввели не верный максимальный диапазон для данного кода операции")
    else:
        if operation_code == 2:
            if max_range % 2 == 0:
                counter = max_range
                while counter >= min_range:
                    print(counter, end = ' ')
                    counter -= 2 
            else:
                print("Вы ввели не верный максимальный диапазон для данного кода операции")
        else:
            print("Вы ввели не верный код операции")