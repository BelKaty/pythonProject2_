# 2) Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения
# списка элементов необходимо использовать функцию input().
elements_list = list(input("Введите данные через запятую: ").split(","))
print(elements_list)
for i in range(1, len(elements_list), 2):
    elements_list[i-1], elements_list[i]=elements_list[i], elements_list[i-1]
print(elements_list)