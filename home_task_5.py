#!/usr/local/bin python3
def three_biggest_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """
    med_list = list(set(input_list))
    med_list.sort()
    biggest_ints = med_list[-3:]
    return biggest_ints

def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """
    lowest_int = min(input_list)
    lowest_int_index = input_list.index(lowest_int)
    return lowest_int_index

def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    input_list.reverse()
    reversed = input_list
    return reversed

def find_keys(dict1, dict2):
    """
    Найти обшие ключи в двух словарях, вернуть список их названий
    """
    set_dict1 = set(dict1.keys())
    set_dict2 = set(dict2.keys())
    set_dict1.intersection_update(set_dict2)
    common_keys = list(set_dict1)
    return common_keys


def sort_by_age(student_list):
    """
    Дан массив из словарей:
    [{'name': 'Viktor', 'age': 30, 'city': 'Kiev'},
     {'name': 'Andrey', 'age': 34, 'city': 'Kiev'},
     {'name': 'Maksim', 'age': 20, 'city': 'Dnepr'},
     {'name': 'Artem', 'age': 50, 'city': 'Dnepr'},
     {'name': 'Vladimir', 'age': 32, 'city': 'Lviv'},
     {'name': 'Dmitriy', 'age': 21, 'city': 'Lviv'}]

    C помощью sort() отсортировать массив из словарей
    по значению ключа 'age', сгруппировать данные по значению ключа 'city'
    вывод должен быть такого вида :
    {
     'Kiev': [ {'name': 'Viktor', 'age': 30 },
               {'name': 'Andrey', 'age': 34}],
     'Dnepr': [ {'name': 'Maksim', 'age': 20 },
                {'name': 'Artem', 'age': 50}],
     'Lviv': [ {'name': 'Vladimir', 'age': 32 },
               {'name': 'Dmitriy', 'age': 21}]
                                                                                                                                                                    
    }
    """
    city_list = {x['city'] for x in student_list}
    sorted_dict = dict()
    for i in city_list:
        sorted_dict[i] = []
        for y in student_list:
            if y['city'] == i:
                name = y['name']
                age = y['age']
                sorted_dict[i].append({'name': name , 'age': age })
        sorted_dict[i].sort(key=lambda r: r['age'])
    return sorted_dict
