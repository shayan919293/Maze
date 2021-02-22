import pytest
from controllers.maze_controller import MazeController
from views.maze_view import MazeView
from models.maze import Maze


@pytest.fixture
def maze():
    """ Fixture for maze object. """
    return Maze('maze.txt')

@pytest.fixture
def maze_view(maze):
    """ Fixture for maze_view object. """
    return MazeView(maze)


def test_init_maze(maze_view):
    """ 1001: tests if self._maze is instance of Maze class. """
    assert isinstance(maze_view._maze, Maze)


def test_maze_getter(maze_view):
    """2001: Tests maze getter. """
    assert maze_view._maze == maze_view.maze



