import unittest
import game.food as food

class MyTestCase(unittest.TestCase):
    def test_countdown_start(self):
        f = food.Food(10)
        self.assertEqual(f.remaining_countdown, 10)

    def test_reduce_at_normal_speed(self):
        f = food.Food(10)
        f.reduce_at_normal_speed()
        self.assertEqual(f.remaining_countdown, 9)

    def test_reduce_at_increased_speed(self):
        f = food.Food(10)
        f.reduce_at_increased_speed()
        self.assertEqual(f.remaining_countdown, 8)
#
# if __name__ == '__main__':
#     unittest.main()
