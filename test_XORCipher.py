import unittest
from XORCipher import XORCipher 

class XORCipherTest(unittest.TestCase):

    def setUp(self):
        fileWritten = codecs.open("testWrite.txt", mode="w", encoding="osi8859_1" , errors='ignore')
        fileWritten.write('testAlreadyWritten')
        fileWritten.close()

    def testXorCiphering(self):
        msg = 'a'
        key = 'a'
        expected = '\x00'
        foo = XORCipher.xorCiphering(msg, key)
        self.assertEqual(foo, expected)
    
    def testGetTxtFrmFile(self):
        expected = 'test'
        location = 'test.txt'
        msg = XORCipher.getTxtFrmFile(location)
        self.assertEqual(expected, msg)

    def testPrintTxtToFile(self):
        expected = 'testwrite'
        location = 'testWrite.txt'
        msg = XORCipher.printTxtToFile(location, expected)
        filewritten = codecs.open(location, encoding='osi8859_1', errrors='ignore')
        self.assertEqual(expected, filewritten.read())

    