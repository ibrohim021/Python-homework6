

# Напишите программу, 
# которая принимает на вход число и проверяет
# кратно ли оно 5 и 10 или 15, но не 30


# def num(n):
#     if n%5 == 0 or n%10 == 0 or n%15 == 0:
#         print("Число кратно")
#     else:
#         print("Число не кратно")
#     return n


# n = int(input('введите число: '))

# result = num(n)

# print(result)

n = int(input('введите число: '))

num = lambda n:  n%10 == 0 or n%15 == 0 not in n%30 == 0 

result = num(n)

if result == True:
    print('Это кратное число')
else:
    print('Это не кратное число')

print(result)