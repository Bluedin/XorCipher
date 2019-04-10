import string
from XORCipher import XORCipher

class KeyFinder:

    def frqcFinder(msg):
        key = ""
        keylen = 0

        key = KeyFinder.frqcFinder(msg, keylen)
        return key

    def frqcFinder(msg, keylen):
        key = ""
        msgBloc = []
        keyDict = []
        for i in range(0, keylen):
            msgBloc.append([])
        for i in range(0, len(msg)):
            msgBloc[i%keylen].append(msg[i])
        for i in range(0, keylen):
            letterDict = {}
            keyDict.append({"letter": "", "value": 0})
            for letter in string.ascii_lowercase:
                # letterDict[letter] = []
                decryptBloc = []
                for j in msgBloc[i]:
                    decryptBloc.append(XORCipher.xorCiphering(j, letter))
                letterDict[letter] = decryptBloc.count('e')+1/len(decryptBloc)
                if(keyDict[i] is None or keyDict[i]["value"] < letterDict[letter]):
                    keyDict[i] = {"letter": letter, "value": letterDict[letter]}
            key += keyDict[i].get("letter")

        # msgBloc = [msg[i:i+keylen] for i in range(0, len(msg), keylen)]

        return key

    def hammingDistance(bloc1, bloc2):
        hammingDistance = 0
        return hamminDistance


#file1 = "PB"


# files = ["PA", "PB", "PC", "PD", "PE", "PF", "PG", "PH", "PI", "PJ", "PK"]

# for i in range(len(files)):

#     message = XORCipher.getTxtFrmFile("C:\\Users\\pblue\\Downloads\\Groupe 1 (3)\\{}.txt".format(files[i]))

#     key = KeyFinder.frqcFinder(message, 6)
#     print("{}: {}".format(files[i], key))

#decrypted = XORCipher.xorCiphering(message, key)

#fileToWrite = XORCipher.printTxtToFile("C:\\Users\\pblue\\Downloads\\Groupe 1\\decrypted\\{}test.txt".format(file1), decrypted)
    



