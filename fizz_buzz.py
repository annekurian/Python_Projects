def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return str(input)


while True:
    user_input = input("Enter a number: ")
    if user_input.lower() == "exit":
        break
    if not user_input.isdigit():
        print("Please enter a valid number or type 'exit' to quit.")
        continue
    print(fizz_buzz(int(user_input)))
