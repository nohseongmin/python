#백준 2441 별 찍기-4
import sys
count = int(sys.stdin.readline())
for i in range(count):
    print(" "*i + "*"*(count-i))