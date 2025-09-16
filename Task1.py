def factorial(n):
    if n<0:
        return "undefine for negative numbers"
    elif n<2 :
        return 1
    else:
        return n * (factorial(n-1))

result = factorial(-1)
print(result)
