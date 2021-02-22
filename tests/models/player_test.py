import pytest
from models.player import Player

@pytest.fixture
def player():
    """ Fixture for Player. """
    return Player()

def test_init_backpack(player):
    """ 1001: Tests for backpack attribute. """
    assert player._backpack == []

def test_getter_backpack(player):
    """ 2001: Tests for backpack getter. """
    assert player.backpack == []

def test_setter_backpack(player):
    """ 3001: Tests for backpack setter. """
    player.backpack = [12]
    assert player.backpack == [12]
