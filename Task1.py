# 1) Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а
# указать явно, в программе.
x_list = [5, 'top', 4.83, False, [1, 2, 3], {9, 7, 5}, (11, 22, 33, 44, 55), None, {1: 'I', 5: 'V', 10: 'X'}]
print(x_list)
for i, item in enumerate(x_list, 1):
    print(f"{item} - {type(item)}")