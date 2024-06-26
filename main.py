# que:1
length_of_rectangle = 5
width_of_rectangle = 3

area_of_rectangle = length_of_rectangle*width_of_rectangle
print[f"area of rectangle = {area_of_rectangle}"]

# ----------------------------------------------------------------------------------

# que:2
a = int(input("Enter Number : 7"))
b = a % 2

if b == 0 :
    print(f"{a} is Even")

else:
    print(f"{a} is Odd")

# ------------------------------------------------------------------------------

# que:3
original_string = "Hello"
reversed_string = original_string[:-1]
print(reversed_string)

 # -------------------------------------------------------------------------------

#  queL:4
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# factorial 5
result = factorial(5)

print(result)

# ---------------------------------------------------------------------------------

# que:5
def pelindroem(s):
   a = "radar"
   b = a[::-1]

if a == b :
    print(f"{a} is a palindrome")

else:
    print(f"{a} is not a palindrome") 

    # -----------------------------------------------------------------------------

# que:7
def largest_number(num1, num2,num3):
    return largest_number

num = "10 25 5"

num2 = num.split(" ")

a = int(num2[0])
b = int(num2[1])
c = int(num2[2])

d = max(a,b,c)

print = {f"the largest in : {d}"}

# ----------------------------------------------------------------------------------

# que:8
def calculate_simple_interest(p, r, t):
    return simple_interest

principal_amount = 1000
rate_of_interest = 5
time_period_in_year = 2
 
# calculate the simple interest
simple_interest = (principal_amount * rate_of_interest * time_period_in_year) / 100

print(f"Simple Interest : {simple_interest}")

# -------------------------------------------------------------------------------------

# que:9
celsius = 37

fahrenheit = ( celsius * 9 / 5 ) + 32

print(f"Temperature in Fahrenheit : {fahrenheit}")

# -------------------------------------------------------------------------------------

# que:10
year = 2020

if (year):
    print(f"{year}is a leap year")

else:
    print(f"{year}is not a leap year")

# ------------------------------------------------------------------------------------

# que:11
def number_of_median(a, b, c):
    number = [10, 5, 20]   
    number.sort()

median = len(number) // 2

print(numbers[median])

# -------------------------------------------------------------------------------------

# que:12
sentence = "the quick brown fox jumps over the lazy dog"

split_sentence = sentence.split(" ")

print(len[split_sentence])

# -------------------------------------------------------------------------------------

# que:13
def sum_of_digits(numbers):
    number = "12345"

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])
e = int(numbers[4])
print(a + b + c + d + e)

