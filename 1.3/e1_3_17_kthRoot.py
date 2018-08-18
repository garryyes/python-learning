'''
nth root of a number using Newton's
'''
import sys

n = int(sys.argv[1])
k = int(sys.argv[2])
epsilon = 1e-15
t = n
temp = float((t**k -n))/t**(k-1)
print temp
while temp > t*epsilon: # here: referrging to the sqrt() method, using (1-
    t -= float(t**k -n)/k/t**(k-1)
    temp = float(t**k -n)/t**(k-1)
    print t, temp
print t

