from itertools import product
from time import perf_counter
import sys

pas = input("Enter the password: ")

keys = "1234567890abcdefghijklmnopqrstuvwxyz"

start = perf_counter()
attempts = 0

for length in range(1, len(pas) + 1):
    for combination in product(keys, repeat=length):
        attempts += 1
        guess = ''.join(combination)

        # Animation: update terminal every 5000 attempts
        if attempts % 5000 == 0:
            sys.stdout.write(f"\rAttacking... Trying: {guess}")
            sys.stdout.flush()

        if guess == pas:
            end = perf_counter()
            print(f"\n\nPassword found: {guess}")
            print(f"Attempts: {attempts}")
            print(f"Time taken: {end - start:.6f} seconds")
            raise SystemExit