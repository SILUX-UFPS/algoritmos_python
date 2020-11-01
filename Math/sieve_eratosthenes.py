#Después de llamar a sieve(N), el vector primes contiene la lista de primos menores o iguales a N, mientras que isPrime[n] contiene si n es primo. 
def sieve(n):
	primes = []
	isPrime = [1 for i in range(n)]
	isPrime[0] = isPrime[1] = 0

	for i in range(n):
		if isPrime[i]:
			primes.append(i)
			h = 2
			while i*h < n:
				isPrime[i*h] = 0
				h += 1

	return primes, isPrime
