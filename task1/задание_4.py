try:
    list = list(map(int,input("Введите список элементов:").split()))
    number = int(input("Введите число:"))
    operations_cod = int(input("Введите код операции:"))
except:
    print("Вы ввели не верный тип данных")
else:
    if operations_cod == 1:
        for tmp in list:
            if number < tmp:
                print (tmp,end = ' ')
    else:
        if operations_cod == 0:
            for tmp in list:
                if number > tmp:
                    print (tmp,end = ' ')