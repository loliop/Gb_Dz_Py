#  Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# days = int(input('Ведите цифру обозначающую день недели: \n '))

# if days > 5 < 8:
#     print(f'{days}-ой день является выходным')
# else:
#     print('Увы не выходной')


# # Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# def check(x: bool, y: bool, z: bool):
#     a = not (x or y or z)
#     b = not x and not y and not z

#     if a != b:
#         print(f'{x} {y} {z} is not ok')
#     else:
#         print(f'{x} {y} {z} is ok')


# true_false = [True, False]

# for x in true_false:
#     for y in true_false:
#         for z in true_false:
#             check(x, y, z)


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# def quadrant(x: int(), y: int()):
#     if x > 0 and y > 0:
#         return 1
#     elif x < 0 and y > 0:
#         return 2
#     elif x < 0 and y < 0:
#         return 3
#     elif x > 0 and y < 0:
#         return 4
#     else:
#         print('error')


# x = int(input())
# y = int(input())
# print(quadrant(x, y))

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input("Введите число: "))
a = []
for i in range(1, n+1):
    print(i, sep=" ",end=" ")
    if(i < n):
        print("+", sep=" ", end=" ")
    a.append(i)
print("=", sum(a))


 
#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

b = int(input('Ведите число:'))
suma = 0

while b > 0:
    digit = b % 10
    suma += digit
    b = b // 10
 
print("Сумма:", suma)
