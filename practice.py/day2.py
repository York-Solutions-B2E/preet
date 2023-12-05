rnge = range(1,10000)
def getprimes(rnge):
    primes = []
    n=1
    while n < max(rnge) + 1:
        isPrime = True
        for i in range(2,n):
            if n % i  == 0 and n!= 1 :
                isPrime = False
                break
        if isPrime:
                primes.append(n)
        n +=1
    return primes

print(getprimes(rnge))

 










    