def is_int_input():
    while True:
        x = input("Enter a positive integer: ")
        try:
            x = int(x)
            if x > 0:
                return True
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a valid integer!")

result = is_int_input()
print(f"You entered: {result}")
