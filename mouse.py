class Mouse:

    def __init__(self, turtle, maze):
        self.donatelo = turtle
        self.maze = maze

        self.position = (0, 0)
        self.positions_options = {}
        self.choice_place = []
        self.direction = 'none'
        self.path = []

    def prepare_turtle(self, width, color, shape):
        self.donatelo.shape(shape)
        self.donatelo.color(color)
        self.donatelo.pensize(width)

    def set_start(self, tuple_position):
        self.donatelo.penup()
        self.donatelo.setpos(tuple_position)
        self.donatelo.pendown()

    def look_arround(self):
        return [self.maze.horizontal[self.position[1]][self.position[0]],
                self.maze.vertical[self.position[0]+1][self.position[1]],
                self.maze.horizontal[self.position[1]+1][self.position[0]],
                self.maze.vertical[self.position[0]][self.position[1]]]

    def how_many_choices(self):
        choices = 0
        for option in self.positions_options.get(self.position):
            if option == 0:
                choices += 1

        return choices

    def set_direction(self, new_direction):
        if self.direction == 'none':
            if new_direction == 'up':
                self.donatelo.left(90)
            elif new_direction == 'right':
                # Donatelo it is already turned right
                pass
            elif new_direction == 'down':
                self.donatelo.right(90)
            elif new_direction == 'left':
                self.donatelo.left(180)

        elif self.direction == 'up':
            if new_direction == 'right':
                self.donatelo.right(90)
            elif new_direction == 'down':
                self.donatelo.right(180)
            elif new_direction == 'left':
                self.donatelo.left(90)

        elif self.direction == 'right':
            if new_direction == 'up':
                self.donatelo.left(90)
            elif new_direction == 'down':
                self.donatelo.right(90)
            elif new_direction == 'left':
                self.donatelo.left(180)

        elif self.direction == 'down':
            if new_direction == 'up':
                self.donatelo.left(180)
            elif new_direction == 'right':
                self.donatelo.right(90)
            elif new_direction == 'left':
                self.donatelo.left(90)

        elif self.direction == 'left':
            if new_direction == 'up':
                self.donatelo.right(90)
            elif new_direction == 'right':
                self.donatelo.right(180)
            elif new_direction == 'down':
                self.donatelo.left(90)

    def go_direction(self, direction):
        self.set_direction(direction)
        self.donatelo.forward(30)
        if direction == 'up':
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == 'right':
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == 'down':
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == 'left':
            self.position = (self.position[0] - 1, self.position[1])

    def go_up(self):
        self.go_direction('up')

    def go_right(self):
        self.go_direction('right')

    def go_down(self):
        self.go_direction('down')

    def go_left(self):
        self.go_direction('left')
    about_directions = {0: go_up, 1: go_right, 2: go_down, 3: go_left}

    def come_back(self):
        pass

    def safe_choice(self):
        self.about_directions[self.positions_options[self.position].index(0)](self)

    def bifurcation(self):
        pass

    def trifurcation(self):
        pass
    about_choices = {0:come_back, 1:safe_choice, 2:bifurcation, 3:trifurcation}

    def go(self):
        # while there_is_exit_here == False
        self.positions_options.update({self.position: self.look_arround()})
        # Saida está ao meu lado?
        self.about_choices[self.how_many_choices()](self)
