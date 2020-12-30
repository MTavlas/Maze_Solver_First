import numpy as np

maze_1 = np.array([[1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                   [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1]])


# end = 3
# start = 2
class Memo:

    def __init__(self, maze: np.array):
        self.maze = maze

        y_start, x_start = np.where(self.maze == 2)
        self.start_y = int(y_start)
        self.start_x = int(x_start)

        y_end, x_end = np.where(self.maze == 3)
        self.end_y = int(y_end)
        self.end_x = int(x_end)

    def check_neigbours(self, y, x):
        # current_pos = self.maze[x, y]

        try:
            upper_neighbour = self.maze[y - 1, x]
        except IndexError:
            upper_neighbour = None

        try:
            lower_neighbour = self.maze[y + 1, x]
        except IndexError:
            lower_neighbour = None

        try:
            right_neighbour = self.maze[y, x + 1]
        except IndexError:
            right_neighbour = None

        try:
            left_neighbour = self.maze[y, x - 1]
        except IndexError:
            left_neighbour = None

        if y == 0:
            upper_neighbour = None

        if x == 0:
            left_neighbour = None

        return [upper_neighbour, lower_neighbour, right_neighbour, left_neighbour]

    def move_forward(self):
        current_pos = (self.start_y, self.start_x)
        fork_pos = []
        for i in range(maze_1.size):
            current_neigh = self.check_neigbours(current_pos[0], current_pos[1])
            maze_1[current_pos[0], current_pos[1]] = 9
            if 0 in current_neigh:
                if current_neigh.count(0) > 1:
                    fork_pos.append(current_pos)
                move_dir = current_neigh.index(0)
                if move_dir == 0:
                    current_pos = (current_pos[0] - 1, current_pos[1])
                elif move_dir == 1:
                    current_pos = (current_pos[0] + 1, current_pos[1])
                elif move_dir == 2:
                    current_pos = (current_pos[0], current_pos[1] + 1)
                elif move_dir == 3:
                    current_pos = (current_pos[0], current_pos[1] - 1)
            elif 3 in current_neigh:
                print("I found the solution!")
                print(maze_1)
                print(f"It took me {i+1} steps in total!")
                break
            else:
                current_pos = fork_pos[0]
                fork_pos.pop(0)


print(maze_1)
Memo(maze_1).move_forward()
