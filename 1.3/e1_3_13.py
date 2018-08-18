'''
exercise 1.3.13 positive power of 2: cost of calculating 2**i if used in while conditionals;
thus use 'temp' to receive the value after one calculation;
'''
import sys
n = float(sys.argv[1])
s = ''
i = 1
temp = 2

while temp <= n:
    s += str(temp)+' '
    i += 1
    temp = 2 ** i
print s



