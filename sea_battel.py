#!/usr/local/bin python3
from random import randint
from os import system

class Battel:

    def __init__(self):
        count_ships_user1 = set()
        count_ships_user2 = set()
        fild_user1 = []
        fild_user2 = []
        enemy_of_user1 = []
        enemy_of_user2 = []

    def counter_ships(self):
        count_us = set()
        while len(count_us) < 10:
            count_us.add(tuple(randint(0, 9) for _ in range(2)))
        return count_us

    def fild_user(self, count_us_ship):
        fild_us = [['~' for _ in range(10)] for _ in range(10)]
        for x, y in count_us_ship:
            fild_us[x][y] = 'o'
        return fild_us

    @staticmethod
    def print_fild(fild_us):
        for i in fild_us:
            print(''.join(i))

    @staticmethod
    def test_input():
        while True:
                tes_x, tes_y =map(str, input('Enter coordinats: ').split())
                if tes_x.isdigit() and tes_y.isdigit():
                        x = int(tes_x)
                        y = int(tes_y)
                        if 0 <= x <=9 and 0 <= y <=9:
                            break
        else:
            print('please input digit of 0 to 9')
        return x, y

    def run_battle(self):
        self.count_ships_user1 = self.counter_ships()
        self.count_ships_user2 = self.counter_ships()
        self.fild_user1 = self.fild_user(self.count_ships_user1)
        self.fild_user2 = self.fild_user(self.count_ships_user2)
        self.enemy_of_user1 = [['~' for _ in range(10)] for _ in range(10)]
        self.enemy_of_user2 = [['~' for _ in range(10)] for _ in range(10)]
        winner = 'None'
        while winner == 'None':
            while winner == 'None':
                if len(self.count_ships_user2) == 0:
                    winner = 'User1'
                    break
                system('clear')
                print('Fild of usre1')
                self.print_fild(self.fild_user1)
                print('')
                print('enemy fild')
                print('')
                print(self.enemy_of_user1)
                self.print_fild(self.enemy_of_user1)
                x1, y1 = self.test_input()
                if self.fild_user2[x1][y1] == '~':
                    self.fild_user2[x1][y1] = '*'
                    self.enemy_of_user1[x1][y1] = '*'
                    break
                elif self.fild_user2[x1][y1] == '*':
                    print('you are shoted there before')
                    break
                self.fild_user2[x1][y1] = 'x'
                self.count_ships_user2.discard((x1, y1))
                if len(self.count_ships_user2) == 0:
                    winner = "User1"

            while winner == 'None':
                if len(self.count_ships_user1) == 0:
                    winner = 'User2'
                    break
                system('clear')
                print('Fild of usre2')
                self.print_fild(self.fild_user2)
                print('')
                print('enemy fild')
                print('')
                self.print_fild(self.enemy_of_user2)
                x2, y2 = self.test_input()
                if self.fild_user1[x2][y2] == '~':
                    self.fild_user1[x2][y2] = '*'
                    self.enemy_of_user2[x2][y2] = '*'
                    break
                elif self.fild_user1[x2][y2] == '*':
                    print('you are shoted there before')
                    break
                self.fild_user1[x2][y2] = 'x'
                self.count_ships_user1.discard((x1, y1))
                if len(self.count_ships_user1) == 0:
                     winner = "User2"
        print(winner)

                		
bat = Battel()
bat.run_battle()

