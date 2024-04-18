def fibonacci(n):
    fib_series = [0, 1]

    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series

num_terms = int(input("Enter the number of terms for Fibonacci series: "))

print(f"Fibonacci series up to {num_terms} terms:")
print(fibonacci(num_terms))
