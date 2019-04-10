import unittest
from DecryptChecker import DecryptChecker

class DecryptCheckerTest(unittest.TestCase):

    def setUp(self):
        self.DC = DecryptChecker()
        self.msg = "world mine yacht bonjour xavier vecteur"
        self.falseMsg = "aefnefna pgaeg,eg azf"

    def testMsgCheck(self):
        result = self.DC.msgCheck(self.msg)
        resultfalse = self.DC.msgCheck(self.falseMsg)
        self.assertEqual(True, result)
        self.assertEqual(False, resultfalse)
