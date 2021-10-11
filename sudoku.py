#!/usr/bin/env python3
import time
import curses
import random
from curses import wrapper

MAP_HEIGHT = 11
MAP_WIDTH = 11

board = [
    [[1,1,1],[4,5,6],[7,8,9]],

    [[2,2,2],[4,5,6],[7,8,9]],

    [[3,3,3],[4,5,6],[7,8,9]],

    [[4,2,1],[4,5,6],[7,8,9]],

    [[5,2,3],[4,5,6],[7,8,9]],

    [[6,2,1],[4,5,6],[7,8,9]],

    [[7,2,3],[4,5,6],[7,8,9]],

    [[8,2,1],[4,5,6],[7,8,9]],

    [[9,2,3],[4,5,6],[7,8,9]],
]


def main(stdscr):
    stdscr.clear()
    # This raises ZeroDivisionError when i == 10.
    x = 1
    y = 1
    for line in board:
        x=1
        split_count_y = 0
        split_count_x = 0
        for group in line:
            for char in group:
                if split_count_y == 3:
                    x+=1
                    stdscr.addstr(y, x, '|')
                    split_count_y = 0
                if split_count_x == 3:
                    y+=1
                    #stdscr.addstr(y, x, '-')
                    split_count_x = 0
                split_count_x+=1
                stdscr.addstr(y, x+1, str(char))
                split_count_y+=1
                x+=1
        y+=1
    #stdscr.addstr(1, 1, 'MEOOOW')
    stdscr.refresh()
    stdscr.getkey()

    #curses.start_color()
    #curses.use_default_colors()
    #curses.noecho()
    #stdscr = curses.newwin(MAP_HEIGHT, MAP_WIDTH, 0, 0)
    #sudowin.nodelay(1)
    #sudowin.clear()
    #sudowin.refresh()
    #sudowin.border(0)
    #sudowin.addstr(1, 1, 'MEOOOW')
    #sudowin.refresh()
    #stdscr.refresh()
    # Doupdate redraws the screen
    #curses.doupdate()

if __name__ == '__main__':
    wrapper(main)
    #stdscr = curses.initscr()
    #main(stdscr)
