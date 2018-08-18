
import stdio
import sys
import math
import random

# # write 'Hello, World' to standard output.
# stdio.writeln('Hello, World')
# # stdio.writeln(4)
# # stdio.writeln(Hello,
# # World)
# # stdio.writeln('Hello, World')
# # stdio.writeln('Hello, World')
# # stdio.writeln('Hello, World')
# # stdio.writeln('Hello, World')
# # stdio.writeln('Hello, World')
# # stdio.writeln('Hello, World')
# # stdio.writeln('Hello, World')
#
# # writeln('Hello, World')
#
# import sys
# import stdio
#
# stdio.write ('Hi ')
# stdio.write (sys.argv[3])
# stdio.write (', ')
# stdio.write (sys.argv[2])
# stdio.write (', and ')
# stdio.write (sys.argv[1])
# stdio.writeln('. How are you?')
#
# # ruler.py
# ruler1 = '1'
# ruler2 = ruler1 +'2' + ruler1
# ruler3 = ruler2 +'3' +ruler2
# ruler4 = ruler3 +'4' + ruler3
# stdio.writeln(ruler1)
# stdio.writeln(ruler2)
# stdio.writeln(ruler3)
# stdio.writeln(ruler4)

# a = 13
# b = 15
# stdio.writeln(str(a) + ' + ' + str(b) + ' = ' + str(a+b))
# # stdio.writeln(str(a) + ' + ' + str(b) + ' = ' str(a+b)) has to use + operator

# intops.py
# a = int(sys.argv[1])
# b = int(sys.argv[2])
# total = a + b
# diff = a - b
# prod = a * b
# quot = a // b
# rem = a % b
# exp = a ** b
# stdio.writeln(str(a) + ' +  ' + str(b) + ' = ' + str(a+b))
# stdio.writeln(str(a) + ' -  ' + str(b) + ' = ' + str(diff))
# stdio.writeln(str(a) + ' *  ' + str(b) + ' = ' + str(prod))
# stdio.writeln(str(a) + ' // ' + str(b) + ' = ' + str(quot))
# stdio.writeln(str(a) + ' %  ' + str(b) + ' = ' + str(rem))
# stdio.writeln(str(a) + ' ** ' + str(b) + ' = ' + str(exp))

#quadratic.py
# b = float(sys.argv[1])
# c = float(sys.argv[2])
# discriminant = b*b - 4.0* c
# d = math.sqrt(discriminant)
# stdio.writeln((-b + d)/2)
# stdio.writeln((-b - d) / 2.0)

# # leapyear.py
# year = int(sys.argv[1])
# isLeapYear = (year % 4 == 0)
# isLeapYear = isLeapYear and (year % 100 != 0)
# isLeapYear = isLeapYear or year %400 ==0 # a composite result: %4=0 but %100 not; or %400=0
# stdio.writeln(isLeapYear)
#
# def isLeapYear(x):
#     if x % 4 != 0:
#         return False
#     if x % 100 ==0 and x%400 != 0:
#         return False
#     return True
#
# print isLeapYear(2)
# print isLeapYear(20)
# print isLeapYear(1900)
# print isLeapYear(2096)

#1.2.2
# cos2+sin2~1.0.py
# theta = float(sys.argv[1])
# stdio.writeln(math.cos(theta)**2 + math.sin(theta)**2)

#1.2.5
# stdio.writeln(2.2 + 3.3)
# stdio.writeln('2' + '3')
# stdio.writeln('2.2' + '3.3')
# stdio.writeln(str(2) + str(3))
# stdio.writeln(str(2.2) + str(3.3))
# stdio.writeln(int('2') + int('3'))
# stdio.writeln(int('2' + '3'))
# stdio.writeln(float('2') + float('3'))
# stdio.writeln(float('2' + '3'))
# stdio.writeln(int(2.6 + 2.6))
# stdio.writeln(int(2.6) + int(2.6))

 # 1.2.6. quadratic.py
# b = float(sys.argv[1])
# b = 0
# c = -float(sys.argv[2])
# discriminant = b*b - 4.0* c
# # d = math.sqrt(discriminant)
# d = sqrt(discriminant)
# stdio.writeln((-b + d)/2)
# stdio.writeln((-b - d) / 2.0)

#1.2.11
# x = int(sys.argv[1])
# y = int(sys.argv[2])
# stdio.writeln((x % y ==0 and x/y %2 ==0) or (y % x ==0 and y/x %2 ==0))

#1.2.12
# x = int(sys.argv[1])
# y = int(sys.argv[2])
# z = int(sys.argv[3])
# stdio.writeln(not(x >= y+z or y >= x+z or z >= x+y))

#1.2.17
# stdio.writeln(random.randrange(1,6)+random.randrange(1,6))

#1.2.21
# P = float(sys.argv[1])
# t = float(sys.argv[2])
# r = float(sys.argv[3])
# stdio.writeln(P*math.exp(r*t)) #math.e is e; math.exp(x) is e**x

#1.2.32 dragon curve
# # if n == 0:
# res = 'F'
# stdio.writeln('n=0 '+ res)
# revres = 'F'
#
# # f n == 1:
# res = res+'L' + revres
# stdio.writeln('n=1 ' + res)
# revres = res.replace('L','E').replace('R','L').replace('E','R')[::-1]
#
# res = res+'L' + revres
# stdio.writeln('n=2 ' + res)
# revres = res.replace('L','E').replace('R','L').replace('E','R')[::-1]
#
# res = res+'L' + revres
# stdio.writeln('n=3 ' + res)
# revres = res.replace('L','E').replace('R','L').replace('E','R')[::-1]
#
# res = res+'L' + revres
# stdio.writeln('n=4 ' + res)
# revres = res.replace('L','E').replace('R','L').replace('E','R')[::-1]
#
# res = res+'L' + revres
# stdio.writeln('n=5 ' + res)
# revres = res.replace('L','E').replace('R','L').replace('E','R')[::-1]

# # flip.py
# if random.randrange(0,2)==0:
#     print 'head'
# else:
#     print 'tail'
#

# #poweroftwo.py
# end = int(sys.argv[1])
# power = 1.0/2 # int 1/2 =0!!!! not =0.5
# i = 0
# while i <= end:
#     power = power * 2
#     print power
#     i += 1

# target = int(sys.argv[1])
# power = 1.0/2 # int 1/2 =0!!!! not =0.5
# # i = 0
# while power <= target:
#
#     print power
#     power = power * 2
#     # i += 1

# # newton_sqrt.py # here: I typed 233333333, and it iterates more than 200 times; when using t*epsilon, it cuts to
# # about 10 times...?
# def sqrtt():
#     c = float(sys.argv[1])
#     epsilon = 1e-15
#     t = c
#     while abs(t-c/t) > epsilon*t: # it used: epsilon*t in book?
#         print t, 'any'
#         t = (c/t + t)/2
#         print abs(t - c / t),'abs(t-c/t)', t*epsilon
#     print t
#     return
# sqrtt()


# # binary.py
# target = int(sys.argv[1])
# power = 1
# i = 0
# while power*2 <= target:
#     power *= 2
#     i += 1
# print power, i, target,'power, i,s, target' # find the largest possible power; then decrease down
#
# target -= 2**i
# s ='' # concatenate string with a list--> if s is [], using s.append(); if s is '',using s+'1'
# for j in range(i-1,-1,-1):
#     # if target == 0:
#     #     break # this is OK if you have defined a string as containing i '0000000'; so that you can simply replace 0-1
#     if 2**j <= target:
#         s = s +'1'
#         target -= 2**j
#     else:
#         s = s + '0'
#     print j,target,'j,target'
# print '1'+s

# monte calo.py
# gambler.py
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

# # mygambler.py
# stake = int(sys.argv[1]) # the initial invest money;
# goal  = int(sys.argv[2]) # the goal amount of cash
# trials= int(sys.argv[3]) # for each trial, it determines the output; after # of trials, average;
#
# bets = 0
# wins = 0
#
# for t in range(trials):
#     cash = stake
#     while 0 < cash < goal:
#         bets += 1 # do a bet;
#         if random.randrange(0,2)==0:
#             cash += 1
#         else:
#             cash -= 1 # lose one bet;
#     if cash == goal:
#         wins += 1
# print 'total wins over the total trials: %', float(wins)*100/trials # times 100 before /trials, otherwise -->0
# print 'average bets in each trial:', bets/trials
# print 'total bets in all the trials',bets
# print 'total wins in all the trials',wins
# print 'gain/invest', float((goal-stake)*wins)/bets # I tried 1 1000 10000--> 0.1% shows:

# prime.py
def prime():
    target = int(sys.argv[1])
    # primelist = [] # no need to list the primes here, as when it increases by 1, any non-prime will be removed;
    factor = 2
    s = []
    while target >= factor:
        while target % factor ==0:
            target //= factor
            s.append(factor)
        factor += 1
    return s
# print prime()

# optimizedprime.py # the outter loop terminization condition
def prime():
    target = int(sys.argv[1])
    # primelist = [] # no need to list the primes here, as when it increases by 1, any non-prime will be removed;
    factor = 2
    s = []
    while target >= factor* factor:
        while target % factor ==0:
            target //= factor
            s.append(factor)
        factor += 1
    if target > 1: # itself as a factor
        s.append(target)
    return s
# print prime() # nothing should be placed inside the () before running, as this function doesn't take argument in ()

#1.3.1
def EqualInt(x,y,z):
    if x==y ==z:
        print 'equal'
    else:
        print 'not equal'
# EqualInt(7,8,0)

#1.3.2
def quadratic(a,b,c):
    if a ==0 and b!= 0:
        return -float(c)/b
    if a==b== 0 and c!= 0:
        return 'No root'
    discriminant = float(b*b - 4*c)
    if discriminant <0:
        # print 'no real root'
        return 'no real root'
    return (-b + math.sqrt(discriminant))/2/a, (-b - math.sqrt(discriminant))/2/a
# print quadratic(0,2,3)
# print quadratic(0,0,3)
# print quadratic(1,2,-3)
# print quadratic(1,2,3)

# #1.3.3
# x = float(sys.argv[1])
# y = float(sys.argv[2])
# if 0.0 <= x <= 1.0 and 0.0 <= y <= 1.0:
#     print 'True'
# else:
#     print 'False'

#1.3.5
# 45; 0; 45

#1.3.6 hello.py
def hellos(n):
    # s = ['1st hello\n','2nd hello\n', '3rd hello\n', 'th hello\n', 'ith hello\n']
    if n == 0:
        return None
    # s =[]
    for i in range (1,n+1):
        if i %10 ==1 and i%100 != 11:
            print str(i) + 'st hello'
        elif i %10 ==2 and i%100 != 12:
            print str(i) + 'nd hello'
        elif i %10 ==3 and i%100 != 13:
            print str(i) + 'rd hello'
        else:
            print str(i) + 'th hello'
    return
# hellos(114)

# #1.3.7 fiveperline.py
# s = ''
# for i in range(1000, 1200):
#     if i % 5 != 4:
#         s += str(i) +' '
#         # print s
#     else:
#         s += str(i) +'\n'
# print s

# ruler = '1'
# stdio.writeln(ruler)
# for i in range(2, 100):
#     ruler = ruler + ' ' + str(i) + ' ' + ruler
#     stdio.writeln(ruler)

# #1.3.10 functiongrowth.py
# s = ''
# for i in range(1,12):
#     n = 2**i
#     s += str(math.log(n,2)) +'\t' + str(n) +'\t' + str(n*math.log(n)) +'\t' + str(n*n) +'\t' + str(n**3) +'\t' + str(
#         2**n) + '\n'
# print s
#
# n = 123456789
# m = 0
# while n != 0:
#     m = (10 * m) + (n % 10)
#     n /= 10
# print m,n

# f = 0
# g = 1
# for i in range(16):
#     stdio.writeln(f)
#     f = f + g
#     g = f - g

#1.3.3

n = float(sys.argv[1])


