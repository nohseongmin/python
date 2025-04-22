#백준 1769 3의 배수
import sys

calc = int(sys.stdin.readline())
cnt = 0
while calc-10>=0:
    calc = sum(map(int, str(calc)))
    cnt+=1
print(cnt)
if calc%3!=0:
    print("NO")
else:
    print("YES")

