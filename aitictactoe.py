"""
https://krigar424-fusdk12-net.trinket.io/sites/ai-tic-tac-toe
"""
import random
l = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
blank=[]
player = "X"
game='no'
# List of winning moves
win_moves = [[l[0],l[1],l[2]],
              [ l[3],l[4],l[5]],
              [ l[6],l[7],l[8]],
              [ l[0],l[3],l[6]],
              [ l[1],l[4],l[7]],
              [ l[2],l[5],l[8]],
              [ l[0],l[4],l[8]],
              [ l[2],l[4],l[6]]]
# Print directions for game
print ("Are you ready to play tic-tac-toe against me?")
print ("\n You play as 'X' and I will be 'O'. You go first.")
print ('\n\n\n\n\nType the number of the corresponding position to make a move.')
print('''\n\n                          1 | 2 | 3 
                         ---|---|---
                          4 | 5 | 6 
                         ---|---|---
                          7 | 8 | 9 ''')
# While the game is on
while game=='no':  
  
  # Player's move - Ask player for an input for move
  if player=='X':
    input1=int(input("\nChoose an empty square to place your piece in."))
   
    ## Check if its a valid move: That is, position is between 1 - 9 and position is empty
    if input1>9 or input1<1:
      print 'Please choose a number from 1-9.'
      continue
    # If yes, Play X in square selected by the player set value of input
    if l[input1-1] == ' ':
      l[input1-1]=player
    else:
      print 'Please enter in an empty square.'
      continue
  # Computer's move - play O  
  elif player=='O':
    # If can win,win
    for x in range (len(l)):
      if l[x] == ' ':
        l[x] = 'O'
        win_moves = [ [l[0],l[1],l[2]],
                      [l[3],l[4],l[5]],  
              [ l[6],l[7],l[8]],
              [ l[0],l[3],l[6]],
              [ l[1],l[4],l[7]],
              [ l[2],l[5],l[8]],
              [ l[0],l[4],l[8]],
              [ l[2],l[4],l[6]]]
        if ['O','O','O'] in win_moves:
          turn='over'
          break
        else:
            l[x] = ' '
            
    if turn=='go':
      # If X will win in next turn, block it
      for x in range (len(l)):
        if l[x] == ' ':
          l[x] = 'X'
          win_moves = [ [l[0],l[1],l[2]],
                      [l[3],l[4],l[5]],  
              [ l[6],l[7],l[8]],
              [ l[0],l[3],l[6]],
              [ l[1],l[4],l[7]],
              [ l[2],l[5],l[8]],
              [ l[0],l[4],l[8]],
              [ l[2],l[4],l[6]]]
          if ['X','X','X'] in win_moves:
            l[x]='O'
            turn='over'
            break
          else:
              l[x] = ' '
    # If no winning move and center square is empty, play in center
    if turn=='go':
      if l[4]==' ':
        l[4]='O'
        turn='over'
    # If no winning move or blocking X or empty center square, play any move
    if turn=='go':
      for y in range (len(l)):
        if l[y]==' ':
          blank.append(y)
      l[random.choice(blank)]='O'
        
      blank=[] 
      turn='over'

  # Print the board after the move ###
  print ("\n "+(l[0])+' | '+(l[1])+' | '+(l[2]))
  print ('---|---|---')
  print (" "+(l[3])+' | '+(l[4])+' | '+(l[5]))
  print ('---|---|---')
  print (" "+(l[6])+' | '+(l[7])+' | '+(l[8]))
  win_moves = [[l[0],l[1],l[2]],
              [ l[3],l[4],l[5]],
              [ l[6],l[7],l[8]],
              [ l[0],l[3],l[6]],
              [ l[1],l[4],l[7]],
              [ l[2],l[5],l[8]],
              [ l[0],l[4],l[8]],
              [ l[2],l[4],l[6]]]
  # check if the current player won
  for win_position in win_moves: 
    if win_position==[player,player,player]:
      print '\n\n\n\n\n\n\n' + (player)+ ' wins!\n\n'
      game='yes'
      break
  # check if the board is full and game is a tie
  if ' ' not in [l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8]]:
    print "\n\n\n\n\n\nIt's a tie!\n\n"
    game='yes'
    break
  # Switch the player
  if player=='X':
    player='O'
    turn='go'
  elif player=='O':
    player='X'
#TIC TAC TOE
