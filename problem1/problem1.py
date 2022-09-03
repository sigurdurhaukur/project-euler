limit = 1000
multiples = []
# listing all the natural numbers, n that are multiples of 3 or 5
for n in range(1, limit):
    # check if n is a multiple of 3
    if(n % 3 == 0 and n% 5 == 0):
        multiples.append(n)
    elif(n % 3 == 0):
        multiples.append(n)
    elif(n % 5 == 0):
        multiples.append(n)


# calculate the sum of the multiples
sum = sum(multiples)
print('solution:', sum)