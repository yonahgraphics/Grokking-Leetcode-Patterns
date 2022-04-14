'''
Left-shift, right-shift, check ith bit
'''
#Left shift a number num n times
def leftShift(num, n):
    num <<= n # num = num*(2**n)
    return num

#Right shift a number num n times
def rightShift(num, n):
    num >>= n # num = num//(2**n)
    return num

# Given a number, num and an index i, return True if the ith bit is set (is 1) and False otherwise
def chechIthBit(num, i):
    num >>= i
    if num | 0: # OR num & 1
        return True
    return False


if __name__ == "__main__":
    print(leftShift(3, 1))
    print(rightShift(3, 2))
    print(chechIthBit(12, 4))


