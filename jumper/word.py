import random

class Word:

    def __init__(self):

        #random word list
        self.list = ["sugar", "amendoim", "cracker" ]
        
        #making a variable named random word
        self.random_word = ""
        
        #making an empty list for our list of letters
        self.letters = []

        #empty list for the blanks
        self.blanks = []

    def word(self):
        #get a random word from the list of words
        self.random_word = random.choice(self.list)
        print(self.random_word)
    
    def word_list(self):
    
        #for each letter in the random_word
        for letter in self.random_word:

            #add the letter to the letters list
            self.letters.append(letter)

    
    def underscores(self):
        
        #take the letters list and for each letter 
        for letter in self.letters:
            #add a letter to the blanks list
            self.blanks.append("_")

    def print_blanks(self):
        print(self.blanks)





   
    