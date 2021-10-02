"""
Exercise: genPrimes
5/5 Points

Write a generator, genPrimes, that returns the sequence of prime numbers on
successive calls to its next() method: 2, 3, 5, 7, 11, ...
"""
def genPrimes():
    primes = [2]
    guess = 3

    yield primes[-1]
    while True:
        if all(guess % p != 0 for p in primes):
            primes.append(guess)
            yield primes[-1]
        guess += 2
