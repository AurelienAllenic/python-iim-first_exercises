fibonacci_cache={0:0, 1:1}

def fibonacci(n):

    if n not in fibonacci_cache:
        fibonacci_cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibonacci_cache[n]

print(fibonacci(60))