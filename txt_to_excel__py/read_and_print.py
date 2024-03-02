# read_and_print.py

# Определение функции для чтения данных из файла и вывода их в терминал
def read_and_print(file_path):
    try:
        # Открытие файла на чтение
        with open(file_path, 'r') as file:
            # Чтение строк из файла
            lines = file.readlines()

            # Вывод данных в терминал
            for line in lines:
                # Разбивка строки на элементы
                data = line.strip().split()

                # Печать данных
                print(f"Имя: {data[0]}, Возраст: {data[1]}, Параметр1: {data[2]}, Параметр2: {data[3]}, Статус: {data[4]}")

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")

# Указание пути к вашему файлу
file_path = 'test.txt'

# Вызов функции для чтения и вывода данных
read_and_print(file_path)
