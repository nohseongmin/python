#백준 9012 괄호
import sys
def is_valid(line : str):
    stack = []
    for letter in line:
        if letter=="(":
            stack.append(letter)
        if letter==")":
            if len(stack)==0:
                return "NO"
            stack.pop()
    if len(stack)!=0:
        return "NO"
    return "YES"

count = int(sys.stdin.readline())
for _ in range(count):
    print(is_valid(sys.stdin.readline()))
