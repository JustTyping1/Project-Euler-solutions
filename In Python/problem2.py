fibonacci_numbers = [1, 1]
counter = 0
while fibonacci_numbers[len(fibonacci_numbers)-1]<=4000000:
    fibonacci_numbers.append(fibonacci_numbers[len(fibonacci_numbers)-1] + fibonacci_numbers[len(fibonacci_numbers)-2])
    if fibonacci_numbers[len(fibonacci_numbers)-1] % 2 == 0:
        counter += fibonacci_numbers[len(fibonacci_numbers)-1]

print(counter)
print(fibonacci_numbers)



