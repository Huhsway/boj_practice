# Brute Force로 푼다면 O(2^40*400)이 걸리는 문제

n = int(input())

coins = [list(map(str,list(input()))) for _ in range(n)]

answer = 21e8

def change(arr, s):

    for i in range(n):
        if arr[i][s] == 'H':
            arr[i][s] = 'T'
        else:
            arr[i][s] = 'H'

    return arr

def flip(s, e, coins):

    global answer

    if s == e:
        result = 0
        for i in range(n):
            tempT = 0
            tempH = 0
            for j in range(n):
                if coins[i][j] == 'T':
                    tempT += 1
                else:
                    tempH += 1
            result += tempT

            if tempT > tempH:
                result -= tempT
                result += tempH

        if answer > result:
            answer = result

        return

    flip(s+1,e,coins)
    coins = change(coins, s)
    flip(s+1,e,coins)
    coins = change(coins, s)

flip(0,n,coins)
print(answer)
