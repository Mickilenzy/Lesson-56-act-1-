def is_palindrome_number(number):
    return number == number[::-1]
def start_game():
    print(" Welcome to the Number Palindrome Game!")
    print("A palindrome number reads the same forward and backward")

while True:
    number = input(" Enter a number to check (or type 'exit' to quit):")

    if number.lower() == "exit":
        print(" Thanks for playing! Keep having fun with numbers!")
        break

    if not number.isdigit():
        print(" Please enter **numbers only**! No letters or symbols!")
        continue

    if is_palindrome_number(number):
        print(f" Awesome! {number} is a PALIDROME!  \n")

    else:
        print(f" Oops! {number} is NOT a palindrome.Try again!  \n")

# start the game
start_game()            