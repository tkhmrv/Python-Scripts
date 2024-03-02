# import csv

# def read_and_write_csv(input_file, output_file):
#     try:
#         # Открытие файла на чтение
#         with open(input_file, 'r') as file:
#             # Чтение строк из файла
#             lines = file.readlines()

#             # Создание CSV файла
#             with open(output_file, 'w', newline='') as csv_file:
#                 # Задание заголовков CSV
#                 fieldnames = ['Имя', 'Возраст', 'Параметр1', 'Параметр2', 'Статус']
#                 writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

#                 # Запись заголовков в CSV
#                 writer.writeheader()

#                 # Запись данных в CSV
#                 for line in lines:
#                     data = line.strip().split()
#                     writer.writerow({'Имя': data[0], 'Возраст': data[1], 'Параметр1': data[2], 'Параметр2': data[3], 'Статус': data[4]})

#     except FileNotFoundError:
#         print(f"Файл {input_file} не найден.")

# # Указание пути к вашему файлу ввода
# input_file_path = 'test.txt'

# # Указание пути к файлу вывода CSV
# output_csv_path = 'output.csv'

# # Вызов функции для чтения и записи данных в CSV
# read_and_write_csv(input_file_path, output_csv_path)

import pandas as pd

def read_and_write_csv(input_file, output_csv):
    try:
        # Чтение данных из файла в DataFrame с использованием пробела в качестве разделителя
        df = pd.read_csv(input_file, sep=' ', header=None, names=['Имя', 'Возраст', 'Параметр1', 'Параметр2', 'Статус'])

        # Запись данных в CSV с явным указанием разделителя и без индексов
        df.to_csv(output_csv, sep=',', index=False)

    except FileNotFoundError:
        print(f"Файл {input_file} не найден.")

# Указание пути к вашему файлу ввода
input_file_path = 'test.txt'
    
# Указание пути к файлу вывода CSV
output_csv_path = 'output2.csv'

# Вызов функции для чтения и записи данных в CSV
read_and_write_csv(input_file_path, output_csv_path)

