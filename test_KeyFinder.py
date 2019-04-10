import unittest
from KeyFinder import KeyFinder 

class KeyFinderTest(unittest.TestCase):

    def setUp(self):
        self.msg = "test test test test test test"
        self.key = "abcd"
        self.falseKey = 'aaaa'
        self.crypted = "\x15\x07\x10\x10A\x16\x06\x17\x15B\x17\x01\x12\x16C\x10\x04\x11\x17D\x15\x07\x10\x10A\x16\x06\x17\x15"
    
    def fqrcFinderTest(self):
        keyFnd = KeyFinder.fqrcFinder(self.crypted, len(self.key))
        self.assertEqual(self.key, keyFnd)
        self.assertNotEqual(self.falseKey, keyFnd)
