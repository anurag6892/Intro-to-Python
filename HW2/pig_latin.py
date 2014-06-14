# Anurag Mukkara
# 11 June 2014
# pig_latin.py

import string

def pig_latin(a):
    vowels = ['a','e','i','o','u']
    first = a[0]
    if first in vowels:
        return a + 'hay'
    else:
        return a[1:] + first+ 'ay'

print pig_latin("boot")
print pig_latin("image")

phrase = raw_input("Enter a phrase with only words and spaces: ")
phrase = phrase.lower()
word_list = phrase.split()
result =  [pig_latin(x) for x in word_list]
print string.join(result)


