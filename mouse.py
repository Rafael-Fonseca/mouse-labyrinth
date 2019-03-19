class Mouse:

    def __init__(self, turtle, maze):
        self.donatelo = turtle
        self.maze = maze

        self.old_position = (0, 0)
        self.position = (0, 0)

        #All options of the lab
        self.axis_x = len(maze.vertical) -1
        self.axis_y = len(maze.horizontal) - 1
        self.positions_options = {}
        for column in range(self.axis_y):  # len(horizontal) = 13
            for line in range(self.axis_x):
                self.positions_options.update({(line, column):
                                                   self.look_arround((line, column))})

        self.choice_place = []
        self.direction = 'none'
        self.path = {}

    def prepare_turtle(self, width, color, shape, speed):
        self.donatelo.shape(shape)
        self.donatelo.color(color)
        self.donatelo.pensize(width)
        self.donatelo.speed(speed)

    def set_start(self, tuple_position):
        self.donatelo.penup()
        self.donatelo.setpos(tuple_position)
        self.donatelo.pendown()

    def set_direction(self, new_direction):
        """
        This method prepare the direction where the turtle should move.
        It considers self variable direction and new direction parameter.
        Direction starts with value none and is update by this method.

        :param new_direction:
        :return: None
        """

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
                self.donatelo.left(90)
            elif new_direction == 'left':
                self.donatelo.right(90)  # Se vai no sentido horario é right

        elif self.direction == 'left':
            if new_direction == 'up':
                self.donatelo.right(90)
            elif new_direction == 'right':
                self.donatelo.right(180)
            elif new_direction == 'down':
                self.donatelo.left(90)

        self.direction = new_direction

    def change_position_options(self, index, new_value):
        '''
        This method change the options, that the mouse has.

        :param index: Where you want to put a new_value
        :param new_value: What you want put in options
        :return: None
        '''
        self.positions_options[self.position].pop(index)
        self.positions_options[self.position].insert(index, new_value)

    def go_direction(self, direction):
        '''
        This method use method set_direction to prepare the direction where the
        turtle should move.
        Change old_position value to be equals position value.
        Move the turtle.
        Change self.positions_options placing a int(4) in the moved direction.
        Change position according move direction

        :param direction:
        :return: None
        '''
        self.set_direction(direction)
        self.old_position = self.position
        self.donatelo.forward(30)

        if direction == 'up':
            self.change_position_options(0, 4)
            self.position = (self.position[0], self.position[1] - 1)
            self.change_position_options(2, 4)

        elif direction == 'right':
            self.change_position_options(1, 4)
            self.position = (self.position[0] + 1, self.position[1])
            self.change_position_options(3, 4)

        elif direction == 'down':
            self.change_position_options(2, 4)
            self.position = (self.position[0], self.position[1] + 1)
            self.change_position_options(0, 4)

        elif direction == 'left':
            self.change_position_options(3, 4)
            self.position = (self.position[0] - 1, self.position[1])
            self.change_position_options(1, 4)

    '''************************************************************************
    **                       ABOUT_DIRECTIONS DEFINITION                     **
    ***************************************************************************
    ** The functions below:                                                  **
    ** go_up()                                                               **
    ** go_right()                                                            **
    ** go_down()                                                             **
    ** go_left()                                                             **
    ** are part of the dictionary of functions: ABOUT_DIRECTION              **
    ************************************************************************'''

    def go_up(self):
        self.go_direction('up')

    def go_right(self):
        self.go_direction('right')

    def go_down(self):
        self.go_direction('down')

    def go_left(self):
        self.go_direction('left')
    about_directions = {'up': go_up, 'right': go_right, 'down': go_down,
                        'left': go_left}

    '''************************************************************************
    **                    END ABOUT_DIRECTION DEFINITION                     **
    ************************************************************************'''

    def walk_to_exit(self, directions):

        for direction in directions:
            self.about_directions[direction](self)




    '''************************************************************************
    **                                                                       **
    **                      END OF THE USEFULL CODE                          **
    **                                                                       **
    ***************************************************************************
    **     The code below is useless, it was written on my first attempt to  **
    ** solve the problem.                                                    **
    ************************************************************************'''


    def look_arround(self, position=None):
        '''
        This fuction receive one position and return all the options that
        position, don't matter if is blocked or free.
        If a position is not received, look_arround treats like you want know
        the option of actual position.

        :param position:
        :return:
        '''
        if position is None:
            position = self.position

        return [self.maze.horizontal[position[1]][position[0]],
                self.maze.vertical[position[0]+1][position[1]],
                self.maze.horizontal[position[1]+1][position[0]],
                self.maze.vertical[position[0]][position[1]]]

    def how_many_choices(self):
        '''
        This function assists the mouse know how many options it has.

        :return: int(quantity of free spaces that are represented by 0)
        '''
        choices = 0
        for option in self.positions_options.get(self.position):
            if option == 0:
                choices += 1

        return choices

    def register_path(self):
        self.path.update({self.old_position: self.position})

    '''************************************************************************
    **                                                                       **
    **                       ABOUT_CHOICES DEFINITION                        **
    **                                                                       **
    ***************************************************************************
    ** The functions below:                                                  **
    ** come_back()                                                           **
    ** safe_choice()                                                         **
    ** bifurcation()                                                         **
    ** trifurcation()                                                        **
    ** are part of the dictionary of functions: ABOUT_CHOICES                **
    ************************************************************************'''
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

    '''************************************************************************
    **                   END ABOUT_CHOICES DEFINITION                        **
    ************************************************************************'''

    def exit_next_me(self):
        return 3 in self.positions_options[self.position]

    def go(self):

        there_is_exit_here = False
        for _ in range(10):
        #while not there_is_exit_here:
            #self.positions_options.update({self.position: self.look_arround()})
            if self.exit_next_me():
                break

            # print('First Position: ', self.positions_options[self.position])
            self.about_choices[self.how_many_choices()](self)
            print('Position: ', self.position, 'Options: ', self.positions_options[self.position], 'Direction: ', self.direction)
