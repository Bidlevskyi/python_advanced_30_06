#!/usr/local/bin/ python3
import unittest

from game import Room, Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.room1 = Room(0, 0, "Main room", "", ["north"])
        self.room2 = Room(0, -1, "Second room", "", ["south"])
        self.map = {(self.room1.x, self.room1.y): self.room1,
               (self.room2.x, self.room2.y): self.room2
            }
        self.game = Game(self.map)
    # это пример с лекции
    def test_move_positive(self): 
        self.game._move(0, -1)
        self.assertEqual(self.game.player_x, 0)
        self.assertEqual(self.game.player_y, -1)
        self.assertEqual(self.game.current_room, self.room2)
        
    def test_move_negative_1(self):
        expected = self.game._move(1, 1)
        result = print('Error: missing room')
        self.assertEqual(expected, result)

    def test_move_negative_2(self):
        expected = self.game._move(1, 1)
        self.assertIsNone(expected)

    def test_parse_positive(self):
        curs = 'go north'
        self.game._parse(curs)
        self.assertEqual(self.game.current_room, self.room2)

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.x = 5
        self.y = 4
        self.name = "Room to test your unit"
        self.description = "You see units standing, ready for test"
        self.exits = ['This way', 'That way']
        self.room = Room(self.x, self.y, self.name, self.description,
                         self.exits)
    
    def test_str(self):
        result = self.room.__str__()
        self.assertIs(type(result), str)
     
if __name__ == '__main__':
    unittest.main()
