variable_1 = input("Введите любое число-")
if variable_1.isdigit():
    print("Сейчас вам нужно будет ввести код операции:1-для работы с четными числами,2-для работы с нечетными числами")
    operashion_cod = input("Введите код операции-")
    if operashion_cod.isdigit():
        if int(operashion_cod) == 1:
            if int(variable_1) % 2 != 0:
                print("Вы ввели не четное число,попробуйте ввести код операции 2")
            else:
                variable_3 = int(variable_1)
                while int(variable_3) >= 0:
                    print(variable_3,end = '.')
                    variable_3 -= 2
        else:
            if operashion_cod.isdigit():
                if int(operashion_cod) == 2:
                    if int(variable_1) % 2 == 0:
                        print("Вы ввели не четное число,попробуйте ввести код операции 1")
                    else:
                        variable_4 = int(variable_1)
                        while int(variable_4) >= 0:
                            print(variable_4, end = '.')
                            variable_4 -= 2                           
    else:
        print("Не пытайтесь снова меня обмануть!")        
else:
    print("Вы должны ввести число и оно не должно быть отрицательным!")