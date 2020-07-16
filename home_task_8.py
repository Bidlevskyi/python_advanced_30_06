#!/usr/local/bin python3
'''
Напишите функцию, которая читает и распечатывает текстовый файл.
Напишите декоратор к этой функции, который печатает название файла и
количество слов в нем
'''

def couter_words(func):
    def wrapper(*args):
        f_na = str(args[0])
        words = 0
        with open(f_na, 'r') as file:
            for line in file:
                line_lts = line.split()
                words += len(line_lts) 
        print('Name:', f_na, 'Words:', words)
        func(*args)
    return wrapper

@couter_words
def print_file(file_name):
    print(file_name)
    file_n = str(file_name)
    with open(file_n, 'r') as file:
        print(file.read())
        
 
