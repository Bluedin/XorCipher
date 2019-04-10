# coding: utf-8
from __future__ import unicode_literals

import os
import codecs
import numpy as np

fileEncoding = 'iso8859_1'

class XORCipher:
    instances = 0
    def __init__(self, file, key):
        self.file = file
        self.key = key
        XORCipher.instances += 1


    def xorCiphering(msg, key):
        decodedMsg = ""
        for i in range(len(msg)):
            r = ord(msg[i]) ^ ord(key[i%len(key)])
            decodedMsg += chr(r)
        return decodedMsg

    def getTxtFrmFile(location):
        fileToDecrypt = codecs.open(location, encoding=fileEncoding , errors='ignore')
        message = fileToDecrypt.read()
        fileToDecrypt.close()
        return message

    def printTxtToFile(location, msg):
        fileToDecrypt = codecs.open(location, mode="w", encoding=fileEncoding , errors='ignore')
        fileToDecrypt.write(msg)
        fileToDecrypt.close()



# c1 = XORCipher("", "")

# files = ["PA", "PB", "PC", "PD", "PE", "PF", "PG", "PH", "PI", "PJ", "PK"]
# key = "test"

# for i in range(len(files)):

#     message = XORCipher.getTxtFrmFile("C:\\Users\\pblue\\Downloads\\Groupe 1 (3)\\{}.txt".format(files[i]))
#     decrypted = XORCipher.xorCiphering(message, key)

#     fileToWrite = XORCipher.printTxtToFile("C:\\Users\\pblue\\Downloads\\Groupe 1\\decrypted\\{}.txt".format(files[i]), decrypted)
    
   