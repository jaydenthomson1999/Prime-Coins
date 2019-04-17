# returns a list of prime numbers lesser or equal to input number 
def get_prime(number: int) -> list():
    non_primes = set(j for i in range(2, 8) for j in range(i*2, number, i))
    primes = [x for x in range(1,number+1) if x not in non_primes]
    return primes

if __name__ == "__main__":
    pass
