print("Please enter a number to create a pyramid")
number = int(input("number:"))
for i in range(number):
    print(" "*(number - i), "*" * (i*2+1))
print("Successfully built a pyramid")