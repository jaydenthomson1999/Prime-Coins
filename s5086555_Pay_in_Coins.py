import time
from collections import deque
from sys import argv

''' class stores nodes in the search tree and can determine if its invalid or a 
    goal and can geneate the nodes children in the search tree  '''
class Node:
    def __init__(self, coins_used:list, total:int):
        self.coins_used = coins_used
        self.total = total
    
    # is a goal if node has total equal to 0
    def is_goal(self) -> bool:
        if self.total == 0:
            return True
        else:
            return False

    # is invalid if node has coin list greater than maximum or if total = 0 
    # and has coin list lesser than minimum
    def is_invalid(self, mini: int, maxi: int) -> bool:
        if len(self.coins_used) > maxi:
            return True
        if self.total == 0 and (len(self.coins_used) < mini):
            return True
        return False

    # generates children based on the which coins it can use in the coin list
    # and prunes out invalid children
    def generate_children(self, coins: list, mini: int, maxi: int) -> list:
        children = []
        for coin in coins:
            if coin <= self.total and coin <= self.coins_used[-1]:
                new_coins_used = list(self.coins_used)
                new_coins_used.append(coin)
                new_total = self.total - coin
                child = Node(new_coins_used, new_total)

                if not child.is_invalid(mini, maxi):
                    children.append(child)
                else:
                    del child
        return children

''' returns a list of prime numbers lesser or equal to input number '''
def get_prime(number: int) -> list():
    non_primes = set(j for i in range(2, number) for j in range(i*2, number, i))

    primes = []
    for i in range(1, number+1):
        if i not in non_primes:
            primes.append(i)

    return primes

''' returns the initial list of coins that initialises the stack'''
def initial_coins(total: int, coins: list, mini: int, maxi: int) -> list:
    init_list = []

    for coin in coins:
        new_total = total - coin
        init_item = Node([coin], new_total)

        if not init_item.is_invalid(mini, maxi):
            init_list.append(init_item)
        else:
            del init_item
    
    return init_list

''' returns the amount of permutations that an amount of money can be payed for 
    only using prime numbers '''
def pay_in_coins(total: int, mini: int, maxi: int) -> int:
    goals = 0
    
    # init main lists
    coins = get_prime(total)

    # initialised stack with prime coins
    init_states = initial_coins(total, coins, mini, maxi)
    stack = deque(init_states)
    
    # depth first search until stack is empty
    while len(stack) != 0:
        # element from top of stack
        node = stack.pop()

        # node has coin list greater than minimum and sum equals grand total
        if node.is_goal():
            goals += 1

        # explore children branches and add them to stack
        else:
            children = node.generate_children(coins, mini, maxi)
            stack.extend(children)  

        del node          

    return goals

if __name__ == "__main__":
    path = argv[1]
    file = open(path, 'r')
    inputs = file.read().splitlines()
    file.close()

    file = open("Output.txt", 'w')

    # run algorithm for each line in the text file - path
    for line in inputs:
        # get args from line
        args = line.split()

        # only has the total, no min or max restrictions
        if len(args) == 1:
            total = int(args[0])
            mini = 1
            maxi = total
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
        file.write(str(sols) + '\n')
    
    file.close()
