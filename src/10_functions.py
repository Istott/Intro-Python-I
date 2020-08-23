# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(n):
    if  n % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
n = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

# print(is_even(n))


if is_even(n) == True:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")


