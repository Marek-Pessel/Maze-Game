import pygame
from pygame import mixer
from maze_generator import Maze, Wall
from player import Player, Enemy
from gui import GUI, Button
import utils
import path_solver
import time

# define window parameter
cell_size = 26
menu_size = 250
window_hgt = 621
window_wdt = 621 + menu_size

# initialize pygame window
pygame.init()   
pygame.display.set_caption("MazeGame")

# load images
easy_img = [pygame.image.load("images/easy.jpg"),
            pygame.image.load("images/easy_clicked.jpg")]

middle_img = [pygame.image.load("images/middle.jpg"),
              pygame.image.load("images/middle_clicked.jpg")]

hard_img = [pygame.image.load("images/hard.jpg"),
            pygame.image.load("images/hard_clicked.jpg")]

player_img = pygame.image.load("images/player.jpg")
enemy_img = pygame.image.load("images/enemy.jpg")

# load sounds and music
mixer.music.load("sounds/background_music.mp3")
diamond_sound = mixer.Sound("sounds/diamond.mp3")
eaten_sound = mixer.Sound("sounds/eaten.mp3")

# start background sound

mixer.music.play(-1) # -1 for endless loop
mixer.music.set_volume(0.2)

difficulty = 0  # difficulty easy as default when starting the game


### GAME LOOP ###
run = True
while run:
    # initialize objects
    size = int(window_hgt / cell_size)
    maze = Maze(size).get_maze()

    player = Player(player_img, cell_size)

    enemy1 = Enemy(enemy_img, cell_size)
    enemy1.set_start_pos(maze, (int(size*0.25), int(size*0.75)))
    enemy2 = Enemy(enemy_img, cell_size)
    enemy2.set_start_pos(maze, (int(size*0.75), int(size*0.25)))
    enemy3 = Enemy(enemy_img, cell_size)
    enemy3.set_start_pos(maze, (int(size*0.75), int(size*0.75)))
    enemies = [enemy1, enemy2, enemy3]

    wall = Wall(cell_size)

    easy_bt = Button(665, 124, easy_img, 0.3, 'easy', (0, 27))
    middle_bt = Button(647, 248, middle_img, 0.3, 'middle', (1, 23))
    hard_bt = Button(663, 372, hard_img, 0.3, 'hard', (2, 20))
    buttons = [easy_bt, middle_bt, hard_bt]

    screen = pygame.display.set_mode((window_wdt, window_hgt))
    gui = GUI(maze, player, wall, cell_size, screen, buttons, difficulty, enemies)
    menu = pygame.Rect(window_wdt-menu_size, 0, menu_size, window_hgt)
    clock = pygame.time.Clock()

    ### MAIN LOOP ###

    finished = False
    while not finished:

        # check win condition
        if utils.check_finished(player.rect, gui.treasure_rect):
            mixer.music.pause()
            diamond_sound.play()
            time.sleep(1.5)
            mixer.music.play(-1)
            break

        # handle user activity
        for event in pygame.event.get():
            utils.event_handler(event, gui)

        # check if a button was clicked
        for button in gui.buttons:
            if button.activate:
                difficulty, cell_size = button.settings
                finished = True # restarting game with new settings

        # moving player
        if player.cnt == 5:
            gui.move_figure(player)
        else:
            player.cnt += 1

        # moving enemies
        for enemy in gui.enemies:
            if enemy.cnt == 15 - difficulty:
                gui.move_figure(enemy)
            else:
                enemy.cnt += 1
        
        # need to show the way?
        key = pygame.key.get_pressed()
        if key[pygame.K_LSHIFT]:
            curr_pos = player.rect.center
            curr_pos = (int(curr_pos[0]/cell_size), int(curr_pos[1]/cell_size))
            solution = path_solver.solve_maze(maze,curr_pos)
        else:
            solution = []

        gui.draw_grid(menu, solution)

        # cought player?
        if utils.cought_player(player.rect, enemies):
            mixer.music.pause()
            eaten_sound.play()
            time.sleep(2)
            mixer.music.play(-1)
            break

        pygame.display.update()
        clock.tick(30)