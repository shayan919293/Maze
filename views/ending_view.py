from views.main_window_view import MainWindow
import pygame

class EndingView(MainWindow):
    def __init__(self):
        super().__init__()
        self.won_image = pygame.transform.scale(pygame.image.load('models/images/genius.png').convert(), (100, 132))
        self.won_image.set_colorkey((0,0,0))
        self.lost_image = pygame.transform.scale(pygame.image.load('models/images/poop.png').convert(), (88, 102))
        self.lost_image.set_colorkey((0,0,0))

    def create_text_surface(self,text,size=0,col="bl"):
        """ Creates a text surface for pygame. """
        arial = pygame.font.SysFont('arial', (2*size)+24)
        if col == "bl":
            text_surface = arial.render(text, True, (0, 0, 0))
        else:
            text_surface = arial.render(text, True, col)
        return text_surface

    def display_ending(self,name,score,capslock,won):
        """ displays ending window """
        self.window.fill((255,255,255))
        if won:
            text_surface_welcome = self.create_text_surface("Congrats! You won the game!")
            text_surface_info = self.create_text_surface("That was an amazing game you played!")
            self.window.blit(text_surface_welcome,(240,50))
            self.window.blit(text_surface_info,(190,150))
            self.window.blit(self.won_image, (50,50))
   

        else:
            text_surface_welcome = self.create_text_surface("Awwwwwww! You lost the game!")
            text_surface_info = self.create_text_surface("The game is finished now. Try harder")
            self.window.blit(text_surface_welcome,(220,50))
            self.window.blit(text_surface_info,(200,150))   
            self.window.blit(self.lost_image, (50,50))


        text_surface_name_taker = self.create_text_surface("Enter your name and press enter to save your score!")
        text_surface_name_printer = self.create_text_surface(f"Your name: {name}")
        text_surface_score_printer = self.create_text_surface(f"Your score: {score}")

        if capslock:
            text_surface_capslock = self.create_text_surface(f"CAPSLOCK is ON!",-4,(255,0,0))
            self.window.blit(text_surface_capslock,(125,380))


        self.window.blit(text_surface_name_taker,(125,250))
        self.window.blit(text_surface_name_printer,(125,350))
        self.window.blit(text_surface_score_printer,(125,400))
        pygame.display.flip()
