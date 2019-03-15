class Mouse:

    def __init__(self, turtle, maze):
        self.donatelo = turtle
        self.maze = maze

        self.old_position = (0, 0)
        self.position = (0, 0)

        self.axis_x = len(maze.vertical)
        self.axis_y = len(maze.horizontal)
        self.positions_options = {}
        for column in range(self.axis_y):
            for line in range(self.axis_x):
                self.positions_options.update({(line, column):
                                                   self.look_arround((line, column))})

        print(self.positions_options)
        self.choice_place = []
        self.direction = 'none'
        self.path = {}

    def prepare_turtle(self, width, color, shape):
        self.donatelo.shape(shape)
        self.donatelo.color(color)
        self.donatelo.pensize(width)

    def set_start(self, tuple_position):
        self.donatelo.penup()
        self.donatelo.setpos(tuple_position)
        self.donatelo.pendown()

    def look_arround(self, position=None):
        if position is None:
            position = self.position

        print('position 1: ', position[1], '\nposition 0: ', position[0])
        return [self.maze.horizontal[position[1]][position[0]],
                self.maze.vertical[position[0]+1][position[1]], # ta tentando acessar positon 6 + 1
                self.maze.horizontal[position[1]+1][position[0]],
                self.maze.vertical[position[0]][position[1]]]

    def how_many_choices(self):
        choices = 0
        for option in self.positions_options.get(self.position):
            if option == 0:
                choices += 1

        return choices

    def register_path(self):
        self.path.update({self.old_position: self.position})

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
            # altera options
            self.positions_options[self.position] = [
                4,
                self.positions_options[self.position][1],
                self.positions_options[self.position][2],
                self.positions_options[self.position][3],
            ]
            # altera posição
            self.old_position = self.position
            self.position = (self.position[0], self.position[1] - 1)

        elif direction == 'right':
            # altera options
            self.positions_options[self.position] = [
                self.positions_options[self.position][0],
                4,
                self.positions_options[self.position][2],
                self.positions_options[self.position][3],
            ]
            # altera posição
            self.old_position = self.position
            self.position = (self.position[0] + 1, self.position[1])

        elif direction == 'down':
            # altera options
            self.positions_options[self.position] = [
                self.positions_options[self.position][0],
                self.positions_options[self.position][1],
                4,
                self.positions_options[self.position][3],
            ]
            # altera posição
            self.old_position = self.position
            self.position = (self.position[0], self.position[1] + 1)

        elif direction == 'left':
            # altera options
            self.positions_options[self.position] = [
                self.positions_options[self.position][0],
                self.positions_options[self.position][1],
                self.positions_options[self.position][2],
                4
            ]
            # altera posição
            self.old_position = self.position
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
        # Volta e tira do path
        pass

    def safe_choice(self):
        self.about_directions[self.positions_options[self.position].index(0)](self)
        self.register_path()

    def bifurcation(self):
        pass

    def trifurcation(self):
        pass
    about_choices = {0:come_back, 1:safe_choice, 2:bifurcation, 3:trifurcation}

    def exit_next_me(self):
        return 3 in self.positions_options[self.position]

    def go(self):
        there_is_exit_here = False
        while not there_is_exit_here:
            self.positions_options.update({self.position: self.look_arround()})
            if self.exit_next_me():
                break

            self.about_choices[self.how_many_choices()](self)

        print('Tudo ok')
