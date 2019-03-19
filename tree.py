class Tree:

    exit_path = []

    def __init__(self, identifier, predecessor=None,
                tree_up=None, tree_right=None, tree_down=None, tree_left=None):

        self.id = identifier
        self.predecessor = predecessor

        self.tree_up = tree_up
        self.tree_right = tree_right
        self.tree_down = tree_down
        self.tree_left = tree_left

    def __str__(self):
        """
            This method specify how print one Tree.
        :return: None
        """
        return (
            'My cargo: ' + str(self.id)
            + '\nMy Up: ' + str(self.tree_up)
            + '\nMy Right: '+ str(self.tree_right)
            + '\nMy Down: '+ str(self.tree_down)
            + '\nMy Left: '+ str(self.tree_left)
        )

    def change_position_options(self, index, new_value, position_options,
                                position=None):
        """
            This method is used for the tree to know where it has passed.

        :param index: Type INT, used for pop and insert new_value.

        :param new_value: Type INT, used as path identifier already traversed.

        :param position_options: Type DICT = {(TUPLE): [LIST]},
                                    used to identify all possible options.

        :param position: Type TUPLE, used to identify what list change.
                        Can be None if you want change you current position.

        :return: This method changes position_options in place, so return None,
        but position_options is changed.
        """
        if position is None:
            position = self.id

        position_options[position].pop(index)
        position_options[position].insert(index, new_value)

    def update_tree(self, position_options):
        """
            This is a recursively method which result in a tree of whole maze.
        Its do this looking every option in my position, stored in the param of
        this method.
            To all option == 0 create a sub-tree and change option in
        position_options to don't repeat itself and be stay locked in an
        infinite loop.
            Or, if option == 3 create a sub-tree which identify the exit.

        :param position_options: Type DICT = {(TUPLE): [LIST]}
        :return: None, update your sub-trees until all options are done.
        """

        # Update tree_up
        if position_options[self.id][0] == 0:
            self.tree_up = Tree((self.id[0], self.id[1] - 1), self)
            self.change_position_options(0, 5, position_options)
            self.change_position_options(2, 5, position_options,
                                         (self.id[0], self.id[1] - 1))

        elif position_options[self.id][0] == 3:
            self.tree_up = Tree('exit', self)

        # Update tree_Right
        if position_options[self.id][1] == 0:
            self.tree_right = Tree((self.id[0] + 1, self.id[1]), self)
            self.change_position_options(1, 5, position_options)
            self.change_position_options(3, 5, position_options,
                                         (self.id[0] + 1, self.id[1]))

        elif position_options[self.id][1] == 3:
            self.tree_right = Tree('exit', self)

        # Update tree_Down
        if position_options[self.id][2] == 0:
            self.tree_down = Tree((self.id[0], self.id[1] + 1), self)
            self.change_position_options(2, 5, position_options)
            self.change_position_options(0, 5, position_options,
                                         (self.id[0], self.id[1] + 1))

        elif position_options[self.id][2] == 3:
            self.tree_down = Tree('exit', self)

        # Update tree_Left
        if position_options[self.id][3] == 0:
            self.tree_left = Tree((self.id[0] - 1, self.id[1]), self)
            self.change_position_options(3, 5, position_options)
            self.change_position_options(1, 5, position_options,
                                         (self.id[0] - 1, self.id[1]))

        elif position_options[self.id][3] == 3:
            self.tree_left = Tree('exit', self)

        '''********************************************************************
        ** Now, we call this method recursively until all the tree are done. **
        ********************************************************************'''

        for tree_direction in [self.tree_up, self.tree_right, self.tree_down,
                               self.tree_left]:

            if tree_direction is not None and tree_direction.id != 'exit':
                tree_direction.update_tree(position_options)

    def path_to_exit(self, branch):
        """
            This method update self.exit_path in place putting my predecessor
        in the path_to_exit, but remember, to know the path, we have to start
        about the end, which results in a path that needed be reverted.

        :param branch: Type TREE, used to know the predecessor.

        :return: This method again case predecessor different of None.
                Else, return None, but path_to_exit is now ready to use.
        """
        if branch is not None:
            # print('branch: ', branch, '\tType: ', type(branch))
            self.exit_path.append(branch.predecessor)
            return self.path_to_exit(branch.predecessor)

    def find_exit(self):
        """
            This function traverse a tree until find, the tree which identifies
        the exit, after that call the recursive method "self.path_to_exit" which
        change "self.exit_path" in place. And return it.

        :return: Note, the list of Tree objects returned by this function
        represents the output path to the beginning, so it needs to be inverted
        """

        for tree_direction in [self.tree_up, self.tree_right, self.tree_down,
                               self.tree_left]:
            if tree_direction is not None:
                if tree_direction.id == 'exit':
                    return self.path_to_exit(tree_direction)
                else:
                    tree_direction.find_exit()

    def invert_direction(self, directions):
        """
            This function receive a list os strings which represents directions
        and replace based on new_direction DICT to a inverted direction.

        :param directions: LIST OF STRINGS
        :return: One list of Strings which represents the path from the start
        to the exit.
        """
        result = []
        new_direction = {'up': 'down', 'right': 'left',
                         'down': 'up', 'left': 'right'}

        for direction in directions:
            result.append(new_direction[direction])

        return result

    def calculate_direction(self):
        """
            This method calculate the path from me until my predecessor.

        :return: A string that represents the direction from my position
        until my predecessor position, can be, 'up', 'right', 'down' or 'left'.
        """

        if self.id[0] - self.predecessor.id[0] == 0:  # same x axis, movement in y
            if self.id[1] - self.predecessor.id[1] > 0:  # moved up in y
                return 'up'

            else:  # moved down in y
                return 'down'

        else:  # same y axis, movement in x

            if self.id[0] - self.predecessor.id[0] > 0:
                return 'left'

            else:
                return 'right'

    def trace_route(self):
        """
            This function use the above functions "calculate_direction" and
        "invert_direction" to return:

        :return: One list of Strings which represents the path from the start
        to the exit.
        """

        route = []
        '''********************************************************************
        ** exit_path[:-2] because the last index of this list is None and    ** 
        ** calculate_direction use tree.predecessor, so -2 is the last index **
        ** with a valid tree.predecessor.                                    **
        ********************************************************************'''
        for tree in self.exit_path[:-2]:
            route.append(tree.calculate_direction())

        route = self.invert_direction(route)

        return route
