try:
    min_range = int(input("Введите минимальный диапазон:"))
    max_range = int(input("Введите максимальный диапазон:"))
    operation_code = int(input("Введите код операци:"))
except:
    print("Вы ввели не верные параметры")
else:
    if operation_code == 0:
        for tmp in range(min_range,max_range):
            if tmp % 2 == 0:
                print(tmp,end = ' ')
    elif operation_code == 1:
        for tmp in range(min_range,max_range):
            if tmp % 2 != 0:
                print(tmp,end = ' ')
    else:
        print("Вы ввели не верный код операции")