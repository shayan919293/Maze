import pygame
class MainWindow:
    """ View to display game screen. """
    def __init__(self) -> None:
        """ Sets up the view of the screen. """
        self.window_height = 800
        self.window_width = 800
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.window.set_colorkey((0, 0, 0))
        self.window.fill((255,255,255))
