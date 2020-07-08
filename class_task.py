#!/usr/local/bin python3
def name_and_bals(str):
    cherta = str.find('|')
    name = str[:cherta + 1]
    bals_list = str[cherta + 1:].split(",")
    bals_summ = 0
    for i  in bals_list:
        print(i)
        bals_summ =+ int(i)
    print(bals_summ)
    bals = int(bals_summ / len(bals_list))
    return f'{name}{bals}'
    

print(name_and_bals("ere|24, 48, 22"))
