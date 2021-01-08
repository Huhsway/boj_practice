n = int(input())
times = list(map(int,input().split()))

q = []

for i in range(n):
    q.append([times[i], i+1])

q.sort()
result = 0

for i in range(n):
    for j in range(i+1):
        result += q[j][0]

print(result)