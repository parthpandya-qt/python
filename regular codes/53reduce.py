from functools import reduce



ls=[4,5,4,5,4,5]

result = reduce((lambda x, y: x + y), ls)
print(result)


