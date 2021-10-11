#!/usr/bin/env python3
import time
import random

# Imcomplete board
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

# Invalid board
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

# Valid board
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

class Board():
    def __init__(self, board):
        self.x_lines = create_x_lines(board)
        self.tiles = self.scan_board(board)
        self.detect_valid()

    def scan_board(self, board):
        tiles = dict()
        x_lines = self.x_lines
        y_lines = create_y_lines(board)
        block_lines = create_block_lines(board)
        for x in range(9):
            for y in range(9):
                z = 0
                t = Tile(x, y, x_lines[x][y])
                tiles[str(x) + 'x' + str(y)] = t
                # Store the associated lines in tile
                tiles[str(x) + 'x' + str(y)].x_line = x_lines[x]
                tiles[str(x) + 'x' + str(y)].y_line = y_lines[y]
                # Store the associated block of digits in tile
                if y < 3:
                    z += 0
                elif y < 6:
                    z+=1
                elif y < 9:
                    z+=2
                if x < 3:
                    z+=0
                elif x < 6:
                    z+=3
                elif x < 9:
                    z+=6
                tiles[str(x) + 'x' + str(y)].block_line = block_lines[z]
                # Is the value of the tile allowed to change
                if not tiles[str(x) + 'x' + str(y)].value:
                    tiles[str(x) + 'x' + str(y)].static = False
        return tiles

    """Check neighbor tiles to determine invalid and valid values on each tile"""
    def detect_valid(self):
        for key in self.tiles.keys():
            self.tiles[key].update_valid_tiles()



class Tile():
    def __init__(self, x, y, value):
        self.static = True
        self.x = x
        self.y = y
        self.value = value
        self.x_line = []
        self.y_line = []
        self.block_line = []
        self.valid_tiles = {}
        self.invalid_tiles = {}

    def update_valid_tiles(self):
        if self.static:
            return [self.value]
        all = {1,2,3,4,5,6,7,8,9}
        self.invalid_tiles = set(self.x_line + self.y_line + self.block_line)
        self.valid_tiles = all.difference(self.invalid_tiles)


    def update_value(self):
        if self.static:
            return

"""
Create a class for board
create a class for each tile
- board object will contain all the tiles and their positions
- board object will contain a list of all positions that are allow to be changed

- use lowest possible numbers first and increment? (might be silly)

- intersect the line with 1-9 to see possible combinations
- place a guess in it that includes valid spots and move on
- when board is filled, detect conflicts
- delete conflicts and recurse ^
"""

def display_xlines(x_lines):
    print('-'*13)
    count = 0
    for l in x_lines:
        if count == 3:
            print('-'*13)
            count = 0
        count += 1
        line = []
        for i in range(9):
            if l[i] == False:
                line.append(0)
            else:
                line.append(l[i])
        block1 = ''.join(str(e) for e in line[0:3])
        block2 = ''.join(str(e) for e in line[3:6])
        block3 = ''.join(str(e) for e in line[6:9])
        print('|'+block1+'|'+block2+'|'+block3+'|')
    print('-'*13)


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

"""Return a list of sets for each 3x3 block"""
def create_block_lines(board):
    blocks = []
    for x in range(0,9,3):
        blocks.append(board[0+x][0] + board[1+x][0] + board[2+x][0])
        blocks.append(board[0+x][1] + board[1+x][1] + board[2+x][1])
        blocks.append(board[0+x][2] + board[1+x][2] + board[2+x][2])
    return blocks

"""Return a list of lines along the x axis"""
def create_x_lines(board):
    linesx = []
    for x in range(9):
        linesx.append(board[x][0] + board[x][1] + board[x][2])
    return linesx

"""Return a list of lists along the y axis"""
def create_y_lines(board):
    linesy = []
    for z in range(3):
        liney1 = []
        liney2 = []
        liney3 = []
        for y in range(9):
            liney1.append(board[y][z][0])
            liney2.append(board[y][z][1])
            liney3.append(board[y][z][2])
        linesy.append(liney1)
        linesy.append(liney2)
        linesy.append(liney3)
    return linesy

"""Turn a list of lists into a list of sets for validation"""
def setify(board):
    set_board = []
    for line in board:
        set_board.append(set(line))
    return set_board


"""Use sets to determine if a full board is legal"""
def board_checker(board):
    valid = True
    test = setify(create_x_lines(board)) + setify(create_y_lines(board)) + setify(create_block_lines(board))
    for line in test:
        if len(line) != 9 or False in line:
            valid = False
    return valid

def solve_it(board):
    #x_lines = create_x_lines(board)
    #y_lines = create_y_lines(board)
    #block_lines = create_block_lines(board)
    pass
















def main():
    display(incomplete_board1)
    b = Board(incomplete_board1)
    display_xlines(b.x_lines)

    #display(b.x_lines)
    # for key in b.tiles.keys():
    #     print(b.tiles[key].value, b.tiles[key].static, b.tiles[key].valid_tiles)
    # for key in b.tiles.keys():
    #     print(key, b.tiles[key].x, b.tiles[key].y, b.tiles[key].value)
    #     print(b.tiles[key].x_line)
    #     print(b.tiles[key].y_line)
    #     print(b.tiles[key].block_line)


    #print(board_checker(board_test1))
    #print(board_checker(board_test2))
    #print(create_x_sets(board_test1))
    #print(setify(create_x_sets(board_test1)))
    #print(board_test1)
    #print(create_x_sets(board_test1))


if __name__ == '__main__':
    main()
    #stdscr = curses.initscr()
    #main(stdscr)
