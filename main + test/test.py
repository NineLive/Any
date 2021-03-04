def func(x):
    action = (lambda n: x ** n)
    return action


x = func(4)
print(x(2))
