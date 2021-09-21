import unittest
from back import Soma

class TestSoma(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(Soma.somar(1,1), 2)