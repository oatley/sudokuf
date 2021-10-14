#!/usr/bin/env python3

"""
Sudoku puzzle solver
author: Andrew ow
co-author: beer and coffee
"""

# Invalid board
board_keys = [
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],

    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],

    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
]

incomplete_board1 = [
    [[8,4,0],[0,9,0],[3,2,1]],
    [[3,0,9],[8,2,1],[6,7,4]],
    [[0,2,0],[0,4,3],[9,8,5]],

    [[0,3,2],[4,0,0],[1,6,8]],
    [[9,0,4],[3,1,6],[7,5,2]],
    [[6,0,0],[2,8,0],[4,9,0]],

    [[5,6,8],[9,3,4],[2,1,7]],
    [[2,7,3],[0,0,0],[5,4,9]],
    [[0,9,1],[5,7,2],[8,3,6]],
]



# MAX TEST
incomplete_board4 = [
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,3,0],[1,0,6],[2,0,7]],
    [[6,0,0],[0,3,0],[5,1,0]],

    [[3,2,0],[0,0,9],[0,0,0]],
    [[0,0,8],[0,0,5],[7,0,0]],
    [[0,0,0],[8,0,0],[0,5,3]],

    [[0,4,7],[0,9,0],[0,0,8]],
    [[8,0,1],[7,0,2],[0,9,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
]

incomplete_board5 = [
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,3,0],[1,0,0],[2,0,7]],
    [[6,0,0],[0,3,0],[5,1,0]],

    [[3,2,0],[0,0,9],[0,0,0]],
    [[0,0,8],[0,0,5],[7,0,0]],
    [[0,0,0],[0,0,0],[0,5,3]],

    [[0,4,7],[0,9,0],[0,0,8]],
    [[8,0,1],[7,0,2],[0,9,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
]

# Invalid board VERY HARD
incomplete_board6 = [
    [[0,0,0],[0,0,0],[9,0,1]],
    [[0,1,0],[0,0,0],[0,0,0]],
    [[0,0,4],[0,6,8],[0,0,3]],

    [[0,0,0],[0,0,9],[0,8,0]],
    [[0,0,7],[8,0,0],[0,9,0]],
    [[0,0,9],[0,0,5],[0,0,0]],

    [[0,0,3],[0,0,1],[0,0,9]],
    [[0,7,0],[0,0,0],[0,0,0]],
    [[2,0,0],[0,0,7],[0,0,8]],
]

# Invalid board
incomplete_board2 = [
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],

    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],

    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
]

incomplete_board3 = [
    [[0,0,3],[0,0,0],[9,0,0]],
    [[0,0,0],[0,0,0],[1,0,0]],
    [[0,0,5],[9,0,0],[0,0,0]],

    [[6,0,0],[0,0,0],[5,2,0]],
    [[8,0,0],[0,0,0],[0,0,0]],
    [[3,0,0],[0,9,0],[0,0,0]],

    [[0,0,0],[0,8,0],[2,9,7]],
    [[0,9,0],[0,7,0],[8,0,1]],
    [[0,0,0],[0,0,0],[0,3,5]],
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
        self.blocks = create_block_lines(board)
        self.solutions = 0
        self.setup_tile_keys()
        self.update_static_tiles()
        self.detect_valid()


    """Tiles are given: x_lines, y_lines, and blocks lines -> lists of neighbor keys on xyz axis"""
    def setup_tile_keys(self):
        self.block_tiles = self.setup_block_lines()
        for tile in self.tiles.keys():
            self.setup_x_tiles(tile)
            self.setup_y_tiles(tile)
            for block in self.block_tiles:
                if tile in block:
                    self.tiles[tile].block_tile_keys = block

    """Create a list of tile keys organized by blocks: index0=0x0->2x2"""
    def setup_block_lines(self):
        block_tiles =[] # list of lists
        block = [0, 1, 2]
        for modrow in range(0,9,3):
            for modcol in range(0,9,3):
                col = 0 + modcol
                row = 0 + modrow
                block_list = []
                for modblock in block:
                    block_list.append(str(row+0) + 'x' + str(col+modblock))
                    block_list.append(str(row+1) + 'x' + str(col+modblock))
                    block_list.append(str(row+2) + 'x' + str(col+modblock))
                block_tiles.append(block_list)
        return block_tiles

    """for each tile store a list of keys for each tile that shares x with this tile"""
    def setup_x_tiles(self, tile):
        x_tiles = []
        for t in self.tiles.keys():
            if self.tiles[tile].x == self.tiles[t].x:
                x_tiles.append(t)
        self.tiles[tile].x_tile_keys = x_tiles

    """for each tile store a list of keys for each tile that shares x with this tile"""
    def setup_y_tiles(self, tile):
        y_tiles = []
        for t in self.tiles.keys():
            if self.tiles[tile].y == self.tiles[t].y:
                y_tiles.append(t)
        self.tiles[tile].y_tile_keys = y_tiles

    def check_static(self):
        tiles = dict()
        for key in self.tiles:
            if not self.tiles[key].static:
                tiles[key] = self.tiles[key]
        return tiles

    def update_static_tiles(self):
        self.nonstatic_tiles = self.check_static()

    """Uhhh comment the datastructure maybe?"""
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

    def update_x_lines(self):
        for x in range(9):
            for y in range(9):
                key = str(x) + 'x' + str(y)
                if self.tiles[key].value != self.x_lines[x][y]:
                    self.x_lines[x][y] = self.tiles[key].value

    """Check neighbor tiles to determine invalid and valid values on each tile"""
    def detect_valid(self):
        for key in self.tiles.keys():
            self.tiles[key].update_valid_tiles()

"""object to store individual tile information"""
class Tile():
    def __init__(self, x, y, value):
        self.static = True
        self.x = x
        self.y = y
        self.key = str(x) +'x' + str(y)
        self.value = value
        self.x_line = []
        self.y_line = []
        self.block_line = []
        self.valid_tiles = {}
        self.invalid_tiles = {}
        self.try_value = []
        self.checking = False

    """find all valid values for each tile"""
    def update_valid_tiles(self):
        if self.static:
            return [self.value]
        all = {1,2,3,4,5,6,7,8,9}
        self.invalid_tiles = set(self.x_line + self.y_line + self.block_line)
        self.valid_tiles = all.difference(self.invalid_tiles)

    """only allow changes to non-static values"""
    def update_value(self, value):
        if self.static:
            return
        self.value = value

def xlines_to_board(x_lines):
    board = []
    for line in x_lines:
        block1 = line[0:3]
        block2 = line[3:6]
        block3 = line[6:9]
        new_line = [block1, block2, block3]
        board.append(new_line)
    return board

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
                print('{}'.format(char), end="")
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

"""Prepare the sudoku board and start the recursive function"""
def start_combo(board):
    display(board)
    b = Board(board)
    b.board = xlines_to_board(b.x_lines)
    b.update_x_lines()
    possy = dict()
    for key in b.nonstatic_tiles.keys():
        possy[key] = b.nonstatic_tiles[key].valid_tiles.copy()
    b.combos = []
    b.combo_length = len(possy)
    print('sudokuf -> combo length set', b.combo_length)
    print('sudokuf -> starting recurse')
    combo = start_combo_recurse_2(possy, b)

"""Recursive sudoku solution"""
def start_combo_recurse_2(possy, b, combo={}):
    # Check if the current combination solves the puzzle and exit
    if len(possy) < 1 and 'x' not in combo.values() and len(combo) == b.combo_length:
        if combo not in b.combos:
            b.solutions += 1
            b.combos.append(combo)
            print ('sudokuf -> found solution')#, combo, b.solutions)
            for key in combo.keys():
                b.tiles[key].update_value(combo[key])
            b.update_x_lines()
            board = xlines_to_board(b.x_lines)
            if board_checker(board):
                print ('sudokuf -> solved puzzle and exiting...')
                print(combo)
                display(board)
                exit()
            return
    # Check if the current combination is void
    if len(possy) < 1 and len(combo) < b.combo_length:
        print ('sudokuf -> broken combo')#, combo)
        return
    p = possy.copy() # possy is a set of non-static tiles and their possible valid values
    combo_copy = combo.copy()
    current = p.popitem() # current is a tuple key[0] value[1] pair
    for v in current[1]: # attempt to use "valid" values and for a combination
        combo_copy[current[0]] = v
        for tile in combo_copy.keys(): # This loop finds invalid combinations early to save time
            # detect invalid combinations based on block positions
            if tile != current[0] and tile in b.tiles[current[0]].block_tile_keys: # detected shared col
                if combo_copy[current[0]] == combo_copy[tile]: # detected shared value in col
                    #print('sudokuf -> found shared value ', combo_copy, b.tiles[current[0]].y_tile_keys)
                    combo_copy[current[0]] = 'x'
                    continue
            # detect invalid combinations based on row tile positions
            if tile != current[0] and tile in b.tiles[current[0]].y_tile_keys: # detected shared col
                if combo_copy[current[0]] == combo_copy[tile]: # detected shared value in col
                    #print('sudokuf -> found shared value ', combo_copy, b.tiles[current[0]].y_tile_keys)
                    combo_copy[current[0]] = 'x'
                    continue
            # detect invalid combinations based on column positions
            if tile != current[0] and tile in b.tiles[current[0]].x_tile_keys: # detected shared col
                if combo_copy[current[0]] == combo_copy[tile]: # detected shared value in col
                    #print('sudokuf -> found shared value ', combo_copy, b.tiles[current[0]].x_tile_keys)
                    combo_copy[current[0]] = 'x'
                    continue
        if 'x' not in combo_copy.values():
            start_combo_recurse_2(p, b, combo_copy)
            if combo_copy in b.combos:
                return
    return

def main():
    #start_combo(incomplete_board1) # easy
    start_combo(incomplete_board4) # maxtest # try and beat .12 I GOT .25!!!!
    #start_combo(incomplete_board5) # maxtest + 2 deletions
    #start_combo(incomplete_board6) # VERY HARD

if __name__ == '__main__':
    main()
