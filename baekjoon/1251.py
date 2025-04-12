#백준 1251 단어 나누기
word=list(input())
result = []

for i in range(1, len(word)-1):
    for j in range(1+i, len(word)):
        first = word[:i]
        second = word[i:j]
        third = word[j:]

        first.reverse()
        second.reverse()
        third.reverse()

        result.append("".join(first + second + third))

print(min(result))

