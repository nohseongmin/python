#백준 10773 제로
import sys
arr = []
count = int(sys.stdin.readline())
for i in range(0, count):
    temp = int(sys.stdin.readline())
    if temp!=0:
        arr.append(temp)
    else:
        arr.pop()
print(sum(arr))