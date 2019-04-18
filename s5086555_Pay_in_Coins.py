from collections import deque
from time import time

# returns a list of prime numbers lesser or equal to input number 
def get_prime(number: int) -> list():
    non_primes = set(j for i in range(2, 8) for j in range(i*2, number, i))
    primes = []
    for i in range(1, number+1):
        if i not in non_primes:
            primes.append(i)

    return primes

class Node:
    def __init__(self, coins_used, total, remaining_coins):
        self.coins_used = coins_used
        self.total = total
        self.remaining_coins = remaining_coins
    
    def isGoal(self):
        if self.total == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    start = time()
    total = 5
    coins = get_prime(total)
    stack = deque()
    goals = []

    for coin in coins:
        new_total = total - coin

        if new_total == 0:
            new_coins = []
        else:
            new_coins = list(coins)

            while new_coins[-1] > coin or new_coins[-1] > new_total:
                new_coins.pop()
        
        stack.append(Node([coin], new_total, new_coins))
    
    while len(stack) != 0:
        node = stack.pop()

        if node.isGoal():
            goals.append(node)

        else:
            for coin in node.remaining_coins:
                new_coins_used = list(node.coins_used)
                new_coins_used.append(coin)

                new_total = node.total - coin

                if new_total == 0:
                    new_coins = []
                else:
                    new_coins = list(node.remaining_coins)

                    while new_coins[-1] > coin or new_coins[-1] > new_total:
                        new_coins.pop()
                
                stack.append(Node(new_coins_used, new_total, new_coins))
    end = time()
    print("time: {}".format(end-start))
    print("solutions: {}".format(len(goals)))
    while len(goals) != 0:
        node = goals.pop()
        print(node.coins_used)
                
                