import island.game
import unittest

Game = island.game.Game


class TestGame(unittest.TestCase):

    def test_nothing_happens_without_guru(self):
        num_blue_eyed = 3
        game = Game(num_blue_eyed=num_blue_eyed)

        for day in range(30):
            self.assertEqual(game.day, day)
            num_left = game.advance_one_day()
            self.assertEqual(num_left, 0)

    def test_meeple_leave_with_guru(self):
        def run_for_num(num_blue_eyed):
            game = Game(num_blue_eyed=num_blue_eyed)
            game.run_guru()

            num_left = 0
            for day in range(num_blue_eyed):
                self.assertEqual(game.day, day)
                self.assertEqual(num_left, 0)
                num_left = game.advance_one_day()

            self.assertEqual(num_left, num_blue_eyed)

        run_for_num(3)
        run_for_num(4)
        run_for_num(5)
        run_for_num(6)
        run_for_num(7)
        run_for_num(8)
