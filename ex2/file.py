# 16. Задать список из n чисел последовательности (1+1/n)^n 
# и вывести на экран их сумму 


# n = int(input('Введите число: ')) 

# def get_squerence(n):
#     return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

# nums = get_squerence(n)
# # print(nums)
# print(round(sum(nums), 5))

# --------------------------------------------------------------------------------

n = int(input('Введите число: '))

nums = lambda n: round((1+1/n)**n, 2)

arr = []

for i in range(1, n+1):
    if n > 0:
        arr.append(nums(i))
print(sum(arr))