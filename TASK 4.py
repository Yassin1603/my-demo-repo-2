# 1. Write a program that checks if a number is prime:
n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number.")
            break
    else:
        print(n, " is a prime number.")
else:
    print(n, "is not a prime number.")
print()
# - Create a function `is_prime(n)` that returns True if `n` is a prime number and False otherwise.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i != 0:
            return True
        else:
            return False

print(is_prime(9))
print()
# - Use this function to print all prime numbers between 1 and 50.
lower = 1
upper = 50

for n in range(lower, upper + 1):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n)
print()
# 2. Create a list of integers from 1 to 15. Iterate through the list and perform the following:
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# - If the number is divisible by 3, print "Fizz".
for i in list:
    if i % 3 == 0:
        print("Fizz")
        continue


# - If the number is divisible by 5, print "Buzz".
    elif i % 5 == 0:
        print("Buzz")
        continue


# - If the number is divisible by both 3 and 5, print "FizzBuzz".
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue

# - Otherwise, print the number itself.
    else:
        print(i)
