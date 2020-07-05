#!/usr/local/bin python3
def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает список
    только тех URL, в которых есть /catalog/.
    """
    result_list = list(filter(lambda x: "/catalog/" in x, url_list))
    return result_list

def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    i = len(input_str) // 2
    if len(input_str) % 2 == 0:
        output_str = input_str[i - 1:i + 2]
    else:
        output_str = input_str[i - 1:i + 2]
    return output_str

def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    output_dict = {}
    for w in input_str:
        output_dict[w] = output_dict.get(w, 0) + 1
    return output_dict

def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять
    вторую в середину первой
    """
    i = len(str1) // 2
    result_str = f'{str1[:i]}{str2}{str1[i:]}'
    return result_str

def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    from random import randint
    lst = [randint(0, 100) for _ in range(20)]    
    even_int_list = [x for x in lst if x % 2 == 0]
    return even_int_list

