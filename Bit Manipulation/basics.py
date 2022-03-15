'''
Left-shift, right-shift
'''
def leftShift(num, n):
    num <<= n # num = num*(2**n)
    return num
def rightShift(num, n):
    num >>= n
    return num

if __name__ == "__main__":
    print(leftShift(3, 1))
    print(rightShift(3, 1))


