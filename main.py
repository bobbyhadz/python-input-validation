# Validating user input in Python

# ✅ Validating integer user input

num = 0

while True:
    try:
        num = int(input("Enter an integer 1-10: "))
    except ValueError:
        print("Please enter a valid integer 1-10")
        continue
    if num >= 1 and num <= 10:
        print(f'You entered: {num}')
        break
    else:
        print('The integer must be in the range 1-10')

# ----------------------------------------------

# ✅ Validating string user input


password = ''

while True:
    password = input('Enter your password: ')

    if len(password) < 5:
        print('Password too short')
        continue
    else:
        print(f'You entered {password}')
        break

print(password)