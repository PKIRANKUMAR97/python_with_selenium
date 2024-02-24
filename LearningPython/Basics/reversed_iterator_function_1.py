tup_1 = (3, 8, 1, 9, 34, 37, 99, 187)
x = reversed(tup_1)
print(x)  # gives the address
print(next(x))  # gives the iterator item in the reverse
print(next(x))
print(next(x))
print(next(x))
