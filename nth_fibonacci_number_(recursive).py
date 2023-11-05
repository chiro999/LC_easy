def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
 
if __name__ == "__main__":
    n = 7
    print(n, "th Fibonacci Number: ")
    print(fibonacci(n))
