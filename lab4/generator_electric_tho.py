# 1. Create a generator that generates the squares of numbers up to some number `N`.
def squares_up_to(N):
    for i in range(1, N+1):
        yield i**2
for square in squares_up_to(12):
    print(square)
# 2. Write a program using generator to print the even numbers between 0 and `n` in comma separated form where `n` is
# input from console.
def even_numbers_up_to(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input("Enter a number: "))
even_nums = even_numbers_up_to(n)
print(','.join(map(str, even_nums)))
# 3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4,
# between a given range 0 and `n`.
def divisible_by_three_and_four(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for num in divisible_by_three_and_four(100):
    print(num)
# 4. Implement a generator called `squares` to yield the square of all numbers from (a) to (b). Test it with a "for"
# loop and print each of the yielded values
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
for num in squares(5,7):
    print(num)
# 5. Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
for r in countdown(10):
    print(r)