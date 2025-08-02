import random
import pygame
import numpy as np

class Maze:
    def __init__(self, size):
        self.width = size
        self.height = size
        self.maze = np.ones((self.height, self.width))
        self.generate_maze()

    def generate_maze(self):
        stack = [(1, 1)]
        self.maze[1, 1] = 0

        while stack:
            x, y = stack[-1]
            dirs = [(0, -2), (0, 2), (-2, 0), (2, 0)]
            random.shuffle(dirs)

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1 and self.maze[ny][nx] == 1:
                    self.maze[ny, nx] = 0
                    self.maze[y + dy // 2][x + dx // 2] = 0
                    stack.append((nx, ny))
                    break
            else:
                stack.pop()

    def get_maze(self):
        return self.maze
    
class Wall():

    def __init__(self, scale):
        self.image = pygame.image.load("images/rock.jpg")
        self.cs = scale # cell size of game grid
        self.img_tf = pygame.transform.scale(self.image, (scale, scale))
        self.rect = self.img_tf.get_rect()