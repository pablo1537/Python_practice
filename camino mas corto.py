import curses
from curses import wrapper
import queue
import time

START_CHAR="O"
STOP_CHAR="X"
OBSTACLE_CHAR="#"


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "X", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

def print_maze(maze, stdscr , path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i ,row in enumerate(maze):
        for j, value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,STOP_CHAR,RED)
            else:
                stdscr.addstr(i,j*2,value,BLUE)

def find_start(maze):
    for i ,row in enumerate(maze):
        for j, value in enumerate(row):
            if value == START_CHAR:
                return i,j
    return None


def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors


#optimizar esto
def find_path(maze,stdscr):
    start_pos = find_start(maze)
    
    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.05)
        stdscr.refresh()

        if maze[row][col] == STOP_CHAR:
            return path
        
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == OBSTACLE_CHAR:
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
        
    return None    

def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_GREEN, curses.COLOR_BLACK)
    color = curses.color_pair(1)
    stdscr.clear()
    #stdscr.addstr(5,10,"Hola mundo!",color)#row,column,text
    #print_maze(maze, stdscr)
    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)