
def special_prime(number):
    special_number = (number ** 2) + 2
    if special_number <= 3:
        return True
    if special_number > 3:
        for i in range(3, special_number + 1, 2):
            if special_number % i == 0 and i != special_number:
                return False
    return True

def main():
    for i in range(1,101):
        if special_prime(i) and i % 3 == 0:
            print("FizzBuzz")
        elif special_prime(i):
            print("Fizz")
        elif i % 3 == 0:
            print("Buzz")
        else:
            print(i)

main()
