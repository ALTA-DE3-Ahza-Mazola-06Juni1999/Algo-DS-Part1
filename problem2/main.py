def primeX(x):
    prime_count = 0
    number = 2
    while True:
        is_prime = True
        for i in range( 2, int(number ** 0.5)+1 ):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_count += 1
            if prime_count == x:
                return number 
        number += 1

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29