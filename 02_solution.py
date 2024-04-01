def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def first_N_alternate_primes(N):
    count = 0
    num = 2
    while count < N:
        if is_prime(num):
            count += 1
            if count % 2 == 1:
                print(num, end=" ")
        num += 1

N = int(input())

first_N_alternate_primes(N)
