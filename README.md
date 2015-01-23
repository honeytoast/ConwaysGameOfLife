# ConwaysGameOfLife
A project for Theory of Computability class that simulates Conway's Game of Life

Included files:

Filename | Description
---------|-------------
conways_game_of_life.py|python3 program that simulates Conway's Game of Life
gosperglidergun_106.lif|sample life1.06 file that initializes the game board for the gosper glider gun pattern
sampleout|sample output of the gosper slider gun pattern with 20 steps

**How to run:**

python3 conways_game_of_life.py {filename} {n}

Where filename is the name of a Life 1.06 file, and n is the number of generations to play.

About the project:

Conway's Game of life is a mathematical simulation of a colony of single-celled organisms.
It is based upon the principles of DFA(Deterministic Finite Automata).

The game board is a grid of squares. Each square represents a cell, which may be alive or dead.
For the sake of simplicity, this program's game board will always have a 20 row x 60 column grid.
Each cell in the grid can be thought of as a DFA with two states, alive or dead, and changes state according to the amount of its live neighbors.

The program will translate the coordinates from the given life file, and sets the corresponding translated cells to be alive. The program then simulates each round of the game by printing the step number, printing the current state of the board, with the character "O" for each live cell, and the character "." for each dead cell, and advancing the state of the grid to the next time step, according to the game rules.

More information about the game and its rules can be found here: http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
