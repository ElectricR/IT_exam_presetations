# Считаем входные ограничения
S, N = map(int, input().split())

# Ининциализируем нужные переменные
files = [] # Массив файлов пользователей
num_users = 0 # Макс. количество файлов пользователей
max_file = 0 # Максимальный объем файла
i = 0 # Индекс текущего элемента

# Считаем файлы пользователей и добавим в массив
for i in range(N):
    files.append(int(input()))


def BubbleSort(input_list):
    for i in range(len(input_list) - 1):
        is_sorted = True
        for j in range(len(input_list) - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = \
                        input_list[j + 1], input_list[j]
                is_sorted = False
        if is_sorted:
            break

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
