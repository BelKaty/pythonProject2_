# 3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

#решение через dict
month_num = int(input("Введите число от 1 до 12: "))
seasons_dict = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
for seasons, months in seasons_dict.items():
    if month_num in months:
        print(f'Время года - {seasons}.')

#решение через list
month_numb = int(input("Введите число от 1 до 12: "))
seasons_list = ['Зима', 1, 'Зима', 2, 'Весна', 3, 'Весна', 4, 'Весна', 5, 'Лето', 6, 'Лето', 7, 'Лето', 8, 'Осень', 9, 'Осень', 10, 'Осень', 11, 'Зима', 12]
i = seasons_list.index(month_numb)
print(f'Время года - {seasons_list[i - 1]}')