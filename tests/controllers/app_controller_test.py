import pytest
from controllers.app import App
from models.maze import Maze
from controllers.maze_controller import MazeController


@pytest.fixture
def app():
    return App()

def test_init_maze(app):
    """ 1001: Checks if app._maze is instance of Maze class. """
    assert isinstance(app._maze, Maze)

def test_run_obj(app):
    """ 2001: Checks if maze_ctrl_obj is instance of MazeController. """
    assert isinstance(app._maze_ctrl_obj, MazeController)

def test_maze_ctr_getter(app):
    """ 3001 : Checks if maze controller getter returns the _maze ctrl object """
    assert app.maze_ctrl_obj == app._maze_ctrl_obj

