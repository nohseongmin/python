#백준 1296 팀 이름 정하기

love = input()
count = int(input())

names = [input() for _ in range(count)]
best_score = -1
result = ""

for name in sorted(names):
    L = (love + name).count('L')
    O = (love + name).count('O')
    V = (love + name).count('V')
    E = (love + name).count('E')

    score = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

    if score > best_score:
        best_score = score
        result = name

print(result)
