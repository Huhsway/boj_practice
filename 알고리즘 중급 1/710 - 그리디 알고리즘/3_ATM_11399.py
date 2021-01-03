n = int(input())
times = list(map(int,input().split()))

q = []
for i in range(n):
    temp = []
    temp.append(times[i])
    temp.append(i+1)
    q.append(temp)

q.sort()
result = 0

for i in range(n):
    for j in range(i+1):
        result += q[j][0]

print(result)