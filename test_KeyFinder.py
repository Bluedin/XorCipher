import unittest
from KeyFinder import KeyFinder 

class KeyFinderTest(unittest.TestCase):

    def setUp(self):
        self.KF = KeyFinder()
        self.msg = "Je représente une entreprise qui vient de passer n°5 mondial des sites de e-commerce. Notre équipe informatique est composée de : 75 ingénieurs développement, qui développent et réalisent la MCO de nos services vitrines et backend, 75 ingénieurs système & réseau, qui conçoivent et réalisent la MCO de nos infrastructures, 75 personnes dans les équipes de testing à la fois sur la partie métier mais également sur la partie intégration système et interface utilisateur."
        self.key = "l"
        self.falseKey = 'f'
        self.crypted = "&\tL\x1e\t\x1c\x1e\x85\x1f\t\x02\x18\tL\x19\x02\tL\t\x02\x18\x1e\t\x1c\x1e\x05\x1f\tL\x1d\x19\x05L\x1a\x05\t\x02\x18L\x08\tL\x1c\r\x1f\x1f\t\x1eL\x02ÜYL\x01\x03\x02\x08\x05\r\x00L\x08\t\x1fL\x1f\x05\x18\t\x1fL\x08\tL\tA\x0f\x03\x01\x01\t\x1e\x0f\tBL\"\x03\x18\x1e\tL\x85\x1d\x19\x05\x1c\tL\x05\x02\n\x03\x1e\x01\r\x18\x05\x1d\x19\tL\t\x1f\x18L\x0f\x03\x01\x1c\x03\x1f\x85\tL\x08\tLVL[YL\x05\x02\x0b\x85\x02\x05\t\x19\x1e\x1fL\x08\x85\x1a\t\x00\x03\x1c\x1c\t\x01\t\x02\x18@L\x1d\x19\x05L\x08\x85\x1a\t\x00\x03\x1c\x1c\t\x02\x18L\t\x18L\x1e\x85\r\x00\x05\x1f\t\x02\x18L\x00\rL!/#L\x08\tL\x02\x03\x1fL\x1f\t\x1e\x1a\x05\x0f\t\x1fL\x1a\x05\x18\x1e\x05\x02\t\x1fL\t\x18L\x0e\r\x0f\x07\t\x02\x08@L[YL\x05\x02\x0b\x85\x02\x05\t\x19\x1e\x1fL\x1f\x15\x1f\x18\x84\x01\tLJL\x1e\x85\x1f\t\r\x19@L\x1d\x19\x05L\x0f\x03\x02\x8b\x03\x05\x1a\t\x02\x18L\t\x18L\x1e\x85\r\x00\x05\x1f\t\x02\x18L\x00\rL!/#L\x08\tL\x02\x03\x1fL\x05\x02\n\x1e\r\x1f\x18\x1e\x19\x0f\x18\x19\x1e\t\x1f@L[YL\x1c\t\x1e\x1f\x03\x02\x02\t\x1fL\x08\r\x02\x1fL\x00\t\x1fL\x85\x1d\x19\x05\x1c\t\x1fL\x08\tL\x18\t\x1f\x18\x05\x02\x0bL\x8cL\x00\rL\n\x03\x05\x1fL\x1f\x19\x1eL\x00\rL\x1c\r\x1e\x18\x05\tL\x01\x85\x18\x05\t\x1eL\x01\r\x05\x1fL\x85\x0b\r\x00\t\x01\t\x02\x18L\x1f\x19\x1eL\x00\rL\x1c\r\x1e\x18\x05\tL\x05\x02\x18\x85\x0b\x1e\r\x18\x05\x03\x02L\x1f\x15\x1f\x18\x84\x01\tL\t\x18L\x05\x02\x18\t\x1e\n\r\x0f\tL\x19\x18\x05\x00\x05\x1f\r\x18\t\x19\x1eB"
    
    def testFqrcFinder(self):
        decuCrypted = self.crypted
        keyFnd = KeyFinder.frqcFinder(decuCrypted, len(self.key))
        self.assertEqual(self.key, keyFnd)
        self.assertNotEqual(self.falseKey, keyFnd)

    def testBruteFrcFinder(self):
        decuCrypted = self.crypted
        keyFnd = self.KF.bruteFrcFinder(decuCrypted, len(self.key))
        self.assertEqual(self.key, keyFnd)
        self.assertNotEqual(self.falseKey, keyFnd)
