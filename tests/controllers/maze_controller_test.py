import pytest
from controllers.maze_controller import MazeController
from views.maze_view import MazeView
from models.maze import Maze
from unittest.mock import patch


@pytest.fixture
def maze():
    """ Fixture for maze object """
    return Maze('maze.txt')

@pytest.fixture
def maze_control(maze):
    """ Fixture for maze_controller object. """
    return MazeController(maze)

def test_init_maze_object(maze_control):
    """ 1001: Tests if maze object of maze_controller is instance of Maze. """
    assert isinstance(maze_control._maze,Maze)

def test_init_view_object(maze_control):
    """ 1002: Tests if view object of maze_controller is instance of Maze_view. """
    assert isinstance(maze_control._view,MazeView)

def test_maze_getter(maze_control):
    """ 2001: Tests maze getter. """
    assert maze_control.maze == maze_control._maze




