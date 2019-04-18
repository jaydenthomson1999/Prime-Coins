from collections import deque
import time
from sys import argv

''' class stores nodes in the search tree and can determine if its invalid or a 
    goal and can geneate the nodes children in the search tree  '''
class Node:
    def __init__(self, coins_used:list, total:int, remaining_coins: list):
        self.coins_used = coins_used
        self.total = total
        self.remaining_coins = remaining_coins
    
    # is a goal if node has total equal to 0 and its coin list is >= mini
    def is_goal(self, mini: int) -> bool:
        if self.total == 0 and (mini == None or len(self.coins_used) >= mini):
            return True
        else:
            return False

    # is invalid if node has coin list greater than maximum
    def is_invalid(self, mini: int, maxi: int) -> bool:
        if maxi != None and len(self.coins_used) > maxi:
            return True
        if self.total == 0 and (mini != None and len(self.coins_used) < mini):
            return True
        else:
            return False

    # generates children based on the remaining coins the node can use
    def generate_children(self) -> list:
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

''' returns a list of prime numbers lesser or equal to input number by 
    generating a list of non prime numbers and iterates through 1 to number 
    (inclusive) and checks if it is in the non prime numbers list, if not than 
    it is a prime number, add to primes list '''
def get_prime(number: int) -> list():
    non_primes = set(j for i in range(2, 8) for j in range(i*2, number, i))

    primes = []
    for i in range(1, number+1):
        if i not in non_primes:
            primes.append(i)

    return primes

''' returns the initial list of coins that initialises the stack'''
def initial_coins(total: int, coins: list) -> list:
    init_list = []

    for coin in coins:
        new_total = total - coin
        
        # when total = 0 we have found a solution so we don't need new coins
        if new_total == 0:
            new_coins = []
        else:
            # prunes coins that are greater than the coin added or the new total
            new_coins = list(coins)
            while new_coins[-1] > coin or new_coins[-1] > new_total:
                new_coins.pop()
        
        init_list.append(Node([coin], new_total, new_coins))
    
    return init_list

''' returns the amount of permutations that an amount of money can be payed for 
    only using prime numbers '''
def pay_in_coins(total: int, mini: int, maxi: int) -> int:
    # init main lists
    coins = get_prime(total)
    goals = []

    # initialised stack with prime coins
    init_states = initial_coins(total, coins)
    stack = deque(init_states)
    
    # depth first search until stack is empty
    while len(stack) != 0:
        # element from top of stack
        node = stack.pop()

        # node has coin list which has gone over maximum
        if node.is_invalid(mini,maxi):
            del node
        
        # node has coin list greater than minimum and sum equals grand total
        elif node.is_goal(mini):
            goals.append(node)

        # explore children branches and add them to stack
        else:
            children = node.generate_children()
            stack.extend(children)
            

    return len(goals)

if __name__ == "__main__":
    path = argv[1]
    file = open(path)
    inputs = file.read().splitlines()
    file.close()

    # run algorithm for each line in the text file - path
    for line in inputs:
        # get args from line
        args = line.split()

        # only has the total, no min or max restrictions
        if len(args) == 1:
            total = int(args[0])
            mini = None
            maxi = None
        # only has minimum restriction, logically max = min
        elif len(args) == 2:
            total = int(args[0])
            mini = int(args[1])
            maxi = mini
        # all three inputs total, min and max    
        elif len(args) == 3:
            total = int(args[0])
            mini = int(args[1])
            maxi = int(args[2])
        
        sols = pay_in_coins(total, mini, maxi)
        timer = time.process_time()
        print("{} : {} seconds".format(sols,timer))
