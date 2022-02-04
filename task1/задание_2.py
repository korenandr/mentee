user_variable = input("Введите любое число-")
if user_variable.isdigit():
    print("Сейчас вам нужно будет ввести код операции:1-для работы с четными числами,2-для работы с нечетными числами")
    operation_code = input("Введите код операции-")
    if operation_code.isdigit():
        if int(operation_code) == 1:
            if int(user_variable) % 2 != 0:
                print("Вы ввели не четное число,попробуйте ввести код операции 2")
            else:
                while_variable_1 = int(user_variable)
                while while_variable_1 >= 0:
                    print(while_variable_1,end = '.')
                    while_variable_1 -= 2
        else:
            if int(operation_code) == 2:
                if int(user_variable) % 2 == 0:
                    print("Вы ввели не четное число,попробуйте ввести код операции 1")
                else:
                    while_variable_2 = int(user_variable)
                    while while_variable_2 >= 0:
                        print(while_variable_2, end = '.')
                        while_variable_2 -= 2                           
    else:
        print("Не пытайтесь снова меня обмануть!")        
else:
    print("Вы должны ввести число и оно не должно быть отрицательным!")