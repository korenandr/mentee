i = input("Введите любое число-")
if i.isdigit():
    if int(i)%2==0:
        print(i,"-это четное число")
    else:
        print(i,"-это не четное число")
else:
    print("Не пытайтесь меня обмануть!")