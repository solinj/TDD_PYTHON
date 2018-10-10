import unittest
import mycode as m
# from mycode import *

class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(m.hello_world(), 'hello world')

    def test_score_joseph(self):
        self.assertEqual(m.calculerScore("Joseph", 15), '66%')

    def test_score_marie(self):
        self.assertEqual(m.calculerScore("Marie", 33), '50%')

    def test_score_marc(self):
        self.assertEqual(m.calculerScore("Marc", 60), '43%')

    def test_score_ely(self):
        self.assertEqual(m.calculerScore("Ely", 28), '75%')


if __name__ == '__main__':
    unittest.main()
    # test = MyFirstTests()
    # test.test_hello()

