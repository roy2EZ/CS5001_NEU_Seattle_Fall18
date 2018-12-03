import unittest



empty_position_set = {(3,4),(1,1),(2,2)}
n = 8

def is_in_empty_set(x,y):
    return ((x,y) in empty_position_set)

def check_inside_board(x,y):
    global n
    if x>=1 and x<=n and y>=1 and y<=n:
        return True
    else:
        return False



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
       
   
        



class TestMethods(unittest.TestCase):

    def test_is_in_empty_set(self):
        self.assertTrue(is_in_empty_set(3,4))

    def test_check_inside_board(self):
        self.assertTrue(check_inside_board(5,4))
        self.assertFalse(check_inside_board(8,9))
        self.assertFalse(check_inside_board(0,1))
        self.assertFalse(check_inside_board(12,-13))

    def test_game_over(self):
        white_set1 = {(1,2),(2,3),(3,4)}
        black_set1 = {(4,2),(7,3),(5,4),(3,6)}
        

        white_set2 = {(1,2),(2,3),(3,4),(4,5),(7,7)}
        black_set2 = {(4,2),(7,3),(5,4),(3,6)}
       

        self.assertEqual(game_over(white_set1,black_set1),"Black is the winner.")
        self.assertEqual(game_over(white_set2,black_set2),"White is the winner.")









suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
unittest.TextTestRunner(verbosity=2).run(suite)