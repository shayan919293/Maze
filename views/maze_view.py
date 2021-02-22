import pygame
import time
from views.main_window_view import MainWindow

class MazeView(MainWindow):

    """ Displays the maze and asks for user input to move the player. 

        Tells player when they have won or lost the game.
    """
    def __init__(self, maze_obj) -> None:
        """ Initializes the MazeView class with the attribute maze_obj. """ 
        super().__init__()
        self._maze = maze_obj
        self.timer_limit = 0
        self.remaining_time = self.timer_limit
        self.base_font_size_increaser = 0
        self.score = 0
        
        
    def on_maze_init(self):
        self.game_tab = pygame.Surface((3/5*self.window_width,self.window_height))
        self.result_tab = pygame.Surface((2/5*self.window_width,self.window_height))

        self.walls = pygame.transform.scale(pygame.image.load('models/images/brick.png').convert(), (27, 27))
        self.walls.set_colorkey((0,0,0))

        self.player = pygame.transform.scale(pygame.image.load('models/images/mario.png').convert(), (27, 27))
        self.player.set_colorkey((0,0,0))
        
        self.backpack = pygame.transform.scale(pygame.image.load('models/images/backpack.png').convert(), (27, 27))
        self.backpack.set_colorkey((0,0,0))
        
        self.exitdoor = pygame.transform.scale(pygame.image.load('models/images/exitdoor.png').convert(), (27, 27))
        self.exitdoor.set_colorkey((0,0,0))
 
        self.banana = pygame.transform.scale(pygame.image.load('models/images/banana.png').convert(), (27, 27))
        self.banana.set_colorkey((0,0,0))
        
        self.cherry = pygame.transform.scale(pygame.image.load('models/images/cherry.png').convert(), (27, 27))
        self.cherry.set_colorkey((0,0,0))
        
        self.peach = pygame.transform.scale(pygame.image.load('models/images/peach.png').convert(), (27, 27))
        self.peach.set_colorkey((0,0,0))
        
        self.apple = pygame.transform.scale(pygame.image.load('models/images/apple.png').convert(), (27, 27))
        self.apple.set_colorkey((0,0,0))
        
        self.orange = pygame.transform.scale(pygame.image.load('models/images/orange.png').convert(), (27, 27))
        self.orange.set_colorkey((0,0,0))

        self.check = pygame.transform.scale(pygame.image.load('models/images/check.png').convert(), (27, 27))
        self.check.set_colorkey((0,0,0))
        
        self.uncheck = pygame.transform.scale(pygame.image.load('models/images/uncheck.png').convert(), (27, 27))
        self.uncheck.set_colorkey((0,0,0))

        self.time = time.time()
    
    def item_size(self):
        return 27

    def item_pos(self,x,y):
        return ((x+1)*self.item_size(),(y+1)*self.item_size())

    @property
    def maze(self)-> object:
        """ Getter for maze objects. """
        return self._maze

    def create_text_surface(self,text,size=0,col="bl"):
        """ Creates a text surface for pygame. """
        arial = pygame.font.SysFont('arial', (2*size)+24)
        if col == "bl":
            text_surface = arial.render(text, True, (0, 0, 0))
        else:
            text_surface = arial.render(text, True, col)

        return text_surface

    def display_maze(self)-> None:
        """ Prints the maze details. """
        running = True
        while running:
            self.window.fill((255,255,255))
            # 128,128,128 or 169,169,169
            self.game_tab.fill((255,255,255))

            #maze reader
            for idy,row in enumerate(self.maze.rows):
                for idx,col in enumerate(row):
                    if col == "X" or col == "x":
                        image = self.walls
                        self.game_tab.blit(image,self.item_pos(idx,idy))
                    if col == "P":
                        image = self.player
                        self.game_tab.blit(image,self.item_pos(idx,idy))
                    if col == "E":
                        image = self.exitdoor
                        self.game_tab.blit(image,self.item_pos(idx,idy))
                    if col == "banana":
                        image = self.banana
                        self.game_tab.blit(image,self.item_pos(idx,idy))
                    if col == "cherry":
                        image = self.cherry
                        self.game_tab.blit(image,self.item_pos(idx,idy))
                    if col == "apple":
                        image = self.apple
                        self.game_tab.blit(image,self.item_pos(idx,idy))
                    if col == "peach":
                        image = self.peach
                        self.game_tab.blit(image,self.item_pos(idx,idy))
                    if col == "orange":
                        image = self.orange
                        self.game_tab.blit(image,self.item_pos(idx,idy))
            #showing items in backpack
            self.backpack_printer()

            #showing instructions
            self.instructions_printer()

            #attaching game and result tabs on window
            self.window.blit(self.game_tab,(0,0))
            self.window.blit(self.result_tab,(3/5*self.window_width,0))
            self.result_tab.fill((255,255,255))

            #Timer ->
            time_diff = time.time()-self.time
            if time_diff >= self.timer_limit: raise SystemExit("Time up")
            self.remaining_time = self.timer_limit - int(time_diff)
            if self.remaining_time <= 10:
                my_text_surface = self.create_text_surface("Time Left: "+str(self.remaining_time),size=10-self.remaining_time,col=(255,0,0))
                
            else:
                my_text_surface = self.create_text_surface("Time Left: "+str(self.timer_limit-int(time_diff)))
            self.result_tab.blit(my_text_surface,(40,40))
            
            #flip the display
            pygame.display.flip()
            running = False

        
    def backpack_printer(self):
        """ Displays the items in the players backpack on the screen. """
        self.result_tab.blit(self.backpack,(0,200))
        self.result_tab.blit(self.create_text_surface("{",-1),(32,200))
        for index,item in enumerate(self.maze.player.backpack):
            if item == "banana":
                image = self.banana
                self.result_tab.blit(image,(((index+1)*27+20),200))
            if item == "cherry":
                image = self.cherry
                self.result_tab.blit(image,(((index+1)*27+20),200))
            if item == "apple":
                image = self.apple
                self.result_tab.blit(image,(((index+1)*27+20),200))
            if item == "peach":
                image = self.peach
                self.result_tab.blit(image,(((index+1)*27+20),200))
            if item == "orange":
                image = self.orange
                self.result_tab.blit(image,(((index+1)*27+20),200))
        self.result_tab.blit(self.create_text_surface("}",-1),(190,200))

        #little check mark next to backpack
        if len(self._maze.player.backpack) == len(self._maze.objects):
            self.result_tab.blit(self.check,(210,200))
            self.result_tab.blit(self.create_text_surface("HURRY! YOU ARE DONE! GO TO EXIT ASAP",-5,(255,0,0)),(0,240))
        else:
            self.result_tab.blit(self.uncheck,(210,200))
            self.result_tab.blit(self.create_text_surface(f"{len(self._maze.objects) - len(self._maze.player.backpack)} items left on maze",-5),(0,240))


    def instructions_printer(self):
        """ Displays maze instructions. """
        self.result_tab.blit(self.create_text_surface("INSTRUCTIONS:"),(0,400))
        self.result_tab.blit(self.create_text_surface("Press 'b' to break walls around you.",-4),(0,430))
        self.result_tab.blit(self.create_text_surface("NOTE that by breaking walls you'll",-4,(255,0,0)),(0,450))
        self.result_tab.blit(self.create_text_surface("get 5s penalty",-4,(255,0,0)),(0,470))
        self.result_tab.blit(self.create_text_surface("Use arrow keys to move around.",-4),(0,490))
        self.result_tab.blit(self.create_text_surface("Use q to exit the game.",-4),(0,510))

    def score_printer(self,score):
        """ Displays player score. """ 
        self.result_tab.blit(self.create_text_surface(f"Score: {score}",0,(0,0,255)),(0,600))
        
        

