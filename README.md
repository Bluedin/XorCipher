# XorCipher

Nous avons 11 fichiers qui ont été cryptés. Au cours de notre enquête, nous avons découvert qu'ils étaient cryptés à l'aide d'un chiffrement XOR à l'aide d'une clé composée de 6 lettres en minuscules.

Pour trouver cette clé, nous avons écrit un programme en Python.

D'après nos recherches, il y a deux façons de trouver une clé utilisée pour crypter avec XOR : 
  - Brute Force : Tester toutes les possibilités jusqu'à ce que nous déchiffrions le message
  - Avec analyse de fréquence



# Analyse de fréquence :

L'analyse de fréquence fonctionne en testant toutes les possibilités pour chaque caractère de la clé et en comparant la fréquence de la lettre à ce qui est attendu en fonction de la langue cible.
Par exemple, en français, la fréquence de la lettre'e' est la plus élevée. C'est pourquoi pour trouver la bonne lettre, nous recherchons la lettre qui donne la plus haute fréquence de'e' dans le message décrypté.

# L'algorithme est le suivant :

  - Message séparé pour déchiffrer en bloc la longueur de la clé
  - Faire autant de tableaux que la longueur de la clé et les remplir avec le caractère correspondant à partir de nos blocs
      nous avons maintenant une table remplie du caractère qui doit être déchiffré par le même caractère de la clé
      Une table pour le premier caractère de la clé, une pour le second, ....
  - Pour chaque table, décrypter avec toutes les possibilités (26 caractères) et trouver celle qui a la fréquence la plus élevée de'e'.

Avec ça, on peut trouver la clé.
Nombre d'essais : 26 + 26 + 26 + 26 + 26 + 26 + 26 = 156


# A propos de XOR Cipher :

XOR Cipher est un code symétrique où nous avons une clé composée de caractères. Ces caractères cryptent le message lettre par lettre avec une opération XOR.

Rappel : L'opération XOR est une opération efficace au niveau des octets et représentée par l'opérateur'^' en python : 
1^1 = 0, 1^0 = 1, 0^0 = 0

La méthode consiste à convertir le caractère à chiffrer en int, de même pour le caractère de la clé et effectuer une opération XOR entre les deux.



# Brute-Force :

On essaie toutes les clés jusqu'à ce qu'on trouve la bonne. Par exemple : AAAAAAAA, puis AAAAAB, ....
Nombre d'essais : 26 * 26 * 26 * 26 * 26 * 26 * 26 * 26 = 308 915 776


Dans la méthode Brute-Force, nous testons chaque combinaison qui nécessite de ckeck le résultat à chaque fois, comme le nombre de combinaisons possibles est trop grand, il n'est pas possible de vérifier chacune à la main, c'est pourquoi nous devons ckeck le résultat avec un dictionnaire.



# Dictionnaire :
Un dictionnaire est une base de données ou un fichier contenant une liste de mots d'une langue.

