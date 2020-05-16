def stockOptimize(prices):
    n = len(prices)
    if(n == 0):
        return 0
    max_index = prices.index(max(prices))
    spend = 0
    for i in range(max_index):
        spend += prices[i]
    profit = max_index*max(prices)-spend;
    profit += stockOptimize(prices[max_index+1:])
    return profit
    
t = int(input())

for i in range(t):
    n = int(input())
    prices = [int(x) for x in input().split(' ')]
    print(stockOptimize(prices))