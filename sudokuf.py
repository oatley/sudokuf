#!/usr/bin/env python3
import time
import random

incomplete_board1 = [
    [[8,4,False],[False,9,False],[3,2,1]],
    [[3,False,9],[8,2,1],[6,7,4]],
    [[False,2,False],[False,4,3],[9,8,5]],

    [[False,3,2],[4,False,False],[1,6,8]],
    [[9,False,4],[3,1,6],[7,5,2]],
    [[6,False,False],[2,8,False],[4,9,False]],

    [[5,6,8],[9,3,4],[2,1,7]],
    [[2,7,3],[False,False,False],[5,4,9]],
    [[False,9,1],[5,7,2],[8,3,6]],
]

board_test1 = [
    [[1,1,1],[4,5,6],[7,8,9]],
    [[2,2,2],[4,5,6],[7,8,9]],
    [[3,3,3],[4,5,6],[7,8,9]],

    [[4,2,1],[4,5,6],[7,8,9]],
    [[5,2,3],[4,5,6],[7,8,9]],
    [[6,2,1],[4,5,6],[7,8,9]],

    [[9,2,3],[4,5,6],[7,8,9]],
    [[8,2,1],[4,5,6],[7,8,9]],
    [[7,2,3],[4,5,6],[7,8,9]],
]

board_test2 = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[7,8,9],[1,2,3],[4,5,6]],
    [[4,5,6],[7,8,9],[1,2,3]],

    [[3,1,2],[8,4,5],[9,6,7]],
    [[6,9,7],[3,1,2],[8,4,5]],
    [[8,4,5],[6,9,7],[3,1,2]],

    [[2,3,1],[5,7,4],[6,9,8]],
    [[9,6,8],[2,3,1],[5,7,4]],
    [[5,7,4],[9,6,8],[2,3,1]],
]


"""
Ideas:
- use sets and intersections to create a "Legal" set of digits that can be placed in each tile
- using the "legal" digits in each tile, add the test number to a temp exclusion and work through the other numbers
- if you've determined that a tile cannot "be" add that tile to a permanent exclusion
- create a method for printing current numbers while working through it and put it on a timer
"""

"""Print the board"""
def display(board):
    x = 1
    y = 1
    split_count_y = 3
    split_count_x = 0
    print('-'*13)
    for line in board:
        x=1
        for group in line:
            if split_count_x == 3:
                print('-'*13)
                split_count_x = 0
            for char in group:
                if split_count_y == 3:
                    x+=1
                    print('|', end="")
                    split_count_y = 0
                print('{:d}'.format(char), end="")
                split_count_y+=1
                x+=1
        split_count_x+=1
        print("|")
        y+=1
    print('-'*13)

# Return a list of sets for each 3x3 block
def create_block_sets(board):
    blocks = []
    for x in range(0,9,3):
        blocks.append(set(board[0+x][0] + board[1+x][0] + board[2+x][0]))
        blocks.append(set(board[0+x][1] + board[1+x][1] + board[2+x][1]))
        blocks.append(set(board[0+x][2] + board[1+x][2] + board[2+x][2]))
    return blocks

# Return a list of lines along the x axis
def create_x_sets(board):
    linesx = []
    for x in range(9):
        linesx.append(set(board[x][0] + board[x][1] + board[x][2]))
    return linesx

# Return a list of sets along the y axis
def create_y_sets(board):
    linesy = []
    for z in range(3):
        liney1 = []
        liney2 = []
        liney3 = []
        for y in range(9):
            liney1.append(board[y][z][0])
            liney2.append(board[y][z][1])
            liney3.append(board[y][z][2])
        linesy.append(set(liney1))
        linesy.append(set(liney2))
        linesy.append(set(liney3))
    return linesy


"""Use sets to determine if a full board is legal"""
def board_checker(board):
    valid = True
    test = create_x_sets(board) + create_y_sets(board) + create_block_sets(board)
    for line in test:
        if len(line) != 9:
            valid = False
    return valid


















def main():
    #display(board_test)
    print(board_checker(board_test1))
    print(board_checker(board_test2))


if __name__ == '__main__':
    main()
    #stdscr = curses.initscr()
    #main(stdscr)
