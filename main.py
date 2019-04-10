from XORCipher import XORCipher
from DecryptChecker import DecryptChecker
from KeyFinder import KeyFinder


DC = DecryptChecker()
KF = KeyFinder()
KeyFound = ""

while 1:
    

    print("Que voulez vous faire ?")
    print("1. Trouver une clé")
    print("2. Déchiffrer un fichier")

    input1 = int(input())

    if input1 == 1:
        print("Chemin vers le fichier: ")
        fileLocation = input()
        print("Taille de la clé /nombre de caractères: ")
        keylen = int(input())
        print("Quelle méthode voulez vous utiliser ?")
        print("1. Analyse fréquentiel")
        print("2. Brute force")
        choice = int(input())
        msgToDecrypt = XORCipher.getTxtFrmFile(fileLocation)
        if choice == 1:
            keyFound = KeyFinder.frqcFinder(msgToDecrypt, keylen)
            print("Clé trouvé: {}".format(keyFound))
        elif choice == 2:
            keyFound = KF.bruteFrcFinder(msgToDecrypt, keylen)
            print("Clé trouvé: {}".format(keyFound))

    elif input1 == 2:
        print("Chemin vers le fichier: ")
        fileLocation = input()
        useKey = 'n'
        if KeyFound != "":
            print("Voulez-vous utiliser la dernière clé trouvée : y/n")
            useKey = input()
        if useKey == 'n':
            print("Quelle est la clé utilisée ?")
            KeyFound = input()
        print("Chemin vers le fichier de sortie: ")
        decryptedFileLocation = input()
        msgToDecrypt = XORCipher.getTxtFrmFile(fileLocation)
        decryptedMsg = XORCipher.xorCiphering(msgToDecrypt, KeyFound)
        XORCipher.printTxtToFile(decryptedFileLocation, decryptedMsg)

    print("Continuer ? y/n")
    response = input()
    if response == 'n':
        break



