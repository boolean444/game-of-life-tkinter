from Gol_game import Grid
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

class Screen(tk.Canvas):
    def __init__(self):
        self.window_side_length = 300
        tk.Canvas.__init__(self, root, height=self.window_side_length, width=self.window_side_length)
        self.board = Grid()
        self.board.new_pattern('glider')
        self.ticks = 0
        self.factors_of_300 = [x for x in range(1, 151) if self.window_side_length%x == 0 and x < 151] # to get equal spacing of the squares on the grid
        self.action_state = 0  # can be only play (1) or pause (0)
        self.separation_length = 0
        self.moving_x = 0
        self.moving_y = 0
        self.slider = None
        self.play_pause = None
        self.patternlist = tk.StringVar()
        self.patternlist.set('clear')

        if self.action_state:
            self.tick()

    def todo(self, *action): # Either continue ticking or tick by user input
        if self.action_state:
            self.action_state = 0
            self.play_pause.config(text='Play')
        else:
            self.action_state = 1 # self.tick() is run in place_squares
            self.play_pause.config(text='Pause')

    def place_squares(self):
        self.delete('all')
        self.create_rectangle(0, 0, self.window_side_length, self.window_side_length, fill='black')

        if self.window_side_length % self.slider.get() != 0:  # To filter number so the scale number is a factor of 300 (To get equilateral squares)
            closest = sorted(self.factors_of_300, key=lambda x: abs(x - self.slider.get()))
            self.separation_length = self.window_side_length / closest[0]

        else:
            self.separation_length = self.window_side_length / self.slider.get()
        m = (self.board.position2 * self.separation_length) - 15 # to spread list to the left and up. The 15 is to give some space to zooming
        x = self.moving_x
        y = self.moving_y-m
        x2 = self.separation_length+self.moving_x
        y2 = self.separation_length+self.moving_y-m
        cube_array = self.board.current_grid # Using the Grid class
        for row in cube_array:
            for block in row:
                if block:
                    self.create_rectangle(x-m, y, x2-m, y2, fill='light green')

                if not block:
                    pass
                x += self.separation_length
                x2 += self.separation_length
            x = self.moving_x
            x2 = self.separation_length+self.moving_x
            y += self.separation_length
            y2 += self.separation_length

        if self.action_state:
            self.tick()
        self.after(10, self.place_squares)

    def tick(self):
        self.ticks += 1
        self.board.tick()

    def reverse_tick(self):
        self.board.tick_reverse()

    def start_over(self):
        self.ticks = 0
        self.board.start_over()

    def home(self):
        self.moving_x = 0
        self.moving_y = 0

        self.slider.set(25)

    def move(self, action):
        if action.keycode == 37:
            self.moving_x += 20
        elif action.keycode == 38:
            self.moving_y += 20
        elif action.keycode == 39:
            self.moving_x -= 20
        elif action.keycode == 40:
            self.moving_y -= 20

    def set_pattern(self):
        self.board.new_pattern(self.patternlist.get())


def main():
    canv = Screen()
    canv.grid(column=2)
    tk.Frame(root, width=100).grid(column=0)
    tk.Button(root, text='<', command=canv.reverse_tick).grid(column=2, row=1, sticky=tk.W)
    play_pause = tk.Button(root, text='Play', command=canv.todo)
    play_pause.grid(column=2, row=1)
    tk.Button(root, text='>', command=canv.tick).grid(column=2, row=1, sticky=tk.E)
    slider = tk.Scale(root, from_=1, to=150, orient=tk.HORIZONTAL)
    slider.grid(column=2)
    slider.set(25)
    options = tk.OptionMenu(root, canv.patternlist, 'clear', 'glider', 'glider 2', 'glider gun', 'random')
    options.grid(row=3, column=2)
    tk.Button(root, text='Go', command=canv.set_pattern).place(x=290, y=375)
    canv.play_pause = play_pause
    canv.slider = slider
    canv.place_squares()
    tk.Button(root, text='Start Over', command=canv.start_over).grid(column=2)
    tk.Button(root, text='Home', command=canv.home).grid(column=2)
    root.bind('<Down>', canv.move)
    root.bind('<Left>', canv.move)
    root.bind('<Right>', canv.move)
    root.bind('<Up>', canv.move)
    root.bind('<space>', canv.todo)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Conway\'s Game of Life')
    root.geometry('500x450')
    main()
    root.mainloop()
