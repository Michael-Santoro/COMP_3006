#Michael Santoro
#DU ID: 871869018
#Description: This code will test each of the

import unittest
import count
import sys

class TestCount(unittest.TestCase):
    def test_noFlag(self):
        f = open('Test_Case/no_args.csv', mode='r', encoding='ASCII')
        file_test = f.read()
        sys.argv =[]
        sys.argv.append('test.txt')
        self.assertEqual(count.print_count(), file_test)
    def test_cFlag(self):
        f = open('Test_Case/c_args.csv', mode='r', encoding='ASCII')
        file_test = f.read()
        sys.argv =[]
        sys.argv.append('test.txt')
        sys.argv.append('-c')
        self.assertEqual(count.print_count(), file_test)
    def test_lFlag(self):
        f = open('Test_Case/l_args.csv', mode='r', encoding='ASCII')
        file_test = f.read()
        sys.argv =[]
        sys.argv.append('test.txt')
        sys.argv.append('-l')
        sys.argv.append('ab')
        self.assertEqual(count.print_count(), file_test)
    def test_zFlag(self):
        f = open('Test_Case/z_args.csv', mode='r', encoding='ASCII')
        file_test = f.read()
        sys.argv =[]
        sys.argv.append('test.txt')
        sys.argv.append('-z')
        self.assertEqual(count.print_count(), file_test)

if __name__ == '__main__':
    unittest.main()
