import unittest

# The function I will test
empty_position_set = {(1,1),(1,2),(2,1),(2,2)}
n = 8
# Function: is_in_empty_set
# Does: check if the position x,y in the empty set which means there is no tile
# Signature: is_in_empty_set :: (Integer,Integer) => Boolean
def is_in_empty_set(x,y):
    return ((x,y) in empty_position_set)

# Function: check_inside_board
# Does: check if the position x,y is inside the n*n board
# Signature: check_inside_board :: (Integer,Integer) => Boolean
def check_inside_board(x,y):
    global n
    if x>=1 and x<=n and y>=1 and y<=n:
        return True
    else:
        return False

# Function: init_empty_position_set
# Does: make a initial set of all empty positions on the n*n board
# Signature: init_empty_position_set :: Integer => Set
# Example: init_empty_position_set(2) => {(1,1),(1,2),(2,1),(2,2)}
def init_empty_position_set(n):
    global empty_position_set
    for i in range(int(n*n)):
        for y in range(1,n+1):
            for x in range(1,n+1):
                empty_position_set.add((x,y))
    return empty_position_set

# Function: game_over
# Does: decide the winner 
def game_over(white_set,black_set):
    white_number = len(white_set)
    black_number = len(black_set)
    winner_score = 0
    winner_color = str()
    if white_number > black_number: 
        winner_color = "W"
        winner_score = white_number   
        return "White is the winner."
        
    elif black_number > white_number:
        winner_color = "B"
        winner_score = black_number
        return "Black is the winner."
       

# unit test

class TestMethods(unittest.TestCase):

    def test_is_in_empty_set(self):
        self.assertTrue(is_in_empty_set(2,2))
        self.assertFalse(is_in_empty_set(4,5))

    def test_check_inside_board(self):
        self.assertTrue(check_inside_board(5,4))
        self.assertFalse(check_inside_board(8,9))
        self.assertFalse(check_inside_board(0,1))
        self.assertFalse(check_inside_board(12,-13))
    
    def test_init_empty_position_set(self):
        self.assertEqual(init_empty_position_set(2),{(1,1),(1,2),(2,1),(2,2)})

    def test_game_over(self):
        white_set1 = {(1,2),(2,3),(3,4)}
        black_set1 = {(4,2),(7,3),(5,4),(3,6)}
        
        white_set2 = {(1,2),(2,3),(3,4),(4,5),(7,7)}
        black_set2 = {(4,2),(7,3),(5,4),(3,6)}
       
        self.assertEqual(game_over(white_set1,black_set1),"Black is the winner.")
        self.assertEqual(game_over(white_set2,black_set2),"White is the winner.")


suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
unittest.TextTestRunner(verbosity=2).run(suite)

# Test idea for functions which I don't know how to test:

# Function: draw_board
# n=8 => It show draw a 8*8 board of squares

# Function: draw_lines
# Does: called to draw the lines in the board

# Function: init_four_tile
# Signature: init_four_tile :: (Integer,Integer) => Void
# Does: initialize to draw the first four tiles to start the game
# test: init_four_tile(4) => 
# draw black tile at column 2 row 2, and column 3 row 3
# draw white tile at column 3 row 2, and column 2 row 3

# Function: user_input_n
# Does: let user input the n for drawing n*n board
# Test: user_input_n => n will be assigned by user input

# Function: user_choose_color
# Does: let user input the color he wanna use for game
# Test: user_choose_color => user will input the color

# Function: draw_tile
# Signature: draw_tile :: (Integer,Integer) => Void
# Does: draw a tile at row x column y
# Test: draw_tile(3,4) => 
# current_color is black, then draw a black tile at row 3 column 4


# Function: draw_operation
# Parameters: i, j which are two numbers get from the point by mouse click on screen
# Signature: draw_operation :: (Integer,Integer) => Void
# Does: will operate the draw tile function with different game situation
# Test: draw_operation(200,100) => will draw tile by condition 

# Function: get_flip_position
# Parameters: x,y as two integer for row and column number
# Returns: Set
# Signature: get_flip_position:: (Integer, Integer)=>Set
# Does: get the flip positions for the legal position which tile will be draw
# Test: get_flip_position(3,4) => 
# {(3,5),(3,6),(4,4),(5,3),(6,2)} white is the set of where tiles will be flip



# Function: update_set
# Does: update the set for black or white or empty set, after each tile drawing
# Test: update_set(2,3) => if color is black, (2,3) will add into black_set
#          update_set(3,1) => if color is white, (3,1) will add into white_set