

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input("Введите число: "))
# a = []
# for i in range(1, n+1):
#     print(i, sep=" ",end=" ")
#     if(i < n):
#         print("+", sep=" ", end=" ")
#     a.append(i)
# print("=", sum(a))


 
#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# b = int(input('Ведите число:'))
# suma = 0

# while b > 0:
#     digit = b % 10
#     suma += digit
#     b = b // 10
 
# print("Сумма:", suma)

# Реализуйте алгоритм перемешивания списка 


import random
 
y = ['Ела', 'Спала', 'Ломала', 'Пила']
random.shuffle(y)
 
print(y)