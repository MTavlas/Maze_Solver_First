from skimage import io
import numpy as np
import sys


def condense(maze):
    condensed = []
    for j in range(0, 114, 8):
        my_list = []
        for i in range(0, 114, 8):
            my_list.append(maze[j, i])
        condensed.append(my_list)
    return condensed

print(sys.path)

np.set_printoptions(threshold=sys.maxsize, linewidth=500)

maze_dir = r"C:\Users\Memo\Desktop\Python\Projects\Maze_IMG_Process\maze7x7.png"
maze_uncrop_1 = io.imread(maze_dir, as_gray=True)
maze_uncrop_2 = np.delete(maze_uncrop_1, 0, 1)
maze = np.delete(maze_uncrop_2, 114, 0)

small_ver = condense(maze)

print(small_ver)
