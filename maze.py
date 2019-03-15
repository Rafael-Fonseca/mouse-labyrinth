class Maze:

    def __init__(self, turtle, list_vertical, list_horizontal):
        self.turtle = turtle
        self.vertical = list_vertical
        self.horizontal = list_horizontal

    def prepare_turtle(self, width, color, shape):
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.pensize(width)
        self.turtle.speed(0)

    def set_start(self, tuple_position):
        self.turtle.penup()
        self.turtle.setpos(tuple_position)
        self.turtle.pendown()

    def draw(self):
        for line in self.horizontal:
            self.set_start( (self.turtle.pos()[0] - 180,
                             self.turtle.pos()[1] - 30) )

            for index in line:

                if index == 0:
                    self.pass_line()

                elif index == 2 or index == 3:  # entry and exit indexes
                    self.pass_line()

                else:
                    self.draw_line()
                # else:
                #    print("Index desconhecido encontrado horizontal: ", index)

        self.set_start( (self.turtle.pos()[0] - 210,
                         self.turtle.pos()[1]) )
        self.turtle.right(90)

        for column in self.vertical:
            self.set_start( (self.turtle.pos()[0] + 30,
                             self.turtle.pos()[1] + 360) )

            for index in column:

                if index == 0:
                    self.pass_line()

                elif index == 2 or index == 3:  # entry and exit indexes
                    self.pass_line()

                else:
                    self.draw_line()
                # else:
                #    print("Index desconhecido encontrado vertical: ", index)

    def draw_line(self):
        self.turtle.pendown()
        self.turtle.forward(30)

    def pass_line(self):
        self.turtle.penup()
        self.turtle.forward(30)

    def wait_donatelo(self):
        self.set_start( (self.turtle.pos()[0] + 30, self.turtle.pos()[1] + 75))
        self.turtle.right(90)
