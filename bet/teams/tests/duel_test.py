# execute from parent directory

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import utils
import duel
import unittest

class Tests(unittest.TestCase):

    def test_test(self):
        pass

if __name__ == '__main__':

    unittest.main()
