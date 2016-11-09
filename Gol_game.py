import numpy as np
import random
class Grid(object):
    def __init__(self):
        self.current_grid = np.zeros((150,150))
        self.section_tobe_evaluated = 0
        self.size = 2
        self.pattern = 'clear'
        self.position = 0
        self.position2 = 0
        self.past_ticks = []

    def new_pattern(self, pattern):
        self.position2 = 0
        current_grid = np.zeros((150, 150))
        if pattern == 'glider':
            glider = [[0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0]]
            current_grid[11:16, 11:16] = glider
            self.size = 2
            self.current_grid = current_grid
        elif pattern =='glider 2': # found on http://pentadecathlon.com/lifenews/
            glider2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                       [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                       [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                       [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            self.size = 8
            current_grid[10:18, 9:19] = glider2
            self.current_grid = current_grid
        elif pattern == 'glider gun':
            glider_gun = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                          [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            current_grid[13: 24, 13: 51] = glider_gun
            self.size = 36
            self.current_grid = current_grid
        elif pattern == 'random':
            rand_sect1 = random.randint(0, 5)
            rand_sect2 = random.randint(6, 100)
            sect = current_grid[rand_sect1:rand_sect2, rand_sect1:rand_sect2]
            for y in range(len(sect)):
                for x in range(len(sect)):
                    sect[y][x] = random.choice([1, 0])
            self.current_grid = current_grid[rand_sect1:rand_sect2, rand_sect1:rand_sect2]
        elif pattern == 'clear':
            self.current_grid = current_grid
        else:
            return
        self.pattern = pattern

    def start_over(self):
        self.position2 = 0
        self.new_pattern(self.pattern)

    def tick(self):
        self.expand()
        next_grid = np.zeros((self.size+ self.position,self.size+self.position))
        current_grid = self.current_grid.tolist() # not using numpy functions because slows process down
        for i in xrange(self.section_tobe_evaluated[2]-2, self.section_tobe_evaluated[3]+2):
            for i2 in xrange(self.section_tobe_evaluated[0]-2,self.section_tobe_evaluated[1]+2):
                neighbors = 0
                try:
                    current_state = current_grid[i][i2] # Can be either 1 or 0
                except IndexError:
                    current_state = 0
                try:
                    neighbors += current_grid[i + -1][i2 + -1]
                    neighbors += current_grid[i + -1][i2 + 0]
                    neighbors += current_grid[i + -1][i2 + 1]
                    neighbors += current_grid[i + 0][i2 + -1]
                    neighbors += current_grid[i + 0][i2 + 1]
                    neighbors += current_grid[i + 1][i2 + -1]
                    neighbors += current_grid[i + 1][i2 + 0]
                    neighbors += current_grid[i + 1][i2 + 1]
                except IndexError:
                   continue

                next_grid[i+self.position][i2+self.position] = 1 if current_state and (neighbors == 2 or neighbors == 3) else (1 if neighbors == 3 else 0)
        self.current_grid = next_grid

        self.past_ticks.append(self.live_cells()) # for tick reverse

    def tick_reverse(self):
        next_grid = np.zeros((self.size, self.size))
        try:
            past_tick_grid = self.past_ticks[-1] # 'coordinates' of active cells of past boards
            for tup in past_tick_grid:
                next_grid[tup[0]][tup[1]] = 1
            del self.past_ticks[-1]
            self.current_grid = next_grid
        except IndexError:
            pass
        if len(self.past_ticks) > 100:
            del self.past_ticks[0]

    def expand(self):
        """Stretching list to keep up with the amount of space the living cells take up. This function also
            determines what part of the array to evaluate. After the section of the list that needs to be evaluated
            is determined, the tick function evaluates the section and "puts it back" into the original array."""
        live = self.live_cells()
        live_x = [x[1] for x in live]
        live_y = [y[0] for y in live]
        try:
            min_x = min(live_x)
            min_y = min(live_y)
            max_x = max(live_x)
            max_y = max(live_y)
            self.position = 1 if min_x == 0 or min_y == 0 else 0
            self.position2 += 1 if min_x == 0 or min_y == 0 else 0
            live_max_overall = max(max_x, max_y) + 3
            self.size = live_max_overall
            self.section_tobe_evaluated = (min_x, max_x + 1, min_y, max_y + 1)
        except ValueError:
            pass

    def live_cells(self):
        living = []
        for y, row in enumerate(self.current_grid):
            for x, cell in enumerate(row):
                if cell:
                    living.append((y, x))
        return living