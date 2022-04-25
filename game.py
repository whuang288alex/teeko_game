import random
import copy

class TeekoPlayer:
    """ An object representation for an AI game player for the game Teeko.
    """
    board = [[' ' for j in range(5)] for i in range(5)]
    pieces = ['b', 'r']
    max_depth = 2

    def __init__(self):
        """ Initializes a TeekoPlayer object by randomly selecting red or black as its
        piece color.
        """
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]

    def change_state(self, state, move):
        if len(move) > 1:
            state[move[1][0]][move[1][1]] = ' '
        state[move[0][0]][move[0][1]] = self.my_piece
        
    def is_move_phase(self, state):
        return sum((i.count('b') for i in state)) >= 4 and sum((i.count('r') for i in state)) >= 4
        
    def make_move(self, state):
        #Get all possible moves by the AI
        successors = self.succ(state, self.my_piece)
        #Evaluate all moves
        best_move = None
        max_possible_score = None
        for suc in successors:
            #Generate each new state according to each move and score them
            new_state = copy.deepcopy(state)
            self.change_state(new_state, suc)
            score = self.max_value(new_state, 0)
            #If this is the best move so far, record it
            if best_move == None or score >= max_possible_score:
                best_move = suc
                max_possible_score = score
        return best_move
    
    def max_value(self, state, depth): 
        if self.game_value(state) != 0:
            return self.game_value(state)
        
        elif depth >= self.max_depth:
            return self.heuristic_game_value(state, self.my_piece)

        else:
            score = list()
            successors = self.succ(state, self.my_piece)
            for suc in successors:
                #Generate each new state
                new_state = copy.deepcopy(state)
                self.change_state(new_state, suc)
                score.append(self.min_value(new_state, depth + 1))
            return max(score)
    
    def min_value(self, state, depth):
        
        if self.game_value(state) != 0:
            return self.game_value(state)
        
        elif depth >= self.max_depth:
            return self.heuristic_game_value(state, self.opp)   
        
        else:
            score = list()
            successors = self.succ(state, self.opp)
            for suc in successors:
                #Generate each new state
                new_state = copy.deepcopy(state)
                self.change_state(new_state, suc)
                score.append(self.max_value(new_state, depth + 1))
            return min(score)
    
    def heuristic_game_value(self, state, piece):
        
        max_for_ai = 0
        max_for_player = 0
        
        #Check horizontal
        for i in range(5):
            ai_count = 0
            player_count = 0
            for j in range(5):
                if state[i][j] == self.my_piece:
                    ai_count += 1
                if state[i][j] == self.opp:
                    player_count += 1
            if ai_count > max_for_ai:
                max_for_ai = ai_count  
            if player_count > max_for_player:
                max_for_player = player_count    
                
        #Check vertical  
        for i in range(5):
            ai_count = 0
            player_count = 0
            for j in range(5):
                if state[j][i] == self.my_piece:
                    ai_count += 1
                if state[j][i] == self.opp:
                    player_count += 1
            if ai_count > max_for_ai:
                max_for_ai = ai_count  
            if player_count > max_for_player:
                max_for_player = player_count  
        
        #Check diagonal 1
        for i in range(3, 5):
            for j in range(2):
                ai_count = 0
                player_count = 0
                if state[i][j] == self.my_piece:
                    ai_count += 1
                if state[i - 1][j + 1] == self.my_piece:
                    ai_count += 1
                if state[i - 2][j + 2] == self.my_piece:
                    ai_count += 1
                if state[i - 3][j + 3] == self.my_piece:
                    ai_count += 1 
                     
                if state[i][j] == self.opp:
                    player_count += 1
                if state[i - 1][j + 1] == self.opp:
                    player_count += 1
                if state[i - 2][j + 2] == self.opp:
                    player_count += 1
                if state[i - 3][j + 3] == self.opp:
                    player_count += 1
                      
                if ai_count > max_for_ai:
                    max_for_ai = ai_count  
                if player_count > max_for_player:
                    max_for_player = player_count 
        
        #Check diagonal 1
        for i in range(2):
            for j in range(2):
                ai_count = 0
                player_count = 0
                if state[i][j] == self.my_piece:
                    ai_count += 1
                if state[i + 1][j + 1] == self.my_piece:
                    ai_count += 1
                if state[i + 2][j + 2] == self.my_piece:
                    ai_count += 1
                if state[i + 3][j + 3] == self.my_piece:
                    ai_count += 1 
                     
                if state[i][j] == self.opp:
                    player_count += 1
                if state[i + 1][j + 1] == self.opp:
                    player_count += 1
                if state[i + 2][j + 2] == self.opp:
                    player_count += 1
                if state[i + 3][j + 3] == self.opp:
                    player_count += 1
                
                if ai_count > max_for_ai:
                    max_for_ai = ai_count  
                if player_count > max_for_player:
                    max_for_player = player_count 
        
        #Check box
        for i in range(4):
            for j in range(4):
                ai_count = 0
                player_count = 0
                if state[i][j] == self.my_piece:
                    ai_count += 1
                if state[i +1][j] == self.my_piece:
                    ai_count += 1
                if state[i][j + 1] == self.my_piece:
                    ai_count += 1
                if state[i + 1][j + 1] == self.my_piece:
                    ai_count += 1 
                    
                if state[i][j] == self.opp:
                    player_count += 1
                if state[i + 1][j] == self.opp:
                    player_count += 1
                if state[i ][j + 1] == self.opp:
                    player_count += 1
                if state[i + 1][j + 1] == self.opp:
                    player_count += 1
                
                if ai_count > max_for_ai:
                    max_for_ai = ai_count  
                if player_count > max_for_player:
                    max_for_player = player_count 
                    
        # Determine who is in a better spot according to current state
        if max_for_ai == max_for_player:
            return 0
        elif piece == self.my_piece:
            if max_for_ai > max_for_player:
                return max_for_ai/5.0
            else:
                return (-1.0) * max_for_player/5.0
        else:
            if max_for_ai < max_for_player:
                return max_for_player/5.0
            else:
                return (-1.0) * max_for_ai/5.0
    
    def succ(self, state, piece):
        move_phase = self.is_move_phase(state)
        successors = list()
        if move_phase:
            for i in range(5):
                for j in range(5):
                    if state[i][j] == piece:
                        if j + 1 <= 4 and state[i][j+1] ==' ':
                            successors.append([(i,j+1),(i,j)])
                        elif i + 1 <= 4 and state[i+1][j] ==' ':
                            successors.append([(i+1,j),(i,j)])
                        elif j - 1 >= 0 and state[i][j-1] ==' ':
                            successors.append([(i,j-1),(i,j)])
                        elif i - 1 >= 0 and state[i-1][j] ==' ':
                            successors.append([(i-1,j),(i,j)])
                        elif i - 1 >= 0 and j - 1 >= 0 and state[i-1][j-1] ==' ':
                            successors.append([(i-1,j-1),(i,j)])
                        elif i - 1 >= 0 and j + 1 <= 4 and state[i-1][j+1] ==' ':
                            successors.append([(i-1,j+1),(i,j)])
                        elif i + 1 <= 4 and j - 1 >= 0 and state[i+1][j-1] ==' ':
                            successors.append([(i+1,j-1),(i,j)])
                        elif i + 1 <= 4 and j + 1 <= 4 and state[i+1][j+1] ==' ':
                            successors.append([(i+1,j+1),(i,j)])              
        else:
            for i in range(5):
                for j in range(5):
                    if state[i][j] == ' ':
                        successors.append([(i,j)])
        return successors
           
    def opponent_move(self, move):
        """ Validates the opponent's next move against the internal board representation.
        You don't need to touch this code.

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.
        """
        # validate input
        if len(move) > 1:
            source_row = move[1][0]
            source_col = move[1][1]
            if source_row != None and self.board[source_row][source_col] != self.opp:
                self.print_board()
                print(move)
                raise Exception("You don't have a piece there!")
            if abs(source_row - move[0][0]) > 1 or abs(source_col - move[0][1]) > 1:
                self.print_board()
                print(move)
                raise Exception('Illegal move: Can only move to an adjacent space')
        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")
        # make move
        self.place_piece(move, self.opp)

    def place_piece(self, move, piece):
        """ Modifies the board representation using the specified move and piece

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

                This argument is assumed to have been validated before this method
                is called.
            piece (str): the piece ('b' or 'r') to place on the board
        """
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece
      
    def game_value(self, state):
        """ Checks the current board status for a win condition

        Args:
        state (list of lists): either the current state of the game as saved in
            this TeekoPlayer object, or a generated successor state.

        Returns:
            int: 1 if this TeekoPlayer wins, -1 if the opponent wins, 0 if no winner
        """
        # check horizontal wins
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i+1] == row[i+2] == row[i+3]:
                    return 1 if row[i]==self.my_piece else -1

        # check vertical wins
        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i+1][col] == state[i+2][col] == state[i+3][col]:
                    return 1 if state[i][col]==self.my_piece else -1

        # check \ diagonal wins
        for i in range(2):
            for j in range(2):
                if state[i][j] != ' ' and state[i][j] == state[i+1][j+1] == state[i+2][j+2] == state[i+3][j+3]:
                    return 1 if state[i][j] == self.my_piece else -1
        
        # check / diagonal wins 
        for i in range(3,5):
            for j in range(2):
                if state[i][j] != ' ' and state[i][j] == state[i-1][j+1] == state[i-2][j+2] == state[i-3][j+3]:
                    return 1 if state[i][j]==self.my_piece else -1
        
        # check box wins
        for i in range(4):
            for j in range(4):
                if state[i][j] != ' ' and state[i][j] == state[i][j+1] == state[i+1][j] == state[i+1][j+1]:
                    return 1 if state[i][j]==self.my_piece else -1

        return 0 # no winner yet

    def print_board(self):
        """ Formatted printing for the board """
        for row in range(len(self.board)):
            line = str(row)+": "
            for cell in self.board[row]:
                line += cell + " "
            print(line)
        print("   A B C D E")

############################################################################
#
# THE FOLLOWING CODE IS FOR SAMPLE GAMEPLAY ONLY
#
############################################################################
def main():
    print('Hello, this is Samaritan')
    ai = TeekoPlayer()
    piece_count = 0
    turn = 0

    # drop phase
    while piece_count < 8 and ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece+" moved at "+chr(move[0][1]+ord("A"))+str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp+"'s turn")
            while not move_made:
                player_move = input("Move (e.g. B3): ")
                while player_move[0] not in "ABCDE" or player_move[1] not in "01234":
                    player_move = input("Move (e.g. B3): ")
                try:
                    ai.opponent_move([(int(player_move[1]), ord(player_move[0])-ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        piece_count += 1
        turn += 1
        turn %= 2

    # move phase - can't have a winner until all 8 pieces are on the board
    while ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece+" moved from "+chr(move[1][1]+ord("A"))+str(move[1][0]))
            print("  to "+chr(move[0][1]+ord("A"))+str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp+"'s turn")
            while not move_made:
                move_from = input("Move from (e.g. B3): ")
                while move_from[0] not in "ABCDE" or move_from[1] not in "01234":
                    move_from = input("Move from (e.g. B3): ")
                move_to = input("Move to (e.g. B3): ")
                while move_to[0] not in "ABCDE" or move_to[1] not in "01234":
                    move_to = input("Move to (e.g. B3): ")
                try:
                    ai.opponent_move([(int(move_to[1]), ord(move_to[0])-ord("A")),
                                    (int(move_from[1]), ord(move_from[0])-ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        turn += 1
        turn %= 2

    ai.print_board()
    if ai.game_value(ai.board) == 1:
        print("AI wins! Game over.")
    else:
        print("You win! Game over.")

if __name__ == "__main__":
    main()
