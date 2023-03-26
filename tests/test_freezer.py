import unittest
import game.freezer

class MyTestCase(unittest.TestCase):
    def test_initializing_rows(self):
        freezer = game.freezer.Freezer(2, 2)
        self.assertEqual(freezer.freezer, [[None, None], [None, None]])  # add assertion here

    def test_initializing_with_none(self):
        freezer = game.freezer.Freezer(None, None)
        self.assertEqual(freezer.freezer, [])

    def test_initalize_freezer_with_strings(self):
        freezer = game.freezer.Freezer('two', 2)
        self.assertEqual(freezer.freezer, [])

    def test_initialize_freezer_with_one_row_zero_items(self):
        freezer = game.freezer.Freezer(1,0)
        self.assertEqual(freezer.freezer, [[]])

    def test_initialze_freezer_with_zero_rows(self):
        freezer = game.freezer.Freezer(0, 1)
        self.assertEqual(freezer.freezer, [])

    def test_initialze_freezer_with_zero_rows_and_zero_items(self):
        freezer = game.freezer.Freezer(0, 0)
        self.assertEqual(freezer.freezer, [])


if __name__ == '__main__':
    unittest.main()
