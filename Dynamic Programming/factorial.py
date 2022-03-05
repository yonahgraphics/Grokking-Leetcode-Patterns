 # Iteratively
 # Time Complexity: O(n), where n is the nth number
 # Space Complexity: O(1)
def factorial(n):
    if n == 0:
       return 1
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

# Time Complexity: O(n), where n is the nth number
 # Space Complexity: O(n), since it has to add stack frames for each function call
def factorialRecursive(n):
    if n == 0 or n == 1:
        return 1
    return n*factorialRecursive(n-1)

if __name__ == "__main__":
    print(factorial(200))
    print(factorialRecursive(200))