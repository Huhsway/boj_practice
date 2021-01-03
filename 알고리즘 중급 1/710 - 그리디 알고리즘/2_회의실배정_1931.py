n = int(input())
meetings = []

for i in range(n):
    s, e = map(int,input().split())
    meetings.append([s,e])

meetings = sorted(meetings, key = lambda x : x[0])
meetings = sorted(meetings, key = lambda x : x[1])

previous_e = 0
cnt = 0

for i,j in meetings:
    if i >= previous_e:
        cnt += 1
        previous_e = j

print(cnt)