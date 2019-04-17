# returns a list of prime numbers lesser or equal to input number 
def get_prime(number: int) -> list():
    non_primes = set(j for i in range(2, 8) for j in range(i*2, number, i))
    primes = [x for x in range(1,number+1) if x not in non_primes]
    return primes

def get_coins(total, coins):
    if total == 1:
        return [[1]]

    coin_superset = []

    for coin in coins:
        coin_subset = []
        new_total = total - coin
        
        if new_total == 0:
            coin_subset.extend([coin])
        else:
            new_coins = list(coins)

            while(new_coins[-1] > new_total):
                new_coins.pop()

            temp_set = get_coins(new_total, new_coins)

            for temp in temp_set:
                temp.extend([coin])

            coin_subset.extend(temp)

        coin_superset.append(coin_subset)
    return coin_superset

if __name__ == "__main__":
    total = 10
    coins = get_prime(total)
    maxi = -1
    mini = -1

    print(get_coins(total, coins))
