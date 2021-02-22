from models.maze import Maze
from controllers.maze_controller import MazeController

class App:
    """ Main application of the game. """
    def __init__(self) -> None:
        """ Initializes two instances of Maze and MazeController Classes. """
        self._maze = Maze("maze.txt")
        self._maze_ctrl_obj = MazeController(self._maze)

    @property
    def maze_ctrl_obj(self:object) -> object:
        """ Getter for maze controller. """
        return self._maze_ctrl_obj

    def run(self):
        """ App will run until SystemExit is returned from MazeController object. """
        running_loop = True
        while running_loop:
            try:
                self._maze_ctrl_obj.run()
            except SystemExit:
                running_loop = False
        