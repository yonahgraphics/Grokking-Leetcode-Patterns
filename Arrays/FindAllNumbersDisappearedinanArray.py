
def findDisappearedNumbers(nums):
    seen = set(nums)
    res = []
    for i in range(1, len(nums)+1):
        if i not in seen:
            res.append(i)
    return res
def findDisappearedNumbers1(nums):
    res = []
    for num in nums:
        index = abs(num)-1
        nums[index] = -1*abs(nums[index])
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i+1)
    return res
    

    

if __name__ == "__main__":
    print(findDisappearedNumbers([1,3,3,3]))
    print(findDisappearedNumbers1([1,3,3,3]))
        