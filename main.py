# ========================================================================================================================
# FIZZ BUZZ for loop
    # If a number is divisible by 5, print buzz
    # If a number is divisible by 3, print fizz
    # If a number is divisible by both, print fizzbuzz
    # If none, print num
# for num in range(1,100):
#     if num % 3 == 0 and num % 5 == 0:
#         print("fizzbuzz")
#     if num % 3 == 0:
#         print("fizz")
#     if num % 5 == 0:
#         print("buzz")
#     else:
#         print(num)

# ========================================================================================================================
# FIZZ BUZZ function
    # Params: choice int(input())
    # If a number is divisible by 5, print buzz
    # If a number is divisible by 3, print fizz
    # If a number is divisible by both, print fizzbuzz
    # If none, print num
choice = int(input("What number do you choose?"))
def fizzbuzz(choice):
    for num in range(1, choice):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizzbuzz")
        if num % 3 == 0:
            print("Fizz")
        if num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz(choice)