def factorial_func(num):
    result=1
    if num>0:
        result = num * factorial_func(num-1)
    return result

num = int(input())
print(factorial_func(num))