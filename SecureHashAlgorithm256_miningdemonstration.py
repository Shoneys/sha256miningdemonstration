import random
import time
from hashlib import sha256


# pip install hwcounter

def hashcash():
    """
        In Bitcoin, the hash that needs to be solved is the new head for the block

        x would be the hash of the previous block
        y would be the hash that solves the new block
        the amount of "0's" at the end of the string determines the difficulty of mining
            current difficulty of Bitcoin: https://blockexplorer.com/api/status?q=getDifficulty
        the new hash becomes the

        It's meant to take a predictable amount of time (why it's called Proof of Work)
        Each block solve attempt is a lottery, you can win on the first try, or it can take a million
    """
    timeStart = time.perf_counter()

    # x = 'ad5ecef5a175d612b1fbc6942248b009c2642689sdfgsdfg59ca36b4b874e3279dfa4edf'
    # ↑↑↑↑↑ example of a real hash ↑↑↑↑↑

    # x is hash of previous block
    # y is the nonce, a random number just to hash with. I have made it sequential

    x = random.randint(0, 10000)  # random number is used to simulate the previous block, which would be random
    y = 0  # We don't know what y should be yet
    while sha256(f'{x * y}'.encode()).hexdigest()[-1] != "0" or sha256(f'{x * y}'.encode()).hexdigest()[-2] != "0" or \
            sha256(f'{x * y}'.encode()).hexdigest()[-3] != "0":
        print(sha256(f'{x * y}'.encode()).hexdigest())
        print(y)
        y += 1
    print(f'x was: {x}')
    print(f'The solution is y = {y}')
    print(sha256(f'{x * y}'.encode()).hexdigest())

    print(f'Execution time: {round(time.perf_counter() - timeStart, 5)} seconds')


while __name__ == '__main__':
    hashcash()
    time.sleep(5)
    print('\n')
