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

    def test_1231(self):
        today = datetime.date(2019, 12, 31)
        target = mino.MouIkutsuNerutoOshogatsu()
        actual = target.answer(today)
        expected = 1
        self.assertEqual(actual, expected)

    def test_0101(self):
        today = datetime.date(2020, 1, 1)
        target = mino.MouIkutsuNerutoOshogatsu()
        actual = target.answer(today)
        expected = 0
        self.assertEqual(actual, expected)

    def test_0102(self):
        today = datetime.date(2020, 1, 2)
        target = mino.MouIkutsuNerutoOshogatsu()
        actual = target.answer(today)
        expected = 0
        self.assertEqual(actual, expected)

    def test_0103(self):
        today = datetime.date(2020, 1, 3)
        target = mino.MouIkutsuNerutoOshogatsu()
        actual = target.answer(today)
        expected = 0
        self.assertEqual(actual, expected)

    def test_0104(self):
        today = datetime.date(2020, 1, 4)
        target = mino.MouIkutsuNerutoOshogatsu()
        actual = target.answer(today)
        expected = 363
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()