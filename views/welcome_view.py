from views.main_window_view import MainWindow
import pygame 

class WelcomeView(MainWindow):

    def __init__(self):
        super().__init__()


    def create_text_surface(self,text,size=0,col="bl"):
        """ Creates a text surface for pygame. """
        arial = pygame.font.SysFont('arial', (2*size)+24)
        if col == "bl":
            text_surface = arial.render(text, True, (0, 0, 0))
        else:
            text_surface = arial.render(text, True, col)
        return text_surface


    def display_welcome(self):
        """ Displays difficulty levels on pygame start up. """
        text_surface_welcome = self.create_text_surface("Welcome to Maze")
        text_surface_info = self.create_text_surface("Choose your preferred difficulty")
        self.window.blit(text_surface_welcome,(300,50))
        self.window.blit(text_surface_info,(225,150))

        rect_easy = pygame.Surface((200,150))
        rect_med = pygame.Surface((200,150))
        rect_hard = pygame.Surface((200,150))

        pygame.draw.rect(rect_easy, (0, 255, 0), (0, 0, 200, 150))
        pygame.draw.rect(rect_med, (255, 0, 0), (0, 0, 200, 150))
        pygame.draw.rect(rect_hard, (0, 0, 255), (0, 0, 200, 150))

        rect_easy.blit(self.create_text_surface("EASY 60s"),(45,65))
        rect_med.blit(self.create_text_surface("MEDIUM 45s"),(30,65))
        rect_hard.blit(self.create_text_surface("HARD 30s"),(45,65))
        

        self.window.blit(rect_easy.convert(),(50,500))
        self.window.blit(rect_med.convert(),(300,500))
        self.window.blit(rect_hard.convert(),(550,500))
        pygame.display.flip()
