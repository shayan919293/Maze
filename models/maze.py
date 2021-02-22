import random
from .player import Player

class Maze:
    """ Represents the maze game. """
    def __init__(self,file_name:str) -> None:
        """ Initializes the maze. """ 
        self._file_name = file_name
        self._rows = self.file_reader(self._file_name)
        self._objects = ["orange","apple","banana","cherry","peach"]
        self.player = Player()
        self.player_loc = []

    @property
    def objects(self)-> list:
        """ Getter for self._objects. """
        return self._objects
    
    @property
    def rows(self)->list:
        """ Getter for self._rows. """
        return self._rows

    def file_reader(self,file_name:str)-> list:
        """ Opens the file and returns a list containing lists of objects.

            Returns: final_list (list)
        """
        with open(file_name, 'r') as game_file:
            game = game_file.read()
            splitted = game.split("\n")
            final_list=[]
            for lines in splitted:
                line_list = []
                for words in lines:
                    line_list.append(words)
                final_list.append(line_list)
        return final_list


    def can_move_to(self, line_number, column_number)-> bool:
        """ Checks rows[line_number][column_number]
            
            Returns
                True: if the space is empty
                False: if the space has an object
        """
        try:
            if self._rows[line_number][column_number] == "X" or self._rows[line_number][column_number] == "x":
                return False
            return True
        except IndexError:
            return False

    
    def is_item(self,row_num, col_num) -> bool:
        """ Returns true if the location is one of the objects. """
        if self._rows[row_num][col_num] in self._objects:
            return True
        return False

    
    def is_exit(self,row_num,col_num) -> bool:
        """ Returns true if the location is the exit door. """
        if self._rows[row_num][col_num] == "E":
            return True
        return False
    

    def find_random_spot(self)->tuple:
        """ Returns a random empty spot using random numbers for rows and columns. """
        while True:
            rand_row = random.randint(0,len(self._rows)-1)
            rand_col = random.randint(0,len(self._rows[0]))-1
            if self._rows[rand_row][rand_col] == " ":
                return (rand_row,rand_col)
    

    def object_inserter(self,objects)-> None:
        """ Randomly puts different objects in the maze if the input is a list.

            Puts the object string in the game if the object is a string.
        """
        if type(objects) == list:
            for obj in objects:
                empty_spt = self.find_random_spot()
                self._rows[empty_spt[0]][empty_spt[1]] = obj
        if type(objects) == str:
            empty_spt = self.find_random_spot()
            self._rows[empty_spt[0]][empty_spt[1]] = objects
            if objects == "P":
                self.player_loc = [empty_spt[0],empty_spt[1]]
    

    def player_mover(self,new_loc,old_loc):
        """ Moves the player from the old location to a new location. """
        self._rows[new_loc[0]][new_loc[1]] = "P" 
        self._rows[old_loc[0]][old_loc[1]] = " "
        self.player_loc = new_loc

    
    def object_picker(self,row,col):
        """ Picks up an object from the player location and puts it in the backpack. """
        obj = self._rows[row][col]
        self.player.backpack.append(obj)
