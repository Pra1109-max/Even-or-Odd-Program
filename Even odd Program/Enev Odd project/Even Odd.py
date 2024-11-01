def even_odd(number):
 
# This function is the formula for the checking that the number is even or odd
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

# This variable(num) will take the number from the user to give results
num = int(input("Enter a number to find that the number is Even or odd:-\n "))

# This variable(results) will call this function and print the result in terminal
result = even_odd(num)
print(f"The {num} is {result}")
 

# Please Like and Subscribe my video for more interesting or amazing video
