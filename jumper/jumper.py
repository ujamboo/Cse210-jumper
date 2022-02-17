


class Jumper:

    def __init__(self):
        #the index we start with
        self.start = 0
        row1 = "  ___"
        row2 = " /___\\"
        row3 = " \   /"
        row4 = "  \ / "
        row5 = "   0 " 
        row6 = "  /|\ "
        row7 = "  / \ "
            #indexs start at 0,  
        self.jumper = [row1, row2, row3, row4, row5, row6, row7]



      
    def print_jumper(self):
        #for each index starting with self.start (0), to length of the list jumper(7)
        for i in range(self.start, len(self.jumper)):
            #print each item
            print(self.jumper[i])

        



