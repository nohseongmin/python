#백준 2839 설탕 배달
def div(kg):
    cnt = 0
    if kg%5==0:
        while kg!=0:
            kg-=5
            cnt+=1
        return cnt
    elif kg%5==4:
        if kg%3!=0:
            return -1
        while kg!=0:
            kg-=3
            cnt+=1
        return cnt
    elif kg%5==3:
        while True:
            if kg//5>=1:
                kg-=5
                cnt+=1
            elif kg//3>=1:
                kg-=3
                cnt+=1
            if kg==0:
                return cnt
    elif kg%5==2 or kg%5==1:
        while True:
            if kg // 3 >=1:
                kg -= 3
                cnt += 1
            elif kg // 5 >=1:
                kg -= 5
                cnt += 1
            if kg == 0:
                return cnt
            elif kg%3!=0 and kg%5!=0:
                return -1
    else:
        return -1

print(div(int(input())))


