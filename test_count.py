#Michael Santoro
#DU ID: 871869018
#Description: This code will test each of the

import unittest
import count
import sys

class TestCount(unittest.TestCase):
    def test_noFlag(self):
        '''Testing Count File with no flags'''
        f = open('Test_Case/no_args.csv', mode='r', encoding='ASCII')
        file_test = f.read()
        sys.argv =[]
        sys.argv.append('test.txt')
        self.assertEqual(count.print_count(), file_test)
    def test_cFlag(self):
        '''Testing Count File with '-c' flags'''
        f = open('Test_Case/c_args.csv', mode='r', encoding='ASCII')
        file_test = f.read()
        sys.argv =[]
        sys.argv.append('test.txt')
        sys.argv.append('-c')
        self.assertEqual(count.print_count(), file_test)
    def test_lFlag(self):
        '''Testing Count File with '-l' flags with 'ab' input'''
        f = open('Test_Case/l_args.csv', mode='r', encoding='ASCII')
        file_test = f.read()
        sys.argv =[]
        sys.argv.append('test.txt')
        sys.argv.append('-l')
        sys.argv.append('ab')
        self.assertEqual(count.print_count(), file_test)
    def test_zFlag(self):
        '''Testing Count File with '-z' flags'''
        f = open('Test_Case/z_args.csv', mode='r', encoding='ASCII')
        file_test = f.read()
        sys.argv =[]
        sys.argv.append('test.txt')
        sys.argv.append('-z')
        self.assertEqual(count.print_count(), file_test)
    def test_clFlag(self):
        '''Testing Count File with '-c' and '-l' flags'''
        f = open('Test_Case/cl_args.csv', mode='r', encoding='ASCII')
        file_test = f.read()
        sys.argv =[]
        sys.argv.append('test.txt')
        sys.argv.append('-c')
        sys.argv.append('-l')
        sys.argv.append('ab')
        self.assertEqual(count.print_count(), file_test)
    def test_clzFlag(self):
        '''Testing Count File with '-c', '-l', and '-z' flags'''
        f = open('Test_Case/clz_args.csv', mode='r', encoding='ASCII')
        file_test = f.read()
        sys.argv =[]
        sys.argv.append('test.txt')
        sys.argv.append('-c')
        sys.argv.append('-l')
        sys.argv.append('ab')
        sys.argv.append('-z')
        self.assertEqual(count.print_count(), file_test)
    def test_czFlag(self):
        '''Testing Count File with '-c' and '-z' flags'''
        f = open('Test_Case/cz_args.csv', mode='r', encoding='ASCII')
        file_test = f.read()
        sys.argv =[]
        sys.argv.append('test.txt')
        sys.argv.append('-c')
        sys.argv.append('-z')
        self.assertEqual(count.print_count(), file_test)
    def test_lzFlag(self):
        '''Testing Count File with '-l' and '-z' flags'''
        f = open('Test_Case/lz_args.csv', mode='r', encoding='ASCII')
        file_test = f.read()
        sys.argv =[]
        sys.argv.append('test.txt')
        sys.argv.append('-l')
        sys.argv.append('ab')
        sys.argv.append('-z')
        self.assertEqual(count.print_count(), file_test)

if __name__ == '__main__':
    unittest.main()
