palindromes = []
productpalindromes = []
i = 10
k=100
while 10<=i<=99:
    for j in range(10):
        palindromes.append(
            int(
                str(i) + str(j) + str(i)[::-1]
            )
        )
    i+=1
while 100<=k<=999:
    
    palindromes.append(
        int(
            str(k) + str(k)[::-1]
        )
    )
    k+=1


for palindrome in palindromes:
    a = 100
    while 100 <= a <= 999:
        if palindrome % a == 0:
            if len(str(int(palindrome/a))) == 3:
                print(palindrome)
                print((a, (int(palindrome/a))))
        a+=1 
