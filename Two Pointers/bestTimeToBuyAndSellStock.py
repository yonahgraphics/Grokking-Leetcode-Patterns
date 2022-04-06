'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any 
profit, return 0.
'''


# Tme Complexity: O(n*2) b'se we scan thru the array once albeit with two pointers.
# Space Complxity: O(1), no auxilliary space used.

def maxProfit1(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            curr_profit = prices[j] - prices[i]
            max_profit = max(max_profit, curr_profit)
    return max_profit
                            
# Tme Complexity: O(n) b'se we scan thru the array once albeit with two pointers.
# Space Complxity: O(1), no auxilliary space used.

def maxProfit(prices):
    max_profit = 0
    i = 0
    for j in range(1, len(prices)):
        profit = prices[j] - prices[i]
        if profit > 0: # Making profit
            max_profit = max(max_profit, profit) # Take max profit sofar
        else:
            i = j # Not making profits, buy another day
        
    return max_profit

if __name__ == "__main__":
    print(maxProfit([1,2,7,9,4,3,3]))
    print(maxProfit1([1,2,7,9,4,3,3]))
        
    
    
    