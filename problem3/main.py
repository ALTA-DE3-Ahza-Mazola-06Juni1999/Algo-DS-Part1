def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        first,second = 0,1
        for i in range(2, number + 1):
            next_number = first + second
            first = second
            second = next_number
        return second

if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10)) # 55
    print(fibonacci(12)) # 144