# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# a = int(input('введите начальный элемент: '))
# d = int(input('введите разность между числами: '))
# n = int(input('введите количество элементов в списке: '))
# list_1 = []
# for i in range(n):
#     print(a+i*d,end = " ")

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# import random
# count = int(input('количество цифр в списке: '))
# list1 = []
# for _ in range(count):
#     number = random.randint(10,100)
#     list1.append(number)
# print(list1)

# min_num = int(input('Минимальное число диапазона = '))   
# max_num= int(input('Максимальное число диапозона = '))

# list2=[]
# if max_num>=min_num:
#     for i in range(len(list1)):
#         if max_num>=list1[i] and min_num<=list1[i]:
#             list2.append(i)
# print('количество символов: ',len(list2))
# print ('индексы: ',list2)


# n = int(input('введите количесво символов в первом списке: '))
# list1 = []
# for _ in range (n):
#     list1.append(int(input('введите значение элемента первого списка: ')))
# print(list1)
# x = int(input('начало диапозона: '))
# y = int(input('конец диапозона: '))
# # index = list1.index(x,y)
# # print(index)
# list2 = []
# for el in list1:
#     if x < el < y:
#         list2.append(el)
# print(list2)

# print('Какой язык программирования ты изучаешь?')
# language = input()
# print(language, '- отличный выбор!')
# a = int(input())
# b = a + 1 
# c = b + 1
# print (a,b,c , sep = '\n')
# a = int(input())
# b = int(input())
# c = int(input())
# d = a + b + c

# print(d)

# a = int(input())
# b = int(input())
# f = 3*(a+b)**3 + 275*b**2 - 127*a -41
# print(f)

# a = int(input())
# b = int(input())


# print(a ,'+' ,b, '=', a + b)

# print(a ,'-' ,b, '=',a - b)

# print(a ,'*' ,b, '=',a * b)


# x = int(input('школьники '))
# y = int(input('мандарины '))
# z = y//x
# print(z)

# print(y%x)


# a = int(input())
# a1 = a//1000
# a2 = (a%1000)//100
# a3 = (a//10)%10
# a4 = (a%10)

# print(f'Цифра в позиции тысяч равна {a1}')
# print(f'Цифра в позиции сотен равна {a2}')
# print(f'Цифра в позиции десятков равна {a3}')
# print(f'Цифра в позиции единиц равна {a4}')

# a = input()
# b = ['тысяч', 'сотен', 'десятков', 'единиц']
# for i in range(4):
#     print('Цифра в позиции ' + b[i] + ' равна ' + a[i])
# Цифра в позиции сотен равна 2
# Цифра в позиции десятков равна 8
# Цифра в позиции единиц равна 1
# if 
# print(10 // 3)
# print(-10 // 3)


# 3   # округление в меньшую сторону
# -4  # округление в меньшую сторону
# a = "пурю-ра-рам рам-пм-папам па-ра-па-да"
# b = a.split()
# print(b)
# print(b[0])
# print(b[1])
# print(b[2])
# count_0 = 0
# count_1 = 0
# count_2 = 0
# x = ("а", "е", "и", "о", "у", "ё", "ю", "я")
# for el in b[0]:
#     if el in x:
#         count_0 += 1
# print(count_0)
# for el in b[1]:
#     if el in (x):
#         count_1 += 1
# print(count_1)
# for el in b[2]:
#     if el in (x):
#         count_2 += 1
# print(count_2)

# if count_0 == count_1 == count_2:
#     print(f"Парам пам-пам")
# else:
#     print(f"Пам парам")

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.



