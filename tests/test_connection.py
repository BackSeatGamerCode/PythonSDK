import sys
import time
import unittest
import logging
logging.root.setLevel(logging.DEBUG)

sys.path.append('..')

import bsg_test_child


class TestCases(unittest.TestCase):
    def test_connection(self):

        sdk = bsg_test_child.BSGTestChild()

        while True:
            sdk.poll()


if __name__ == '__main__':
    unittest.main()
