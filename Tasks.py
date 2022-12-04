# Задача 1: Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Задача 2: Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Задача 3: Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Задача 4: Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Задача 5: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

try:
    task = int(input('Введите номер задачи: '))
except ValueError:
    print('Не корректный ввод')
    raise SystemExit
from random import randint
match task:
    case 1:
        any_list = [randint(0, 10) for i in range(10)]
        print(any_list)
        result = 1
        for index in range(1, len(any_list), 2):
            result *= any_list[index]
        print(result)
    case 2:
        any_list = [randint(1, 10) for i in range(int(input('Введите размер списка: ')))]
        print(any_list)
        result = []
        x = any_list[int(len(any_list) - 1)]
        for index in range(int(len(any_list) / 2)):
            result.append(any_list[index] * any_list[int(len(any_list) - 1 - int(index))])
        if int(len(any_list)) % 2 != 0:
            result.append(any_list[int(len(any_list) / 2)] ** 2)
        print(result)
    case 3:
        flo_list = [float(input('Введит вещественное число: ')) for i in range(int(input('Введите размер списка: ')))]
        print(flo_list)
        res_list = []
        for index in range(len(flo_list)):
            res_list.append(round(flo_list[index] % 1, 2))
        result = float(max(res_list) - min(res_list))
        print('%.2f' % result)
    case 4:
        try:
            num = int(input('Введите число: '))
        except ValueError:
            print('Вы ввели не целое число')
            raise SystemError
        result = ''
        while num / 2 > 0:
            result = str(num % 2) + result
            num = num // 2
        print(result)
    case 5:
        try:
            k = int(input('Задайте число: '))
        except ValueError:
            print('Не корректный ввод')
            raise SystemExit
        fib_list = [0] * (k * 2 + 1)
        n = 1
        if k == 0:
            print(fib_list)
            raise SystemExit
        else:
            fib_list[int((len(fib_list) / 2)) + 1] = 1
            fib_list[int((len(fib_list) / 2)) - 1] = 1
        for index in range(int(len(fib_list) / 2) + 2, int(len(fib_list))):
            fib_list[index] = fib_list[index - 1] + fib_list[index - 2]
        for ind in range(0, int(len(fib_list) / 2) - 1):
            fib_list[int(len(fib_list) / 2) - 2 - ind] = fib_list[int(len(fib_list) / 2) - ind] - fib_list[int(len(fib_list) / 2) - 1 - ind]
        print(fib_list)
