# Name:
# Section:
# nims.py

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    stones_left = pile

    ## Basic structure of program (feel free to alter as you please):

    while stones_left > 0:
        valid_input1 = False
        while(valid_input1 == False):
            player1_input = input("Enter player 1 choice")
            if player1_input < 1:
                print "Should be greater than 0"
            elif player1_input > max_stones:
                print "Should be less than", max_stones+1
            elif player1_input > stones_left:
                print "Not enough stones remaining"
            else
                valid_input1 = True
            
        stones_left -= player1_input
        if (stones_left == 0):
            print "Player 1 wins!"
            break

        valid_input2 = False
        while(valid_input2 == False):
            player2_input = input("Enter player 2 choice")
            if player2_input < 1:
                print "Should be greater than 0"
            elif player2_input > max_stones:
                print "Should be less than", max_stones+1
            elif player2_input > stones_left:
                print "Not enough stones remaining"
            else
                valid_input2 = True

       stones_left -= player2_input
       if (stones_left == 0):
            print "Player 2 wins!"
            break
        
    print "Game over"







