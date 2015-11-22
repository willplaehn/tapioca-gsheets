# coding: utf-8

import unittest

from tapioca_gsheets import Gsheets


class TestTapiocaGsheets(unittest.TestCase):

    def setUp(self):
        self.wrapper = Gsheets()


if __name__ == '__main__':
    unittest.main()
