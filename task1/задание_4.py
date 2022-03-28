try:
    list = list(map(int,input("Введите список элементов:").split()))
    number = int(input("Введите число:"))
    operation_cod = int(input("Введите код операции:"))
except:
    print("Вы ввели не верный тип данных")
else:
    if operation_cod == 1:
        for tmp in list:
            if number < tmp:
                print (tmp,end = ' ')
    elif operation_cod == 0:
        for tmp in list:
            if number > tmp:
                print (tmp,end = ' ')
    else:
        print("Вы ввели не верный код операции")