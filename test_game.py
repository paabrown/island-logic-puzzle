import game
import unittest

print("game", game)

Game = game.Game


class TestGame(unittest.TestCase):

    def test_nothing_happens_without_witch(self):
        game = Game(num_blue_eyed=3)
        self.assertEqual(game.day, 0)

        for day in range(30):
            self.assertEqual(game.day, day)
            num_left = game.advance_one_day()
            self.assertEqual(num_left, 0)
