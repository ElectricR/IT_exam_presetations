BubbleSort(files) # Отсортируем массив файлов

# Заполним диск файлами
while i != len(files) and files[i] <= S:
    S -= files[i]
    max_file = files[i]
    i += 1

# Найдем максимальное количество файлов пользователей
num_users = i

# Найдем размер максимального файла
while i != len(files) and S - max_file + files[i] > 0:
    S -= files[i] - max_file
    max_file = files[i]
    i += 1

print(num_users, max_file) # Выведем ответ
