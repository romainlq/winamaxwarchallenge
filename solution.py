import sys
import math
from collections import deque

# Generating player 1 and player 2 decks using deques
p1 = deque()
p2 = deque()

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

# Initializing a pat condition
pat = False

# This function returns which player wins the round
def compare(c1, c2):
    if (values[c1] > values[c2]):
        return 1
    elif (values[c1] < values[c2]):
        return 2
    else:
        return 0

dt1 = deque()
dt2 = deque()

while p1 and p2:
    # One loop = one game round
    dt1.append(p1.popleft())
    dt2.append(p2.popleft())

    # Incrementing game rounds
    count += 1

    # Dealing with war
    try:
        while compare(dt1[-1], dt2[-1]) == 0: # while we have a war on the table
            for i in range(4): # we add the cards to the decks on the table
                dt1.append(p1.popleft())
                dt2.append(p2.popleft())
    except:
        # if we get an error, it means that oe of the two decks is empty, game is over
        pat = True

    # Adding the cards to the round winner
    if not pat:
        if compare(dt1[-1],dt2[-1]) == 1:
            while dt1:
                p1.append(dt1.popleft())
            while dt2:
                p1.append(dt2.popleft())
        else :
            while dt1:
                p2.append(dt1.popleft())
            while dt2:
                p2.append(dt2.popleft())


if pat:
    print "PAT"
else:
    if not p1:
        print '2', count
    elif not p2:
        print '1', count
