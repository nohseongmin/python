#백준 2839 설탕 배달
def div(kg):
    cnt = 0
    while kg >= 0:
        if kg % 5 == 0:
            cnt += kg // 5
            return cnt
        kg -= 3
        cnt += 1
    return -1

print(div(int(input())))