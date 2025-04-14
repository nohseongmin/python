#백준 10807 개수 세기
repeat : int = int(input())
line = [int(x) for x in input().split(" ")]
num = int(input())
print(line.count(num))
