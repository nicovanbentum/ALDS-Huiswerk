def F(amount, coins):
    if amount < coins[0]:
        return

    A = [0 for _ in range(amount+1)]
    A[0] = 1

    for coin in coins:
        if coin > amount:
            break
		#because it's integers in integers we can create an index using the amount
        for i in range(coin, amount+1):
            A[i] += A[i-coin]

    return A[amount]


amount = 7
coins = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]

print(F(amount, coins))
