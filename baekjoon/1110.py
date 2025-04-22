#백준 1110 더하기 사이클
import sys
num = int(sys.stdin.readline())
first = num
cnt = 1
while True:
    tail = ((num%10)+(num//10))%10
    head = (num % 10)
    num = ((head%10)*10) + tail
    if first == num:
        break
    cnt += 1
print(cnt)
