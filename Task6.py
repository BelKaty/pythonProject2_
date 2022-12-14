# 6) *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
n = int(input("Введите количество вводимых товаров: "))
product = []
name_1 = []
price_1 = []
quantity_1 = []
unit_1 = []

for i in range(0, n):
    name = input("Введите название товара: ")
    cost = input("Введите цену товара: ")
    quantity = input("Введите количество товара: ")
    unit = input("Введите единицу измерения товара: ")
    m = (i + 1, {"название": name, "цена": cost, "количество": quantity, "единица измерения": unit})
    product.append(m)
    name_1.append(name)
    price_1.append(cost)
    quantity_1.append(quantity)
    unit_1.append(unit)
print(product)
print("Сортировка по ключу: ")
analytic = [{"название": name_1,
             "цена": price_1,
             "количество": quantity_1,
             "единица измерения": unit_1}]
print(analytic)