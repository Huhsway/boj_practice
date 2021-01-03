n, k = map(int, input().split())

coins = []
result = 0

for i in range(n):
    coin = int(input())
    coins.append(coin)

for i in range(n-1, -1, -1):
    if k // coins[i] > 0:
        result += (k // coins[i])
        k %= coins[i]

print(result)
