# 4) Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
# необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
some_words_list = list(input("Введите несколько слов через пробел: ").split())
for i, item in enumerate(some_words_list, 1):
    print(f"{i}.{item[:10]}")
    