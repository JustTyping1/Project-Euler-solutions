sum = 0
sumofsquares = 0
for i in range(101):
    sumofsquares += i*i
    sum += i
print(sum*sum - sumofsquares)
