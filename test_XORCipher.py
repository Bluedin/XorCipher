import unittest
import codecs
from XORCipher import XORCipher 

class XORCipherTest(unittest.TestCase):

    def setUp(self):
        fileWritten = codecs.open("testWrite.txt", mode="w", encoding="iso8859_1" , errors='ignore')
        fileWritten.write('testAlreadyWritten')
        fileWritten.close()

    def testXorCiphering(self):
        msg = 'a'
        key = 'a'
        expected = '\x00'
        false = '\x01'
        foo = XORCipher.xorCiphering(msg, key)
        self.assertEqual(expected, foo)
        self.assertNotEqual(false, foo)
    
    def testGetTxtFrmFile(self):
        expected = 'test'
        location = 'test.txt'
        msg = XORCipher.getTxtFrmFile(location)
        self.assertEqual(expected, msg)
        self.assertNotEqual("", msg)

    def testPrintTxtToFile(self):
        expected = 'testwrite'
        false = 'testAlreadyWritten'
        location = 'testWrite.txt'
        msg = XORCipher.printTxtToFile(location, expected)
        filewritten = codecs.open(location, encoding='iso8859_1', errors='ignore')
        msgFnd = filewritten.read()
        filewritten.close()
        self.assertEqual(expected, msgFnd)
        self.assertNotEqual(false, msgFnd)

    