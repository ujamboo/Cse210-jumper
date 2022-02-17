from jumper import Jumper
from input import Input
from word import Word

class Game:

    def __init__(self):

        #making a variable equal to the jumper class (making an instance)
        self.jumper = Jumper()

        #making a variable equal to the input class
        self.input = Input()

        #making an instance of the word class
        self.word = Word() 

        #variable equal to true
        self.keep_playing = True

    def start_game(self):

        #calling the word method from the word class
        self.word.word()

        #calling the word_list method from the word class
        self.word.word_list()

        #calling the underscores method from the word class
        self.word.underscores()
        

    def inputs(self):

        #while keep playing is equal to true, these methods will keep being called
        while self.keep_playing == True:
            
            #print underscores
            self.word.print_blanks()
            #calling the print jumper from the jumper class, it prints the parachute guy
            self.jumper.print_jumper()

            #this calls the user input method from the input class which asks for a letter a-z
            self.input.user_input()

    def do_updates(self):
        pass
    
    def do_outputs(self):
        pass



game = Game()

game.start_game()
game.inputs()
