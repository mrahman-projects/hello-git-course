print("Hello World!")
print()

print("This is a new feature added")
numbers = []
for i in range(1,10):
    numbers.append(i)
    print(numbers)

print()

print("this is the third feature added")
while True:
    user_input = input("guess a number, 0 to quit: ")
    if user_input == '0':
        break
    else:
        print(f"your input is: {user_input}")


print("This is the end of the program")

