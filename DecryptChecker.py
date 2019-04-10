import codecs


class DecryptChecker:

    def __init__(self):
        self.dictionnary = []
        dictFile = codecs.open("liste_francais.txt", encoding='iso8859_1', errors='ignore')
        dictTemp = dictFile.readlines()
        dictFile.close()
        for word in dictTemp:
            self.dictionnary.append(word.replace("\r\n", ''))

    def msgCheck(self, msg):
        count = 0
        tabMsg = msg.split(" ")
        for word in tabMsg:
            if word in self.dictionnary:
                count += 1
            if (count/len(tabMsg))*100 > 70:
                return True
        return False

