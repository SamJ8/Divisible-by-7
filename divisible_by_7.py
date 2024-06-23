import random
from colorama import Fore

def Random():

    for i in range(0,6):
        random_number = random.randint(1, 30)

        print("\n")

        if random_number % 7 == 0:
            print(Fore.GREEN + f"{random_number} IS divisible by 7")
        else:
            print(Fore.RED + f"{random_number} ISN'T divisble by 7")

Random()