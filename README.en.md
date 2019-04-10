# XorCipher

We have 11 files that have been encrypted. During our investigation, we discovered that they were encrypted using XOR encryption using a 6-letter lower-case key.

To find this key, we wrote a program in Python. This program is interactive using a console.

According to our research, there are two ways to find a key used to encrypt with XOR:

  - Brute Force: Test all possibilities until we decipher the message
  - With frequency analysis



## Frequency analysis :

Frequency analysis works by testing all the possibilities for each character of the key and comparing the frequency of the letter to what is expected according to the target language.
For example, in French, the frequency of the letter `e` is the highest. That's why to find the right letter, we look for the letter that gives the highest frequency of'e' in the decrypted message.

The algorithm is as follows:

  - Separate message to decrypt the length of the key as a whole
  - Make as many tables as the length of the key and fill them with the corresponding character from our blocks
      we now have a table filled with the character that must be decrypted by the same character of the key
      A table for the first character of the key, one for the second character,...
  - For each table, decrypt with all the possibilities (26 characters) and find the one with the highest frequency of `e`.

Using this method we were able to find the key `fabqtl`.

Number of tests: 26 + 26 + 26 + 26 + 26 + 26 + 26 + 26 + 26 + 26 = 156


## About XOR Cipher:

XOR Cipher is a symmetrical code where we have a key composed of characters. These characters encrypt the message letter by letter with an XOR operation.

Reminder: Operation XOR is an efficient operation at byte level and represented by the operator'^' in python : 
1^1 = 0, 1^0 = 1, 0^0 = 0

The method consists in converting the character to be encrypted to int, the same for the character of the key and performing an XOR operation between the two.



## Brute-Force:

We try all the keys until we find the right one. For example: AAAAAA, then AAAAAB, .....

Number of tests: 26 * 26 * 26 * 26 * 26 * 26 * 26 * 26 * 26 * 26 * 26 = 308 915 776


In the Brute-Force method, we test each combination, which requires checking the result each time. Since the number of possible combinations is too large, it is not possible to check each of them by hand, so we have to check the result with a dictionary.


To try all combinations, we use a recursive function that allows us to test all letter combinations with a list. With each new combination, we try to decrypt the file and then check the content. If found, the function returns the found key.



## Dictionary:

A dictionary is a database or file containing a list of words in a language.
The dictionary used is a text file with one word per line.
We extracted the data inside and stored it in a list to then check the results of the decryption.


To check that a file has been decoded, we separate the contents of the decrypted file into a string list using the split function with the space separator ` `. Then we check if each string in the list is in the dictionary. A ratio `number of words found/number of words in the file` is calculated, if it is greater than 0.7 the file is considered to be correctly decrypted.


## Brute-Force distributed:

The same method as for Brute-Force, but the decryption and verification are done on other machines. 
You can use the ServiceDecryption script to create temporary servers on other computers. They are called to perform decryption and verification operations in distributed versions of the Brute-Force functions. The results are stored on the server and then retrieved by the main program to find the key.


## Class diagram :

![image](https://user-images.githubusercontent.com/19566220/55901080-e714d600-5bc8-11e9-85e8-772c1671b423.png)



## Use the program:
Launch the main.py program with Python
On the command line in the project folder:
  
  `python main.py`

Translated with www.DeepL.com/Translator

