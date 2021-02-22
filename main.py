import pygame
from controllers.app import App

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    clock.tick(144)
    app = App()
    app.run()
    