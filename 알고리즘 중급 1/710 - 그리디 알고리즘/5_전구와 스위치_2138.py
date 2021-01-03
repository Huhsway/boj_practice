n = int(input())

line = list(map(int, input()))
target = list(map(int, input()))


def change(a, idx):
    for i in range(idx - 1, idx + 2):
        if i < 0 or i >= len(a):
            continue
        if a[i] == 0:
            a[i] = 1
        else:
            a[i] = 0


def check(a, b, n, state):
    cnt = 0

    a = list(a)

    if state:
        change(a, 0)
        cnt += 1

    for i in range(1, n):
        if a[i - 1] != b[i - 1]:
            change(a, i)
            cnt += 1

    if a != b:
        cnt = 21e8

    return cnt


answer = min(check(line, target, n, False), check(line, target, n, True))
if answer == 21e8:
    answer = -1
print(answer)
