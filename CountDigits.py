
# Taking input from the user.
n=int(input("Enter number:"))

# Initializing a variable 'count'.
count=0

# Using while loop.
while(n>0):
    count=count+1
    n=n//10
    
print("The number of digits in the number are:",count)
