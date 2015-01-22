#### "conways_game_of_life.py"
#### Grace Hadiyanto
#### CS439 FA14

import sys

class Cell:
    __slots__ = {'_alive', '_successor_state', '_neighbors'}
    def __init__(self):
        # _alive is a bool representing current state of the cell
        self._alive = False
        self._successor_state = None
        self._neighbors = []

    @property
    def alive(self):
        """I'm the 'alive' property"""
        return self._alive
    @alive.setter
    def alive(self, state):
        self._alive = state

    @property
    def neighbors(self):
        """I'm the 'neighbors' property"""
        return self._neighbors
    @neighbors.setter
    def neighbors(self, list_of_neighbors):
        self._neighbors = list_of_neighbors

    @property
    def successor_state(self):
        """I'm the 'successor_state' property"""
        return self._successor_state
    @successor_state.setter
    def successor_state(self, state):
        self._successor_state = state

    def count_live_neighbors(self):
        # Have the cell look around to see how many of their neighbors are
        # currently alive.
        count = 0
        for neighbor in self._neighbors:
            if neighbor.alive:
                count += 1
        return count
    
    def prepare_transition(self):
        # Have the cell prepare to transition by applying the rules of the
        # game and setting their successor state.
        live = True
        die = False
        live_neighbors = self.count_live_neighbors()
        if self.alive:
            if live_neighbors < 2:
                self._successor_state = die
            elif live_neighbors == 2 or live_neighbors == 3:
                self._successor_state = live
            else:
                self._successor_state = die
        else:
            if live_neighbors == 3:
                self._successor_state = live
            else:
                self._successor_state = die
        
    def transition(self):
        # If the successor state is different than the current state, then
        # transition into the successor state.
        if self._successor_state != self.alive:
            self.alive = self._successor_state
            # Flush the successor state since we've consumed it
            self._successor_state = None

    def __str__(self):
        if self.alive:
            return 'o'
        else:
            return '.'

class LifeField:
    __slots__ = {'field'}
    def __init__(self, seed):
        # Create a field of 20 rows by 60 columns, each row representing
        # a y coordinate and each column representing an x coordinate.
        self.field = [[Cell() for col in range(60)] for row in range(20)]
        self.find_cell_neighbors()
        # Set the cells described by coordinates in the seed to be alive.
        for x, y in seed:
            self.field[y][x].alive = True

    def find_cell_neighbors(self):
        # Have each cell get to know their neighbors!
        for y in range(20):
            for x in range(60):
                neighbors  = adjacent_coordinates(y,x)
                for neighbor_y, neighbor_x in neighbors:
                    self.field[y][x].neighbors.append(self.field[neighbor_y][neighbor_x])

    def prepare_for_transition(self):
        # Prepare the life field to transition to the next state by preparing
        # each cell for transition into their successor state.
        for y in range(20):
            for x in range(60):
                self.field[y][x].prepare_transition()

    def simulate_tick(self):
        # Simulate simultaneous births and deaths of cells by having each cell
        # transition.
        self.prepare_for_transition()
        for y in range(20):
            for x in range(60):
                self.field[y][x].transition()
  
    def __str__(self):
        s = ''
        for y in range(20):
            for x in range(60):
                s += str(self.field[y][x])
            s += '\n'
        return s

def adjacent_coordinates(y,x):
    # Calculate legal adjacent coordinates for a given (y, x) coordinate pair
    legal_adjacent_coordinates = []
    if y-1 >= 0:
        legal_adjacent_coordinates.append((y-1,x))
        if x-1 >= 0:
            legal_adjacent_coordinates.append((y-1,x-1))
        if x+1 <= 59:
            legal_adjacent_coordinates.append((y-1,x+1))
    if y+1 <= 19:
        legal_adjacent_coordinates.append((y+1,x))
        if x-1 >= 0:
            legal_adjacent_coordinates.append((y+1,x-1))
        if x+1 <= 59:
            legal_adjacent_coordinates.append((y+1,x+1))
    if x-1 >= 0:
        legal_adjacent_coordinates.append((y,x-1))
    if x+1 <= 59:
        legal_adjacent_coordinates.append((y,x+1))
    return legal_adjacent_coordinates
    
def parse_file(file_name):
    x_coordinates = []
    y_coordinates = []
    input_file = open(file_name, 'r')
    input_file.readline()
    for line in input_file:
        coordinate = line.split()
        x_coordinates.append(int(coordinate[0]))
        y_coordinates.append(int(coordinate[1]))
    return x_coordinates, y_coordinates

def translate_points(x_coordinates, y_coordinates):
    minimum_x = min(x_coordinates)
    minimum_y = min(y_coordinates)
    translated_x = [x - minimum_x for x in x_coordinates]
    translated_y = [y - minimum_y for y in y_coordinates]
    return translated_x, translated_y

def main():

    if len(sys.argv) != 3:
        print('Required usage: python3 conways_game_of_life.py <filename> <n>')
        print('Where filename is the name of a Life 1.06 file, and n is the',end='')
        print(' number of generations you want to play.')
        exit()

    # Collect command line arguments
    filename = sys.argv[1]
    n = int(sys.argv[2])

    # Parse file and gather coordinates, and translate them
    x_coordinates, y_coordinates = parse_file(filename)
    x_coordinates, y_coordinates = translate_points(x_coordinates, y_coordinates)

    # Pair coordinates together to create the seed for the life game
    seed = []
    for i in range(len(x_coordinates)):
        seed.append((x_coordinates[i],y_coordinates[i]))

    # Give birth to the game and print an initial view
    game = LifeField(seed)
    print('TIME STEP 0')
    print(game,end='\n\n')

    # Play the game for the next n-1 generations!!!
    for i in range(1,n):
        print('TIME STEP {}'.format(i))
        game.simulate_tick()
        print(game, end='\n\n')

if __name__ == '__main__':
    main()
