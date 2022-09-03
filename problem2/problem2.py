# limit = 4E6 # four million (scientific notation)
limit = 4E4 # four million (scientific notation)

# calculate the fibonacci sequence up to limit

a = 1
b = 1
fibonacci_sum = 0

while True:
    _sum = a + b

    print(_sum, "\n")
    b = a
    a = a + b

    if(a > limit): break

# while True:
#     print(a, b)
#     # if a exceeds the limit break the loop
#     if(a > limit or KeyboardInterrupt == True):
#         break

#     _sum = a + b

#     # if a + b is even add it to the fibbonacci_sum
#     if (_sum % 2 == 0):
#         fibonacci_sum += _sum
#         print(_sum)

#     # update values
#     a = _sum
#     b = _sum - a # previus sum

# print(limit)