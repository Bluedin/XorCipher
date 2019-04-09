
# XorCipher

We have 11 files that were crypted. From our investigation, we found that they were encrypted with a XOR Cipher using a key composed of 6 letters in lowercase.

To find this key we wrote a program in Python.

Based on our research, there are two ways to find a key used to encrypt with XOR :

  - Brute Force : Testing all possibilities until we decipher the message
  - With frequency analysis



## Frequency Analysis :

The way frequency analysis works is by testing all possibility for each character of the key and compare the frequency of letter to what is expected based on the target language.
For exemple in french, the frequency of the letter 'e' is the highest. That's why to find the right letter, we search which letter yields the highest frequency of 'e' in the decrypted message.

The algorith is as follow :

  - Seperate message to decrypt in block the length of the key
  - Make as many table as the length of the key and fill them with the corresponding character from our blocks
      we now have table filled with the character which are to be decrypted by the same character from the key
      One table for the first character of the key, one for the second, ...
  - For each table, decrypt with all possibility (26 character) and find the one with the highest frequency of 'e'

With this we can find the key.

Number of try : 26 + 26 + 26 + 26 + 26 + 26 = 156


## About XOR Cipher :

XOR Cipher is a symetric Cipher where we have a key composed of characters. Theses characters encrypt the message letter by letter with a XOR operation.

Reminder : XOR operation is an operation effective at a byte level and represented by the '^' operator in python : 
1^1 = 0, 1^0 = 1, 0^0 = 0

The method is to convert character to encrypt to int, same for character from key and perform a XOR operation between the two.



## Brute-Force :

We try every key until we find the good one. For example: AAAAAA, then AAAAAB, ...

Number of try : 26 * 26 * 26 * 26 * 26 * 26 = 308 915 776


In the Brute-Force method, we test each combination which require to ckeck the result each time, as the number of possible combination is too big, it is not feasible to check each one by hand, thats why we must ckeck the result with a dictionary.



## Dictionary :

A dictionary is a database or a file containing a list of words from a language.

