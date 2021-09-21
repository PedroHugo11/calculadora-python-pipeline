import unittest
from back import Subtracao

class TestSubtracao(unittest.TestCase):

    def test_subtracao(self):
        self.assertEqual(Subtracao.subtrair(2,1), 1)