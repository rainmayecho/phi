import time

''' To use this program from terminal,
    go to the directory in which this
    file is saved and start an interactive
    Python session. Type 'import eulerphi'
    and all of the following functions can
    be used. Read this file for the inputs
    required for each function. '''

## Computes the greatest common divisor
## of two integers using the Euclidean algorithm.
def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)

## Generates a list of prime numbers 2<= p_k <= n.
def sieve(n):
    sieve = range(n+1)
    sieve[1] = 0
    for i in xrange(2, int(n**.5)+1):
        if sieve[i]:
           m = n/i - i
           sieve[i*i: n+1:i] = [0] * (m + 1)
    return [x for x in sieve if x]

## Finds the prime factorization of n
## Using an appropriately passed list of primes.
## Primes should be a list of primes at least up to the sqrt of n.
## Reduces all multiplicities greater than 1 to 1.
def pfactorize(n, primes):
    if n in [0, 1]:
        return []
    if n in primes:
        return [n]

    R = []
    for p in primes:
        temp = n
        if n in primes:
            R.append(n)
            return R
        while not n % p:
            n /= p
        if not temp == n:
            R.append(p)
        if n == 1:
            break
    if not n == 1:
        R.append(n)
    return R
            

## Calculates how many numbers
## less than n are coprime with n
## using the Euclidean gcd algorithm.
def gcd_phi(n):
    r = 1
    for x in xrange(2, n):
        if gcd(x,n) == 1:
            r += 1
    return r

## A slight optimization
def phi_2(n):
    r = 1
    if not n % 2:
        for x in xrange(3, n, 2):
            if gcd(x,n) == 1:
                r += 1
    else:
        for x in xrange(2, n):
            if gcd(x,n) == 1:
                r += 1
    return r

## Calculates phi
## using the prime factorization of n.
def phi_fact(n, primes):
    pfactors = pfactorize(n, primes)
    r = n
    for p in pfactors:
        r *= (1-1./p)
    return int(r)
        
## Sieving for phi values for 0 <= k <= n.
def sieve_phi(n):
    R = range(n+1)
    for i in xrange(2, n+1):
        if R[i] == i:
            R[i::i] = (x*(i-1)/i for x in R[i::i])
    return R

''' Note that time.clock()'s results
    will vary based on processor usage.'''
def time_gcd_phi(n):
    t = time.clock()
    print gcd_phi(n)
    print str(time.clock()-t)+' seconds'

def time_phi_fact(n):
    t = time.clock()
    primes = sieve(int(n**.5))
    print phi_fact(n, primes)
    print str(time.clock()-t)+' seconds'
    
def time_phi_fact2(n, primes):
    t = time.clock()
    print phi_fact(n, primes)
    print str(time.clock()-t)+' seconds'    
    
##
