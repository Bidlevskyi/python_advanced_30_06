#!/usr/local/bin python3
'''
Напишите функцию, которая возвращает список файлов из директории.
Напишите декоратор для этой функции, который распечатает все файлы с
раcширением .log из найденных
'''
import os

def print_log(func):
    def wrapper(*args):
        cur_dir = func(*args)
        log_files = filter(lambda x: x.endswith('.log'), cur_dir)
        for file in log_files:
            with open(file, 'r') as log_f:
                print(log_f.read())
    return wrapper
@print_log
def pr_dir(dir_name):
    files = os.listdir(dir_name)
    return files
