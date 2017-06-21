#https://www.reddit.com/r/ProgrammingPrompts/comments/3mg2im/easymedium_tictactoe/
def draw_board(board):
	print("-------")
	for i in board:	
		for j in i:
			print("|"+j, end="")
		print("|")
	print("-------")
def get_not_valid(message):
	returnable=None
	while(returnable!="X" and returnable!="O"):
		returnable=input(message).upper()
	return returnable
def set_piece(board, player_val):
	row=int(input("Row:"))
	column=int(input("Column:"))
	while(board[row-1][column-1]!=" "):
		row=int(input("Row:"))
		column=int(input("Column:"))
	board[row-1][column-1]=player_val
	return board
def switch_player(player):
	if(player=="X"):
		return "O"
	else:
		return "X"
def turn(board, player_val):
	set_piece(board, player_val)
	win=check_winner(board, player_val)
	draw_board(board)
	return win
def check_winner(bo, le):
 # Given a board and a player’s letter, this function returns True if that player has won.
 # We use bo instead of board and le instead of letter so we don’t have to type as much.
	return ((bo[2][0] == le and bo[2][1] == le and bo[2][2] == le) or # across the top
	(bo[1][0] == le and bo[1][1] == le and bo[1][2] == le) or # across the middle
	(bo[0][0] == le and bo[0][1] == le and bo[0][2] == le) or # across the bottom
	(bo[2][0] == le and bo[1][0] == le and bo[0][0] == le) or # down the left side
	(bo[2][1] == le and bo[1][1] == le and bo[0][1] == le) or # down the middle
	(bo[2][2] == le and bo[1][2] == le and bo[0][2] == le) or # down the right side
	(bo[2][0] == le and bo[1][1]== le and bo[0][2] == le) or # diagonal
	(bo[2][2] == le and bo[1][1] == le and bo[0][0] == le)) # diagonal
player_token=get_not_valid("Please enter your token(X or O)")
curr_turn=get_not_valid("Which token should play first?")
board=[[" " for x in range(3)] for y in range(3)] 
print(board)
draw_board(board)
set_piece(board, curr_turn)
for turn_num in range(9):
	result=turn(board, curr_turn)
	if(result):
		print(curr_turn +" has won!")
		break;
	if(turn_num==8):
		print("Its a draw!")
	curr_turn=switch_player(curr_turn)
