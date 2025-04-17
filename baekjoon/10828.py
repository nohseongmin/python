#백준 10828 스택
import sys

count = int(sys.stdin.readline())
stack = []
for i in range(count):
    a = sys.stdin.readline().split()#.split(" ")은 위험
    if a[0] == "push":
        stack.insert(0, a[1])
    elif a[0] == "pop":
        if len(stack)==0:
            print("-1")
        else:
            print(stack.pop(0))
    elif a[0] == "size":
        print(len(stack))
    elif a[0] == "empty":
        if len(stack)==0:
            print("1")
        else:
            print("0")
    elif a[0] == "top":
        if len(stack)==0:
            print("-1")
        else:
            print(stack[0])
    else:
        quit()
