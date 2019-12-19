'Nicholas, Syd, Esha, Evan'

'''
Iterative Prisoner's Dillema Team Submission

Nicholas, Syd, Esha, Evan

In this file, you MUST define the following:

Variables:
  - team_name:            a string with your team's name
  - strategy_name:        a string with your team's strategy name
  - strategy_description: a string with your team's strategy name

Functions:
  - move(my_last_move, their_last_move):
    your team's implementation of your strategy (see move() docstring)
'''

team_name = 'TEAM 7'
strategy_name = 'The Hunt Strategy'
strategy_description = 'Record the past 5 moves to determine a pattern and then choose a counter strategy'
alltheirmoves = []
move=0
def move(my_last_move, their_last_move):
    global alltheirmoves
    global move
    alltheirmoves+=[their_last_move]

    move+=1
    if move<5:
        return 'c'
    if move==6:
        return 'b'
    if move == 7 and their_last_move == 'b':
        return 'c'
    elif their_last_move =='c':
        return 'b'
    if alltheirmoves[range(6,12)] == 'c':
        return 'b'
    elif alltheirmoves[len(alltheirmoves-2)] == 'c' and alltheirmoves[len(alltheirmoves-3)] == 'c':
        return 'b'
    elif alltheirmoves[len(alltheirmoves-2)] == 'b' and alltheirmoves[len(alltheirmoves-3)] == 'b':
        return 'b'
    elif alltheirmoves[len(alltheirmoves-2)] == 'b' and alltheirmoves[len(alltheirmoves-3)] == 'c':
        return 'b'
    else:
        return 'c'
    
            
    '''
    Make my move based on the history with this player.

    my_last_move: a one letter String (c or b) that represents the last move you made
        against your opponent
    their_last_move: a one letter String (c or b) that represents the last move your
        opponent made against you
    Returns 'c' or 'b' for collude or betray.
    '''
    return 'c'

if __name__ == '__main__':
  move()
