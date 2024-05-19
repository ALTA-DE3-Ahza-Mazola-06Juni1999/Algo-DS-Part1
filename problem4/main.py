def generate_primes_grid(width, height, start):
    result = [[0] * width for _ in range(height)]
    num = start + 1
    prime_found = 0
    
    while prime_found < width * height:
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                row = prime_found // width
                coloum = prime_found % width
                if row < height and coloum < width:
                    result[row][coloum] = num
                prime_found += 1
        num += 1
    return "\n".join(" ".join(map(str, row)) for row in result) + "\n"

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """