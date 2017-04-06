# Problem 31

# How many different ways can 2 GBP be made using 1p, 2p, 5p, 10p, 20p, 50p,
# 1GBP, 2 GBP?

goal = 200 
coins = [1, 2, 5, 10, 20, 50, 100, 200]
combo = [1] + [0] * goal
for coin in coins:
    for i in range(coin, goal + 1):
        combo[i] += combo[i-coin]

print(combo)
input('\nexit')
