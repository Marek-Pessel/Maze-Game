import pygame
import random

class Figure():
    def __init__(self, image, scale):
        self.image = image
        self.cs = scale # cell size of game grid in pixel
        self.img_tf = pygame.transform.scale(self.image, (scale, scale))
        self.rect = self.img_tf.get_rect()
        self.cnt = 0

class Player(Figure):

    def __init__(self, image, scale):

        super().__init__(image, scale)
        # starting position
        self.rect.x = scale
        self.rect.y = scale

    def move(self) -> int:
        key = pygame.key.get_pressed()     # sign of the pressed key
        dest_x = self.rect.x    # might be updated
        dest_y = self.rect.y    # might be updated

        if key[pygame.K_d]: 
            dest_x += self.cs     # move right
        elif key[pygame.K_a]:
            dest_x -= self.cs     # move left
        elif key[pygame.K_s]:
            dest_y += self.cs     # move down
        elif key[pygame.K_w]:
            dest_y -= self.cs     # move up
        
        return dest_x, dest_y
    
class Enemy(Figure):

    def __init__(self, image, scale):

        super().__init__(image, scale)
        self.rect.x = 0
        self.rect.y = 0
        # randomized starting direction
        self.direction = random.randint(0,3)

    def move(self) -> int:

        dest_x = self.rect.x    # might be updated
        dest_y = self.rect.y    # might be updated

        # try to move right relative to old direction
        self.direction += 1
        if self.direction == 4:
            self.direction = 0
        if self.direction == -1:
            self.direction = 3

        # calculate destination coords
        if self.direction == 0: 
            dest_x += self.cs   # move right
        elif self.direction == 1:
            dest_y += self.cs   # move down
        elif self.direction == 2:
            dest_x -= self.cs   # move left
        elif self.direction == 3:
            dest_y -= self.cs   # move up
        
        return dest_x, dest_y

    def set_start_pos(self, maze, dest_pos):
        print
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        if maze[dest_pos[1]][dest_pos[0]] == 1: # figure is on wall
            for dir in directions:
                n_dest_pos = (dest_pos[0]+dir[0], dest_pos[1]+dir[1])

                if maze[n_dest_pos[1]][n_dest_pos[0]] == 0: # cell is a way
                    dest_pos = n_dest_pos
                    break
        
        self.rect.x = dest_pos[0] * self.cs
        self.rect.y = dest_pos[1] * self.cs

        print(dest_pos)