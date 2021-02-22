from views.maze_view import MazeView
from views.welcome_view import WelcomeView
from views.ending_view import EndingView
import pygame, pygame.locals, json


class MazeController:
    """ This is the maze controller.

        Uses MazeView. 

        Valid actions in this controller are:
            Left arrow: will move left one space
            Down arrow: will move down one space
            Up arrow: will move up one space
            Right arrow: will move back one space
            b key: will break all walls around the player
            'End': will end the game
            'end': will end the game
    """

    def __init__(self,maze_obj) -> None:
        """ Initializes the MazeController class.

            Inserts the player start, end, and objects into random locations in the maze.
        
            Displays the maze.
        """
        self._maze = maze_obj
        self.maze.object_inserter(self.maze.objects)
        self.maze.object_inserter("P")
        self.maze.object_inserter("E")
        self._view = MazeView(self.maze)
        self._welcome = WelcomeView()
        self._ending = EndingView()
        self.score = 0
        self.difficulty = None


    @property
    def maze(self)->object:
        """ Getter for self._maze. """
        return self._maze


    def run(self):
        """ main running method of the class.
        controls running of different pages """
        self.run_welcome()
        self.run_maze()
        self.run_ending()
        raise SystemExit("Done")
        
    def run_welcome(self):
        """ Controller for start up screen.
        
            Displays maze level difficulty. 
        """
        welcome_hold = True
        while welcome_hold:
            self._welcome.display_welcome()
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    welcome_hold = False
                    raise SystemExit("Quit game")
                elif event.type == pygame.MOUSEBUTTONUP: 
                    pos = pygame.mouse.get_pos()
                    if pos[0]in range(50,250) and pos[1] in range(500,650):
                        self._view.timer_limit = 60
                        self.difficulty = "easy"
                        welcome_hold = False
                    if pos[0]in range(300,500) and pos[1] in range(500,650):
                        self._view.timer_limit = 45
                        self.difficulty = "medium"
                        welcome_hold = False
                    if pos[0]in range(550,750) and pos[1] in range(500,650):
                        self._view.timer_limit = 30
                        self.difficulty = "hard"
                        welcome_hold = False



    def run_maze(self):
        """ Controller for the keys the player can use.

            Key Events:
                q: quit the game
                b: break wall
                up arrow: move up one space
                down arrow: move down one space
                left arrow: move left one space
                right arrow: move right one space
        """
        self._view.on_maze_init()
        game_on = True
        self._view.display_maze()
        while game_on:
            # Event loop - quit if closed or 'escape' is pressed
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    self._view.ending()
                    raise SystemExit("end of game")
                
                elif event.type == pygame.locals.KEYDOWN:
                    if event.key == pygame.locals.K_q:
                        #quit the game
                        game_on = False

                    if event.key == pygame.locals.K_b:
                        #calls wallbreaker
                        self.wall_breaker(self.maze.player_loc)
                        self._view.timer_limit -= 5

                    if event.key == pygame.locals.K_RIGHT:
                        new_loc =  [self.maze.player_loc[0],self.maze.player_loc[1]+1]
                        game_on = self.play(new_loc)
                    if event.key == pygame.locals.K_LEFT:
                        new_loc =  [self.maze.player_loc[0],self.maze.player_loc[1]-1]
                        game_on = self.play(new_loc)
                    if event.key == pygame.locals.K_UP:
                        new_loc =  [self.maze.player_loc[0]-1,self.maze.player_loc[1]]
                        game_on = self.play(new_loc)
                    if event.key == pygame.locals.K_DOWN:
                        new_loc =  [self.maze.player_loc[0]+1,self.maze.player_loc[1]]
                        game_on = self.play(new_loc)
            self.score_calc()
            self._view.display_maze()


    def play(self,new_loc):
        """ Checks the new location that player wants to go.

            If the new location has an object, the player will pick it up and move to that position.

            If the player moves to the exit location, the game will exit.
        """
        if self.maze.can_move_to(new_loc[0],new_loc[1]):
            if self.maze.is_exit(new_loc[0],new_loc[1]):
                return False
            else:
                if self.maze.is_item(new_loc[0],new_loc[1]):
                    self.maze.object_picker(new_loc[0],new_loc[1])
                    self.maze.player_mover(new_loc,self.maze.player_loc)
                else:
                    self.maze.player_mover(new_loc,self.maze.player_loc)
        return True


    def wall_breaker(self,location):
        """ Uses player location to change a wall to an empty space.
           breaks all walls around the player
        """
        if self._maze.rows[location[0]][location[1]+1] == "x": self._maze.rows[location[0]][location[1]+1] = " "
        if self._maze.rows[location[0]+1][location[1]] == "x": self._maze.rows[location[0]+1][location[1]] = " "
        if self._maze.rows[location[0]][location[1]-1] == "x": self._maze.rows[location[0]][location[1]-1] = " "
        if self._maze.rows[location[0]-1][location[1]] == "x": self._maze.rows[location[0]-1][location[1]] = " "
        if self._maze.rows[location[0]-1][location[1]-1] == "x": self._maze.rows[location[0]-1][location[1]-1] = " "
        if self._maze.rows[location[0]+1][location[1]+1] == "x": self._maze.rows[location[0]+1][location[1]+1] = " "
        if self._maze.rows[location[0]-1][location[1]+1] == "x": self._maze.rows[location[0]-1][location[1]+1] = " "
        if self._maze.rows[location[0]+1][location[1]-1] == "x": self._maze.rows[location[0]+1][location[1]-1] = " "


    def score_calc(self):
        """ Calculates score based on difficulty chosen by player. """
        score = 0
        if self.difficulty == "hard": score+= 2000
        if self.difficulty == "medium": score+= 1000
        if self.difficulty == "easy": score+= 500
        score -= (self._view.timer_limit-self._view.remaining_time)*5
        score *= len(self.maze.player.backpack)
        self._view.score_printer(score)
        self.score = score


    def write_to_json(self,name):
        """ writes the new score to score.json file if it's already been created. 
        if not, it creates and appends the new score
        """
        try:
            with open("scores.json", "r") as file:
                py_data = json.load(file)
                py_data.append({"name":name,"score":self.score})
                with open("scores.json","w") as json_file:
                    json.dump(py_data,json_file)
        except:
            with open("scores.json","w") as file:
                json.dump([{"name":name,"score":self.score}],file)
    

    def run_ending(self):
        """ Displays ending windows
            Gets user input for high score. 
            Appends the user input to the web application.
            User can press all keys on keyboard + capslock/backspace/space/enter to enter the name.
            the name and the score will be posted to score.json file by calling write_to_json method
        """
        name = ""
        ending_run = True
        capslock = False
        won = False
        if len(self.maze.objects) == len(self.maze.player.backpack):
            won = True

        while ending_run:
            self._ending.display_ending(name,self.score,capslock,won)
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    ending_run = False
                    raise SystemExit("done")
                elif event.type == pygame.locals.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        ending_run = False
                    elif event.key == pygame.K_CAPSLOCK:
                        if capslock:
                            capslock = False
                        else:
                            capslock = True
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(pygame.key.name(event.key)) == 1:
                            key = pygame.key.name(event.key)
                            if capslock:
                                key = pygame.key.name(event.key).upper()
                            name += key
                        elif pygame.key.name(event.key)=="space":
                            name += " "
        
        self.write_to_json(name)

