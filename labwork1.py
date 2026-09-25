#EX1:
r = float(input("Enter circle radius? "))
area = 3.14 * (r ** 2)
print(f"Circle area = {area}") 

#EX2:
c = float(input("Enter the temperature in Celsius? "))
f = (c * 9 / 5) + 32
print(f"{c} (C) = {f} (F)")

#EX3:
n = int(input("Enter a number? "))

if n < 2:
    print(f"{n} is a NOT prime number")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is a NOT prime number")

#EX4:
n = int(input("Enter a number? "))

if n > 1 and sum(i for i in range(1, n) if n % i == 0) == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is a NOT perfect number")

#EX5:
colors = ["Blue", "Yellow", "Black", "Red", "White"]
fav = input("What is your favorite color? ")

if fav in colors:
    print(f"Your color is at index {colors.index(fav)} in my list")
else:
    print("Sorry, I could not find your color")

#EX6:
range1 = list(range(7))
range2 = list(range(1, 11, 3))
range3 = list(range(5, 0, -1))
range4 = list(range(6, -3, -2))

print("range1:", range1)
print("range2:", range2)
print("range3:", range3)
print("range4:", range4)

#EX7:
def remove_dollar_sign(s):
    return s.replace("$", "")

#EX8:
def extract_even(l):
    return [x for x in l if x % 2 == 0]

#EX9:
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#EX10:
def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

#EX11:
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance: {distance}")

#EX12:
def print_pattern(m, n):
    for _ in range(m):
        print("* " * n)