class Player:
    def __init__(self) -> None:
        """ Initializes the Player object with a backpack attribute. """
        self._backpack = []
    
    @property
    def backpack(self)-> list:
        """ Getter for self._backpack. """
        return self._backpack
    
    @backpack.setter
    def backpack(self,new_bp) -> None:
        """ Setter for self._backpack. 

            Args:
                new_bp: a list
        """
        self._backpack = new_bp