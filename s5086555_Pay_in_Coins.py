from collections import deque
from time import time
from sys import argv

# class node stores a node in the search tree
class Node:
    def __init__(self, coins_used, total, remaining_coins):
        self.coins_used = coins_used
        self.total = total
        self.remaining_coins = remaining_coins
    
    def is_goal(self, mini):
        if self.total == 0 and (mini == None or len(self.coins_used) >= mini):
            return True
        else:
            return False
    
    def is_invalid(self, maxi):
        if maxi != None and len(self.coins_used) > maxi:
            return True
        else:
            return False
    
    def generate_children(self):
        children = []
        for coin in self.remaining_coins:
            new_coins_used = list(self.coins_used)
            new_coins_used.append(coin)
            new_total = self.total - coin

            if new_total == 0:
                new_coins_remaining = []
            else:
                new_coins_remaining = list(self.remaining_coins)
                
                while ((new_coins_remaining[-1] > coin) or 
                        (new_coins_remaining[-1] > new_total)):
                    new_coins_remaining.pop()

            children.append(Node(new_coins_used, new_total, 
                            new_coins_remaining))
        return children
    

# returns a list of prime numbers lesser or equal to input number 
def get_prime(number: int) -> list():
    non_primes = set(j for i in range(2, 8) for j in range(i*2, number, i))

    primes = []
    for i in range(1, number+1):
        if i not in non_primes:
            primes.append(i)

    return primes

def initial_coins(total, coins):
    init_list = []

    for coin in coins:
        new_total = total - coin

        if new_total == 0:
            new_coins = []
        else:
            new_coins = list(coins)
            while new_coins[-1] > coin or new_coins[-1] > new_total:
                new_coins.pop()
        
        init_list.append(Node([coin], new_total, new_coins))
    
    return init_list
    
if __name__ == "__main__":
    # get input from console
    if len(argv) == 2:
        total = int(argv[1])
        mini = None
        maxi = None

    elif len(argv) == 3:
        total = int(argv[1])
        mini = int(argv[2])
        maxi = mini
        
    elif len(argv) == 4:
        total = int(argv[1])
        mini = int(argv[2])
        maxi = int(argv[3])

    start = time()

    coins = get_prime(total)
    stack = deque()
    goals = []

    # initialised stack with prime coins
    init_states = initial_coins(total, coins)
    stack.extend(init_states)
    
    while len(stack) != 0:
        node = stack.pop()

        if node.is_invalid(maxi):
            continue

        elif node.is_goal(mini):
            goals.append(node)

        else:
            children = node.generate_children()
            stack.extend(children)

    # pritning time, num of solutions and solutions            
    end = time()
    print("time: {}".format(end-start))
    print("solutions: {}".format(len(goals)))           