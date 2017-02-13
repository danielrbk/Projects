"""
Challenge link: https://www.hackerrank.com/challenges/basic-cryptanalysis

Decrpyt a list of space separated words to a list of words in dictionary.lst

A frequency attack won't work because the words in our dictionary are not common English words, but technical ones.

Therefore, we use a string isomorphism attack by attempting to map an encrypted word to one in our dictionary.
If and only if there is one match between the encrypted word to a non-encrypted word, we add the isomorphism to our
decryption map.

Constraints for a successful hackerrank run:
1 <= words in dictionary.lst <= 1700
1 <= words in input <= 100
"""

from fileinput import input

line = input()[0]
unsorted = [s for s in line.strip().split( )]
encryptedWords = sorted(unsorted, key=lambda s: [len(s),s])

f = open('dictionary.lst','r')
words = [x.strip().lower() for x in f.readlines()]
words = sorted(words, key=lambda s: [len(s),s]) # sort words according to length followed by lexicographical order

keys = []
for w in encryptedWords:
    for c in list(w):
        if c not in keys:
            keys.append(c)

decryptionMap = {key: None for key in keys} # encrypted letter to unencrypted letter

def make_isomorphism(encryptedWord, word, currMap):
    """
    Attempts to make an isomorphism of an encrypted word to a word in our dictionary.
    The function attempts to map a letter to the respective one in the decrypted word.
    This is done only if the letter is not already mapped to a letter in our current map.
    :param encryptedWord: A string representing the encrypted word
    :param word: A string representing a word out of our dictionary
    :param currMap: A dictionary mapping certain letters to other ones.
    :return: a modified version of currMap for which the encrypted word can be mapped to our word. None otherwise.
    """
    encryptedWord = list(encryptedWord)
    keys = encryptedWord
    word = list(word)
    decryptionMap = currMap.copy()
    encryptionMap = {chr(i+97): None for i in range(26)}

    for k,v in decryptionMap.items():
        if v is not None:
            encryptionMap[v]=k

    i=0
    for c in encryptedWord:
        if decryptionMap[c] is None and encryptionMap[word[i]] is None:
            decryptionMap[c] = word[i]
            encryptionMap[word[i]] = c
        else:
            if encryptionMap[word[i]] != c:
                return None
            if decryptionMap[c] != word[i]:
                return None
        i+=1
    return decryptionMap

# Start with longest words and attempt to map encrypted letters to standard letters.
while len([k for k,v in decryptionMap.items() if v is None])!=0:
    for e in reversed(encryptedWords):
        prevMapping = decryptionMap.copy()
        count = 0
        for w in reversed(words):
            if len(w)==len(e):
                map = make_isomorphism(e, w, prevMapping)
                if map is not None:
                    if count==1: # We've already mapped the word thus there are multiple options to map the current word
                        decryptionMap = prevMapping
                        break
                    count+=1
                    decryptionMap = map.copy()
            elif len(w)<len(e):
                break

string = ""
# Print the decrpyted words according to the original order.
for w in unsorted:
    for c in list(w):
        string += decryptionMap[c]
    string+=" "

print(string)