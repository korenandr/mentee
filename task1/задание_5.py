try:
    list = list(map(int,input('Введите список элементов:').split()))
except:
    print('Один из элементов не является числом,а значит список не может быть арифметической прогрессией')
else:
    number_of_elements = len(list)
    final_value = number_of_elements - 1
    difference = list[1] - list[0]
    for number in range(1,number_of_elements):
        previous_index = number - 1
        if list[number] - list[previous_index] == difference:
            if number == final_value:
                print('список является арифметической прогрессией')
                break
        else:
            print('список не является арифметической прогрессией')
            break