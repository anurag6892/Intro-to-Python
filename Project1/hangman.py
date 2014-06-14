# -*- coding: utf-8 -*-
# Anurag Mukkara
# 11 June 2014
# hangman.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *
print "Art created by sk"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words


WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    print len(wordlist)
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True  

def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    
    ####### YOUR CODE HERE ######
    result = []
    for letter in secret_word:
        if letter in letters_guessed:
            result.append(letter)
        else:
            result.append('-')

    return join(result,'')

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0
    letters_guessed = []
    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word  = get_word()

    ####### YOUR CODE HERE ######
    while(True):
        n = MAX_GUESSES - mistakes_made
        print_hangman_image(mistakes_made)
        if (n == 0):
            print "No more guesses left"
            print "Game over!"
            print "Secret word is:", secret_word
            print "You lose"
            break
        print n, "guesses left"
        print print_guessed()

        char = raw_input("Enter a letter, or the word 'guess' to try and guess the full word: ")
        if char == "guess":
            guess_word = raw_input("Enter the complete word: ")
            if guess_word == secret_word :
                 print "Game Over!"
                 print "Secret word is:", secret_word
                 print "You win"
            else:
                 print "Wrong guess :("
                 mistakes_made+=2
                 continue
        else:    
            char = lower(char)
            if char not in letters_guessed:
                letters_guessed.append(char)    
                if char not in secret_word:
                    mistakes_made += 1
                elif word_guessed():
                        print "Game Over!"
                        print "Secret word is:", secret_word
                        print "You win"
                        break
    
    return None




