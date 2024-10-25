def fun(n):
    sum = 1
    for i in range(1, n + 1):
        sum*= i
    return sum

print(fun(4))


def fun(n):
    sum= 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            sum *= j
    return sum
print(fun(4))