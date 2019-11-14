# coding: utf-8

import unittest
import datetime
import mino

class MouIkutsuNerutoOshogatsuTest(unittest.TestCase):
    def test_1201(self):
        today = datetime.date(2019, 12, 1)
        target = mino.MouIkutsuNerutoOshogatsu()
        actual = target.answer(today)
        expected = 31
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()