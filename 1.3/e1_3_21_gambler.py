# gambler.py
import sys
import stdio
import random
import numpy

# stake  = int(sys.argv[1])
# goal   = int(sys.argv[2])
# trials = int(sys.argv[3])
#
# bets = 0
# wins = 0
# for t in range(trials):
#     # Run one experiment.
#     cash = stake
#     while (cash > 0) and (cash < goal):
#         # Simulate one bet.
#         bets += 1
#         if random.randrange(0, 2) == 0:
#             cash += 1
#         else:
#             cash -= 1
#     if cash == goal:
#         wins += 1
# print bets, trials,'bets, trials,'
# stdio.writeln(str(100 * wins // trials) + '% wins')
# stdio.writeln('Avg # bets: ' + str(bets // trials))

# mygambler.py
stake = int(sys.argv[1]) # the initial invest money;
goal  = int(sys.argv[2]) # the goal amount of cash
trials= int(sys.argv[3]) # for each trial, it determines the output; after # of trials, average;
win_prob = float(sys.argv[4])

bets = 0
wins = 0
# s = '*' # when put s initilization outside for-loop, it multiplied for each i, but not clear up;
for t in range(trials):
    s = '*'
    cash = stake
    s = s*cash
    # print s,'s*cash'

    while 0 < cash < goal:
        bets += 1 # do a bet;
        # if random.randrange(0,2)==0:
        if numpy.random.choice(numpy.arange(0,2), p=[win_prob, 1-win_prob])==0:
            cash += 1
            s += '*'
        else:
            cash -= 1 # lose one bet;
            s = s[:-1]
        # print s
    if cash == goal:
        wins += 1
    # print 'one trial done'

print 'total wins over the total trials: %', float(wins)*100/trials # times 100 before /trials, otherwise -->0
print 'average bets in each trial:', bets/trials
print 'total bets in all the trials',bets
print 'total wins in all the trials',wins
print 'gain/invest', float((goal-stake)*wins)/bets # I tried 1 1000 10000--> 0.1% shows: