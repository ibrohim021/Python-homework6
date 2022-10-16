# 1. Задайте рандомно список из чисел размером N, где N число с клавиатуры.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# [2, 3, 5, 8, 3] -> на нечётных позициях элементы 3 и 8, ответ: 11

import random



# num_int = int(input('Введите число: '))

# arr = []
# for i in range(num_int):
#     arr.append(random.randint(0, 20))
# print() 
# print(arr)



# sum = 0
# for j in range(len(arr)):
#     if j%2 == 1:
#         sum += arr[j]
#         print(f'Элемент с не четным индексам = {arr[j]}')
# print(f'Сумма этих элементов = {sum}')

num_int = int(input('Введите число: '))

arr = []
for i in range(num_int):
    arr.append(random.randint(0, 20))
print() 
print(arr)


sum_elem = sum(arr[i] for i in range(1, len(arr), 2))
odd_el = str([arr[i] for i in range(1, len(arr), 2)]).strip('[]')
print(f'Для списка {arr} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_elem}.')