name=input("Enter your name: ")
print(name)

# -- Mathematics on user input --
size_input = input("How bit is your house (in square feer): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(f"{square_feet} square feet is {square_metres:.2f} square metres.")