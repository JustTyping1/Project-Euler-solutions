import math
def check_factors(num):
    factors = []
    i=2
    while i < int(math.floor(math.sqrt(num))):
        if num % i == 0:
            factors.append(i)
        i+=1
    return factors

for item in check_factors(600851475143):
    if len(check_factors(item)) == 0:
        print(item)

