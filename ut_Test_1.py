#!/usr/bin/python3

import unittest
import Test_1

class Test_Create_Common_List(unittest.TestCase):
    def test01_empty_lists(self):
        a = []
        b = []

        expected = [] 

        self.assertEqual(Test_1.create_common_list(a, b), expected)
        

    def test02_one_empty_list(self):
        a = []
        b = ['a', 'b', 'c', 'a']

        expected = ['a', 'b', 'c']

        self.assertEqual(Test_1.create_common_list(a, b), expected)


    def test03_combined_lists(self):
        a = ['a', 'c', 'a', 'a', 'a', 'b', 'tg']
        b = ['z', 'a', 'a', 'c', 'p']

        expected = ['a', 'b', 'c', 'p', 'z', 'tg']

        self.assertEqual(Test_1.create_common_list(a, b), expected)
        

    def test04_None_as_args(self):
        a = None
        b = None

        self.assertRaises(SystemExit, lambda: Test_1.create_common_list(a, b))


    def test05_strings_as_args(self):
        a = 'test'
        b = 'input'

        self.assertRaises(SystemExit, lambda: Test_1.create_common_list(a, b))


if __name__ == '__main__':
    unittest.main()
