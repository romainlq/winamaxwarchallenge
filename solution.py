import sys
import math

# Generating player 1 and player 2 decks
p1, p2 = [], []

n = int(raw_input())# the number of cards for player 1
for i in xrange(n):
    cardp_1 = raw_input() # the n cards of player 1
    p1.append(cardp_1)


m = int(raw_input()) # the number of cards for player 2
for i in xrange(m):
    cardp_2 = raw_input()  # the m cards of player 2
    p2.append(cardp_2)

# Initializing a dictionnary with all the possible values
suits = ['S','D','H','C']
order = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
values = {}
for i in order:
    for j in suits:
        key = i+j
        value = order.index(i)
        values[key] = value

# Initializing a round count
count = 0


# This function returns which player wins the round
def compare(c1, c2):
    global values # Getting the values from the dictionnary

    if (values[c1] > values[c2]):
        return 1
    elif (values[c1] < values[c2]):
        return 2
    else:
        return 0


while True:
    # One loop = one game round
    try:
        dt1 = [p1.pop(0)]
        dt2 = [p2.pop(0)] # Taking the first card from the players decks
    except IndexError:
        # if there is an error, it means that one of the decks is empty, the game is over
        if len(p1) > 0:
            win = '1' # player 1 wins
        else:
            win = '2' # player 2 wins

        print win, count
        break

    # Incrementing game rounds
    count += 1

    # Dealing with war
    try:
        while compare(dt1[-1], dt2[-1]) == 0: # while we have a war on the table
            for i in range(4): # we add the cards to the decks on the table
                dt1.append(p1.pop(0))
                dt2.append(p2.pop(0))
    except IndexError:
        # if we get an error, it means that oe of the two decks is empty, game is over
        print 'PAT'
        break

    # Adding the cards to the round winner
    if compare(dt1[-1],dt2[-1]) == 1:
        p1 = p1 + dt1 + dt2
    else :
        p2 = p2 + dt1 + dt2
