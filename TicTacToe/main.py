#https://www.reddit.com/r/ProgrammingPrompts/comments/3mg2im/easymedium_tictactoe/
def draw_board(board):
	print("-------")
	for i in board:	
		for j in i:
			print("|"+j, end="")
		print("|")
	print("-------")
player_token=None
while(player_token!="X" and player_token!="O"):
	player_token=input("Please enter your token(X or O)").upper()
curr_turn=None
while(curr_turn!="X" and curr_turn!="O"):
	curr_turn=input("Which token should play first?").upper()
board=[["X" for k in range(3)]]*3
draw_board(board)