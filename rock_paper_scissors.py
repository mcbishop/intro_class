
one = raw_input("Player 1: Give me a value: rock, paper, or scissors. ")
two = raw_input("Player 2: Give me a value: rock, paper, or scissors. ")

def rock_paper_scissors(player1,player2):
	if (player1 == "rock" and player2 == "scissors") or (player2 == "rock" and player1 == "scissors"):
    		print "Rock wins. Rock smashes scissors."
	elif (player1 == "rock" and player2 == "paper") or (player2 == "rock" and player1 == "paper"):
			print "Paper wins. Paper wraps up rock."
	elif player1 == player2:
	 		print "It's a tie. "
	elif (player1 == "paper" and player2 == "scissors") or (player2 == "paper" and player1 == "scissors"):
	 		print "Scissors wins. Scissors cuts through paper."





rock_paper_scissors(one,two)
