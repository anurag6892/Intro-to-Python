# Anurag Mukkara
# June 11, 2014
# rps.py

player1 = raw_input("Player1? ")
player2 = raw_input("Player2? ")

if player1 == "Rock" and player2 == "Rock":
    result = "Tie!"
elif player1 == "Rock" and player2 == "Scissors":
    result = "Player 1 wins."
elif player1 == "Rock" and player2 == "Paper":
    result = "Player 2 wins."
elif player1 == "Scissors" and player2 == "Rock":
    result = "Player 2 wins."
elif player1 == "Scissors" and player2 == "Scissors":
    result = "Tie!"
elif player1 == "Scissors" and player2 == "Paper":
    result = "Player 1 wins."
elif player1 == "Paper" and player2 == "Rock":
    result = "Player 1 wins."
elif player1 == "Paper" and player2 == "Scissors":
    result = "Player 2 wins."
elif player1 == "Paper" and player2 == "Paper":
    result = "Tie!"
else:
    result = "This is not a valid object selection"

print result
