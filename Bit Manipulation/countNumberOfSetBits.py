# Given a number, return the number of set bits (1s)
def countBits(num):
    count = 0
    if num == 0:
        return count
    while num > 0:
        
        if num & 1:
            print("hey hey")
            count += 1
            print(count)
        print("num, count", num, count)
        num >>= 1
    return count
        
if __name__ == "__main__":
    print(countBits(2))


