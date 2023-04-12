import math

def main():
    n = int(input("Enter a number: "))
    primes = get_primes(n)

    combinations = get_combinations(n, primes)

    multiplications = []
    for comb in combinations:
        multiplication = multiply(comb)
        multiplications.append(multiplication)

    largest_product = max(multiplications)
    index_of_largest_product = multiplications.index(largest_product)

    print("\nLargest product:", largest_product)
    print("+".join(str(x) for x in combinations[index_of_largest_product]))
    input()

def multiply(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def get_primes(n):
    primes = []
    is_composite = [False] * (n + 1)

    for i in range(2, n + 1):
        if not is_composite[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_composite[j] = True

    return primes

def get_combinations(n, primes):
    combinations = []
    get_combinations_helper(n, primes, combinations, [], 0)
    return combinations

def get_combinations_helper(n, primes, combinations, current_combination, start_index):
    if n == 0:
        combinations.append(current_combination[:])
        return

    for i in range(start_index, len(primes)):
        if primes[i] <= n:
            current_combination.append(primes[i])
            get_combinations_helper(n - primes[i], primes, combinations, current_combination, i)
            current_combination.pop()
        else:
            break

if __name__ == "__main__":
    main()