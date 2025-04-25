#백준 2444 별 찍기 - 7
first = int(input())
num = 2*first-1
for i in range(num):
    if i<first:
        print(" "*(first-1-i) + "*"*(i*2+1) + " ")
    else:
        break
for j in range(num, first, -1): # 8 7 6 5
    print(" "*((num-j)+1) + "*"*((j-first-1)*2+1) +" ")
