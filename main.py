# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3]
sum = 0
for i in range(len(my_list)):
    if i % 2 != 0:
        sum += my_list[i]
 
print (sum)



# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]

l = len(lst)
if( l % 2 > 0) : l += 1
l = int(l/2)

out = [lst[i] * lst[ -i - 1] for i in range(0,  l)]
print(out)


#  Вариант 2 

# lst = [2, 3, 4, 5, 6]

# def outs(lst):
#     my_list = []
#     l = len(lst)
#     if( l % 2 > 0):
#          l += 1
#          l = int(l/2)
#     for i in range(l):
#          s = lst[i] * lst[-i -1] 
#          my_list.append(s)
#     return my_list
# print(outs(lst))
# ==================================================
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def maxmin( my_number ):
    max = 0.0;
    min = 1.0;

    drobs = [ round( my_number[i] - int(my_number[i]),2) for i in range(len(my_number)) if my_number[i] != int(my_number[i])]

    for a in drobs :
        if max < a : max = a
        if min > a : min = a
    print( f" min ={min} max = {max}" )
    return ( max - min)

my_number = [1.1, 1.2, 3.1, 5, 10.01, 12.0]
print(maxmin(my_number))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input())
 
b = ''
 
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print(int(b))