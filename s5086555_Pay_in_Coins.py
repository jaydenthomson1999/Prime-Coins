<<<<<<< HEAD


if __name__ == "__main__":
    pass
=======
# returns a list of prime numbers lesser or equal to input number 
def get_prime(number: int) -> list():
    non_primes = set(j for i in range(2, 8) for j in range(i*2, number, i))
    primes = [x for x in range(1,number) if x not in non_primes]
    return primes

def get_coins(total, coins):
    if total == 1:
        return [1]

    coin_superset = []

    for coin in coins:
        coin_subset = []
        new_total = total - coin
        
        if new_total == 0:
            coin_subset.append([coin])
        else:
            pass

        coin_superset.append(coin_subset)
    return coin_superset

if __name__ == "__main__":
    total = 5
    coins = get_prime(total)
    maxi = -1
    mini = -1

>>>>>>> ead58c186b1e64ef41198fbb4e0697ede7791f84
