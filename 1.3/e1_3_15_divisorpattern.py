"""
1.3.15 Compose a version of divisorpattern.py (PROGRAM 1.3.4) that uses while loops instead of for loops.
Option + Option +L to format lines
"""
import sys
import stdio

n = int(sys.argv[1])

# for i in range(1, n+1):
#     # Write the ith line.
#     for j in range(1, n+1):
#         # Write the jth entry in the ith line.
#         if (i % j == 0) or (j % i == 0):
#             stdio.write('* ')
#         else:
#             stdio.write(' ')
#     stdio.writeln(i)

i = 1
while i <= n:
    # Write the ith line.
    j = 1
    while j <= n:
        # Write the jth entry in the ith line.
        if (i % j == 0) or (j % i == 0):
            stdio.write('* ')
        else:
            stdio.write('  ')
        j += 1
    stdio.writeln(i)
    i += 1
