try:
    min_range = int(input("Введите минимальный диапазон:"))
    max_range = int(input("Введите максимальный диапазон:"))
    operation_code = int(input("Введите код операци:"))
except:
    print("Вы ввели не верные параметры")
else:
    list = []
    for tmp in range(min_range,max_range):
        if tmp != max_range:
            list.append(tmp)
    else:
        if operation_code == 0:
            for tmp in list:
                if tmp % 2 == 0:
                    print(tmp,end = ' ')
        else:
            if operation_code == 1:
                for tmp in list:
                    if tmp % 2 != 0:
                        print(tmp,end = ' ')
            else:
                print("Вы ввели не верный код операции")