# Readme: MazeGame
MazeGame is a fun and exciting maze-based game where players must find a path through a randomly generated maze to reach a treasure placed opposite their starting position. Along the way, they must avoid enemies and can use limited tools to manipulate the maze in their favor. Sound effects and background music are integrated to enhance immersion — including movement sounds, treasure pickup sounds, and an enemy attack sound.

MazeGame was developed in Python and uses the following external libraries:

    pygame, numpy

## Installation

To run the game, make sure you have Python 3.x installed, then install the required packages using pip:

pip install -r requirements.txt

requirements.txt example:

pygame
numpy

## Controls

Use the following keyboard controls to navigate and interact with the maze:
Key(s):	                        Action:

W, A, S, D	                    Move the player up, left, down, right

move+O	                        Use a pickaxe to remove a wall
                                (if any pickaxes are left)

Shift       	                Highlight the path from your current Position
                                to the treasure (cheat/debug feature)

## Rules
    Each round, a new maze is generated randomly using a depth-first algorithm.

    The goal is to reach the treasure while avoiding enemies that patrol the maze.

    The number of enemies and maze size increase with the selected difficulty level:

    Easy Mode:      1 enemy, small maze

    Medium Mode:    2 enemies, medium-sized maze

    Hard Mode:      3 enemies, large maze

In Hard Mode enemy speed increases by one unit for each diamond you collect, making the game progressively harder.

## Special Abilities

Players have 3 pickaxes available per game.

Pickaxes can be used to break down a wall and create a path — useful for escaping tight spots.

If the player is caught by an enemy:

     Collected diamonds reset to 0

     Pickaxes are refilled to 3

## User Interface

A panel on the right side of the screen allows you to:

        Select the difficulty mode via buttons

        View the number of remaining pickaxes

        Track the number of collected diamonds without dying

## Sound Effects & Audio

To enhance the gaming experience, MazeGame includes immersive sound design:

## Sound Event	Description

Background Music	        A continuous soundtrack plays during
                            gameplay

Movement Sound	            Plays each time the player moves

Diamond Sound	            Triggered when a diamond is collected

Death Sound	                Plays when the player is eaten by an enemy

These sound effects make the game feel more alive and help give audio cues about game events and danger.

## Technical Details

    Maze generation uses a Depth-First Search (DFS) algorithm.

    Game difficulty dynamically affects:

        Enemy count

        Maze size

## Developers

### This project was developed by:

    Marek Pessel – [GUI interface, Solver Algorithm, Main]

    Bela Rung – [Maze generator, Player and Enemies]

    No known bugs. The game runs smoothly across multiple difficulty levels.