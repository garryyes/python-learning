'''
Modify binary.py to create a program kary.py that takes i and k as command-line arguments and converts i to base k. Assume that k is an integer between 2 and 16. For bases greater than 10, use the letters A through F to represent the 11th through 16th digits, respectively.
'''
# convert i to base k
import sys
i = float(sys.argv[1])
k = int(sys.argv[2])
inti = int(i)
floati = i-int(i)
maxorder = 0
temp = k ** maxorder

while temp <= inti:
    maxorder += 1
    temp = k ** maxorder
print maxorder, temp, inti

s = ''
marker = 'ABCDEF' # if k is larger than 10, then need letters to represent 10,11,12,13,14,15, etc
for j in range(maxorder-1, -1,-1):
    x = k ** j
    if inti / x < 10:
        s += str(inti/x) + ' '
    else:
        s += marker[inti/x-10] + ' '
    inti = inti % x
print s


