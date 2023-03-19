import unittest
import variables

class MyTestCase(unittest.TestCase):
    def test_that_colours_exist(self):
        self.assertEqual(variables.COLOURS.RED.name, 'RED')

    def test_that_colour_contains_correct_value(self):
        self.assertEqual(variables.COLOURS.GREEN.value, '#C70039')


if __name__ == '__main__':
    unittest.main()
