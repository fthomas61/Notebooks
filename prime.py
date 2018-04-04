n = int(input("Entrez le nombre dont on veut tester la primalité : "))

isPrime = True
for i in range(2,n):
    if n%i == 0:
        isPrime = False
        break
    else:
        pass

if isPrime:
    print("Congratulations :",n,"is prime !")
else:
    print("Nope.",n,"is not prime. Try again.")
