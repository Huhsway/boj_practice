n, m = map(int, input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
b = [list(map(int,list(input()))) for _ in range(n)]

cnt = 0

def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True

def solve(y, x):
    for i in range(y, y+3):
        for j in range(x, x+3):
            a[i][j] = 1-a[i][j]

for i in range(0,n-2):
    for j in range(0,m-2):
        if a[i][j] != b[i][j]:
            cnt+=1
            solve(i,j)

if check():
    print(cnt)
else:
    print(-1)