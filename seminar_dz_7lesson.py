# a = "пурю-ра-рам рам-пум-папам па-ра-па-да"
# b = a.split()
# count_0 = 0
# count_1 = 0
# count_2 = 0
# x = ("а", "е", "и", "о", "у", "ё", "ю", "я")
# for el in b[0]:
#     if el in x:
#         count_0 += 1
# for el in b[1]:
#     if el in (x):
#         count_1 += 1
# for el in b[2]:
#     if el in (x):
#         count_2 += 1
# if count_0 == count_1 == count_2:
#     print(f"Парам пам-пам")
# else:
#     print(f"Пам парам")


# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.
    

def print_operation_table(operation, num_rows=9, num_columns=9):
     for i in range(1, num_rows + 1):
         answer = []
         for j in range(1, num_columns + 1):
             answer.append(str(operation(i, j)))
         print(''.join(f'{e:<4}' for e in answer))
 
print_operation_table(lambda x, y: x * y)
