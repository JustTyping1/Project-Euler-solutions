import math
def isprime(num):
    i=2
    while i <= int(math.floor(math.sqrt(num))):
        if num % i == 0:
            return False
        i+=1
    return True
    
primes = []

k=2
while len(primes) < 10002:
    if isprime(k):
        primes.append(k)
    k += 1

print(primes[10000])
    

