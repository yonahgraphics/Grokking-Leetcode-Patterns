# Time complexity: O(n^m), when n == len(arr) and m = target
# Space complexity: O(m)
def canSum(target, arr):
    if target < 0: return False
    if target == 0: return True

    for i in range(len(arr)):
        remainder = target - arr[i]
        result = canSum(remainder, arr)
        if result == True:
            return True
    return False
# Time complexity: O(n*m), when n == len(arr) and m = target
# Space complexity: O(m)
def canSumOptimum(target, arr, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0: return True
    if target < 0: return False

    for i in range(len(arr)):
        remainder = target - arr[i]
        memo[remainder] = canSumOptimum(remainder, arr, memo)
        if memo[remainder] == True: return True
    memo[target] = False
    return False



if __name__ == "__main__":
    # print(canSum(500, [7,14]))
    print(canSumOptimum(300, [7, 14]))