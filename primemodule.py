
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

def print_primes(n):
    global prime
    prime = []
    for v in range(2, n):
        if is_prime(v):
            print(v, end= " ")
            prime.append(v)

def get_primes(n):
    print(f"\n{prime}")