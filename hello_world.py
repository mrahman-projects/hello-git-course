print("Hello World!")
print()

# this is the feature-01
print("This is a new feature added")
numbers = []
for i in range(1,10):
    numbers.append(i)
    print(numbers)

# this is the feature-02
print()
print("This is the second feature added")
company_dict = {"1": "company 01", "2": "company 02", "3": "company 03", "4": "company 04"}
for key, value in company_dict.items():
    print(f"{key}: {value}")

print()

print("this is the third feature added")
while True:
    user_input = input("guess a number, 0 to quit: ")
    if user_input == '0':
        break
    else:
        print(f"your input is: {user_input}")

print("this is the forth feature added")
target_number = int(input("Please select a number: "))
for count in range(1, 11):
    print(f"{target_number} * {count} = {target_number * count}")

print("This is the end of the program")

