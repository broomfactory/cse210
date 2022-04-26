"""
    tictactoe.py
    Matthew Scoville
    CSE210
    
    A simple Tic-Tac-Toe game. 
"""

class GameBoard:
    def __init__(self):
        self.size = 3
        self.squares = [[0 for i in range(self.size)] for j in range(self.size)]
        self.gameover = False
        self.winner = None
        self.turn = 'X'
        self.draw = False
        self.maxIndex = self.size**2

        # Fill cells with index number (1-based)
        square = 1
        for row in self.squares:
            for i in range (len(row)):
                row[i] = square;
                square += 1;

    def print(self):
        """
            Prints the board to stdout
        """
        print()
        firstRow = True
        for row in self.squares:
            line = "|"
            for cell in row:
                line += str(cell) + "|"
            #if not firstRow:
            #    print ('+'+'-+'*self.size)
            firstRow = False
            print (line)
        print()

    def mark(self,cellNumber):
        """
            Marks cellNumber with the specified symbol (x or o)
            specified in self.turn
        """



        symbol = self.turn
        # Check for a valid symbol
        if symbol in ['X','O']:

            # Determine the row and column of cellNumber
            c = (cellNumber -1) % self.size 
            r = (cellNumber -1) // self.size

            # Make sure the cell is not already claimed
            if not(self.squares[r][c] in ['X','O']):
                self.squares[r][c] = symbol
                self.checkWinner()
                
                # Change to other person's turn
                if self.turn == 'X':
                    self.turn = 'O'
                else:
                    self.turn = 'X';
                
                # Indicate successful placement
                return True
            else:
                return False
    
    def checkWinner(self):
        """
            Checks to see if X or O has won
            If so, sets gameover = True, winner to the appropriate player
            and returns True
        """
        # Check rows

        for r in range(self.size):
            totalX = 0
            totalO = 0
            for c in range(self.size):
                if self.squares[r][c] == 'X':
                    totalX += 1
                elif self.squares[r][c] == 'O':
                    totalO += 1
            
            if totalX == self.size:
                self.winner = 'X'
                self.gameover = True
                return True

            if totalO == self.size:
                self.winner = 'O'
                self.gameover = True
                return True

        # Check columns

        for c in range(self.size):
            totalX = 0
            totalO = 0
            for r in range(self.size):
                if self.squares[r][c] == 'X':
                    totalX += 1
                elif self.squares[r][c] == 'O':
                    totalO += 1
            
            if totalX == self.size:
                self.winner = 'X'
                self.gameover = True
                return True

            if totalO == self.size:
                self.winner = 'O'
                self.gameover = True
                return True

        # Check diagonal 1


        totalX = 0
        totalO = 0
        for x in range(self.size):
            
            if self.squares[x][x] == 'X':
                totalX += 1
            elif self.squares[x][x] == 'O':
                totalO += 1
        
            if totalX == self.size:
                self.winner = 'X'
                self.gameover = True
                return True

            if totalO == self.size:
                self.winner = 'O'
                self.gameover = True
                return True   

        #Check diagonal 2
        totalX = 0
        totalO = 0
        
        for x in range(self.size):
            
            if self.squares[x][self.size-1 -x] == 'X':
                totalX += 1
            elif self.squares[x][self.size-1 -x] == 'O':
                totalO += 1
        
            if totalX == self.size:
                self.winner = 'X'
                self.gameover = True
                return True

            if totalO == self.size:
                self.winner = 'O'
                self.gameover = True
                return True

        #Check for a draw
        total = 0
        for c in range(self.size):            
            for r in range(self.size):
                if self.squares[r][c] in ['X','O']:
                    total += 1

        if total == self.maxIndex:
            self.gameover = True
            self.draw = True


        return False    

    def doTurn(self):
        """
            Gets input and marks the board
        """   

        prompt = self.turn + "'s turn to choose a square (1-" + str(self.maxIndex) + "):"

        success = False

        while not success:
            response = input(prompt)
            if response.strip().isdigit():
                index = int(response)

                if (index > 0 and index <= self.maxIndex):
                    success = self.mark(index)
                    if not success:
                        print("That square is taken. Please try again.")

                else:
                    print("Please choose a valid square.")
            else:
                print("Please enter a valid number.")


def main():
    game = GameBoard()
    
    game.print()

    while game.gameover == False:        
        game.doTurn()
        game.print()

    if game.draw:
        print("Game ends in a draw!")
    else:
        print(game.winner + " wins the game!")
        print("Thank you for playing.")


# If this file is executed like this:
# > py tictactoe.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()