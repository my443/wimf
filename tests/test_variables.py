import unittest
import variables

class MyTestCase(unittest.TestCase):
    def test_that_colours_exist(self):
        self.assertEqual(variables.COLOURS.RED.name, 'RED')  # add assertion here


if __name__ == '__main__':
    unittest.main()
