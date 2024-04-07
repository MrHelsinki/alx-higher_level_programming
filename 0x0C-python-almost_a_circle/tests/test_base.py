#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_noarg(self):
        case_one = Base()
        case_two = Base()
        self.assertEqual(case_one.id, case_two.id - 1)


if __name__ == "__main__":
    unittest.main()
