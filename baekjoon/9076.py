#백준 9076 점수 집계
count = int(input())
result = []
line = []
for i in range(count):
    line = [int(x) for x in input().split(" ")]
    line.sort(reverse=True)
    if line[1]>=line[3]+4:
        result.append("KIN")
    else:
        sum = line[1]+line[2]+line[3]
        result.append(sum)
        sum = 0
    line.clear()
for k in range(len(result)):
    print(result[k])