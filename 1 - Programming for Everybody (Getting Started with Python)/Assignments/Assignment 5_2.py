# 5.2 Write a program that repeatedly prompts a user for integer numbers
# until the user enters 'done'. Once 'done' is entered, print out the
# largest and smallest of the numbers. If the user enters anything other
# than a valid number catch it with a try/except and put out an appropriate
# message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the
# output below.

largest = None
smallest = None

while True:
    numInput = input("Enter a number: ")
    if numInput == "done" : break
    else:
        try:
        	num = float(numInput)
        except ValueError:
            print('Invalid input')
    if smallest is None and largest is None:
        smallest = num
        largest = num
    if smallest > num:
        smallest = num
    if largest < num:
        largest = num


print("Maximum is", int(largest))
print("Minimum is", int(smallest))
