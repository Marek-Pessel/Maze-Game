import pygame
from player import Player

class GUI():

    def __init__(self, maze, player, wall, cell_size, screen, buttons, dif, enemies):
        self.maze = maze    # 2D array
        self.player = player
        self.wall = wall
        self.cs = cell_size
        self.screen = screen
        self.buttons = buttons # list of buttons
        self.difficulty = dif
        self.enemies = enemies  # list of enemies
        if dif == 0:
            # remove 2 enemies
            self.enemies.pop(-1)
            self.enemies.pop(-1)
        elif dif == 1:
            # remove 1 enemy
            self.enemies.pop(-1)
        # else: leave all 3 enemies

        # define some RGB colors
        self.white = (255, 255, 255)
        self.menu_color = (200, 180, 180)   # light beighe
        self.solution_col = (120, 40, 240)   
        # load special images
        self.diamond_img = pygame.image.load("images/diamond.jpg")
        self.treasure_tf = pygame.transform.scale(self.diamond_img, (self.cs, self.cs))
        self.treasure_rect = self.treasure_tf.get_rect()
        self.treasure_rect.x = (len(maze)-2) * self.cs
        self.treasure_rect.y = (len(maze)-2) * self.cs

        # load special sounds
        self.walking = pygame.mixer.Sound("sounds/walking.mp3")

        self.sol_rect = pygame.Rect(0, 0, self.cs, self.cs)

    def draw_grid(self, menu, solution):

        # get grid span    
        span = len(self.maze)
        # fill all white
        self.screen.fill(self.white)
        
        # search for wall cells in 2D array
        for i, x in enumerate(range(0, span*self.cs, self.cs)):
            for j, y in enumerate(range(0, span*self.cs, self.cs)):

                if self.maze[j][i] == 1:
                    #add wall grafic
                    self.wall.rect.x = x
                    self.wall.rect.y = y
                    self.screen.blit(self.wall.img_tf, self.wall.rect)
        
        # print solution if called
        for cell in solution:
            self.sol_rect.x = cell[0] * self.cs
            self.sol_rect.y = cell[1] * self.cs
            pygame.draw.rect(self.screen, self.solution_col, self.sol_rect)

        # add treasure to grid
        self.screen.blit(self.treasure_tf, self.treasure_rect)

        # add figures to grid
        self.screen.blit(self.player.img_tf, self.player.rect)
        for enemy in self.enemies:
            self.screen.blit(enemy.img_tf, enemy.rect)

        # coloring menu space
        pygame.draw.rect(self.screen, self.menu_color, menu)

        # add buttons
        for button in self.buttons:
            button.draw(self.screen, self.difficulty)

    def move_figure(self, figure):

        dest_x, dest_y = figure.move()

        if self.validate_step(dest_x, dest_y):
            # play sound when player walked
            if type(figure) == Player and not figure.rect.topleft == (dest_x, dest_y):
                self.walking.play()
            figure.rect.x = dest_x
            figure.rect.y = dest_y
            figure.cnt = 0

        else:
            # change enemy direction
            try:
                # -2 for motion pattern (right,straight,left,turn)
                figure.direction -= 2
                # move again
                self.move_figure(figure)
            except:
                pass

    def validate_step(self, x, y) -> bool:
        cs = self.cs
        m = 2
        cell_topleft = (x // cs, y // cs)
        cell_topright = ((x+cs-m) // cs, y // cs)
        cell_bottomleft = (x // cs, (y+cs-m) // cs)
        cell_bottomright = ((x+cs-m) // cs, (y+cs-m) // cs)

        corners = [cell_topleft,
                   cell_topright,
                   cell_bottomleft,
                   cell_bottomright]
        for corner in corners:
            if self.maze[corner[1]][corner[0]] == 1: # colide with wall
                return False
        return True
    
    def show_start_menu(self, font):
        # text to image
        img = font.render('Choose mode!', True, (0,0,0))
        self.screen.blit(img, (635, 100))
        
class Button():

    def __init__(self, x=int, y=int, images=list, scale=float, name=str, settings=tuple):

        self.imgs = []
        for img in images:
            wdt = img.get_width()
            hgt = img.get_height()
            img_tf = pygame.transform.scale(img, (int(wdt*scale), int(hgt*scale)))
            img_rect = img_tf.get_rect()
            img_rect.x = x
            img_rect.y = y
            self.imgs.append((img_tf,img_rect))
        self.rect = None
        self.name = name
        self.settings = settings
        self.activate = False

    def draw(self, screen, dif):
        # draw easy button
        if self.name == 'easy':
            if dif == 0:
                self.rect = self.imgs[1][1]
                screen.blit(self.imgs[1][0], self.imgs[1][1])
            else:
                self.rect = self.imgs[0][1]
                screen.blit(self.imgs[0][0], self.imgs[0][1])
        
        #draw middle button
        elif self.name == 'middle':
            if dif == 1:
                self.rect = self.imgs[1][1]
                screen.blit(self.imgs[1][0], self.imgs[1][1])
            else:
                self.rect = self.imgs[0][1]
                screen.blit(self.imgs[0][0], self.imgs[0][1])
        
        # draw hard button
        elif self.name == 'hard':
            if dif < 2:
                self.rect = self.imgs[0][1]
                screen.blit(self.imgs[0][0], self.imgs[0][1])
            else:
                self.rect = self.imgs[dif-1][1]
                screen.blit(self.imgs[dif-1][0], self.imgs[dif-1][1])
    
    def check_clicked(self, pos) -> bool:
        if self.rect.collidepoint(pos):
            self.activate = True
        else:
            self.activate = False