import rpyc
from rpyc.utils.server import ThreadedServer
from XORCipher import XORCipher
from DecryptChecker import DecryptChecker

class ServiceDecryption(rpyc.service):

    listKey = [{"keyTemp": "", "is correct": ""}]

    def exposed_askDecryption(msg, keytemp):
        
        return 42

    def exposed_getKeyResult():
        key = ""
        for keyTemp in listKey:
            if keyTemp["is correct"] == "True":
                key = KeyTemp["keyTemp"]
        return key