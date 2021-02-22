import pytest
from models.maze import Maze
from models.player import Player

@pytest.fixture
def maze():
    return Maze('maze.txt')

def test_init_file_name(maze):
    """ 1001: Checks to see if file name is maze.txt. """
    assert maze._file_name == "maze.txt"

def test_init_player_obj(maze):
    """ 1002: Checks to see maze.player is instance of Player class. """
    assert isinstance(maze.player,Player)

def test_init_player_loc(maze):
    """ 1003: Checks to see maze.player_loc is empty list. """
    assert len(maze.player_loc) == 0
    assert isinstance(maze.player_loc,list)

def test_init_rows(maze):
    """ 1004: Tests if rows is instance of list. """
    assert isinstance(maze._rows,list)

def test_move_wrong_index(maze):
    """ 2001: Tests if can move to a wrong index. """
    assert not maze.can_move_to(999,999)

def test_move_wall(maze):
    """ 2002: Tests if can move to a wall. """
    assert not maze.can_move_to(0,0)

def test_random_spot(maze):
    """ 3001: Tests if random spots are random. """
    assert maze.find_random_spot() != maze.find_random_spot()

def test_random_spot_return(maze):
    """ 3002: Tests if random spot returns a tuple. """ 
    assert type(maze.find_random_spot()) == tuple

def test_is_exit(maze):
    """ 4001: Tests if is exit returns a boolean. """ 
    assert type(maze.is_exit(2,2)) == bool

def test_is_item(maze):
    """ 5001: Tests if is item returns a boolean. """ 
    assert type(maze.is_item(2,2)) == bool

def test_player_mover(maze):
    """ 6001: Tests if can move player to a new location. """
    old = [1,1]
    new = [2,2]
    maze.player_mover(new,old)
    assert maze._rows[new[0]][new[1]] == "P"
    assert maze._rows[old[0]][old[1]] == " "

def test_object_picker(maze):
    """ 7001: Tests if can pickup an object and add to backpack. """
    (row,col) = (1,1)
    maze._rows[row][col] = "obj"
    maze.object_picker(row,col)
    assert "obj" in maze.player.backpack

def test_rows_getter(maze):
    """ 8001: tests rows getter """
    assert maze._rows == maze.rows
