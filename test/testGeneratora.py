import unittest

from src.generator import GeneratorKulWody

class Test_Generatora(unittest.TestCase):
    def setUp(self):
        pass
    def test_dziala(self):
        self.assertEqual('Ok', 'Ok');
    def test_generujJedna(self):
        self.generator = GeneratorKulWody()
        self.assertEqual(self.generator.zwrocWspolrzedne(), [(0.0,0.0,0.0)])
    def test_generujSiedem(self):
        self.generator = GeneratorKulWody(7)
        self.assertEqual(self.generator.zwrocWspolrzedne(), [(-3.4,0,0),
                                                             (0,-3.4,0),
                                                             (0,0,-3.4),
                                                             (0,0,0),
                                                             (0,0,3.4),
                                                             (0,3.4,0),
                                                             (3.4,0,0)])
    def generujSzesc(self):
        self.generator = GeneratorKulWody(6)
        self.assertEqual(self.generator.zwrocWspolrzedne(), [(-3.4,0,0),
                                                             (0,-3.4,0),
                                                             (0,0,-3.4),
                                                             (0,0,3.4),
                                                             (0,3.4,0),
                                                             (3.4,0,0)])
                                                             

if __name__ == '__main__':
    unittest.main()
