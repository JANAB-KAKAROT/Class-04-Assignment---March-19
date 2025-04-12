# Function to check if number is positive, negative, or zero
def check_status(number):
    """This check if number is positive, negative, or zero."""
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Function to say hello in Karachi
def say_hello(name="Kako"):
    """This say hello to name."""
    print(f"Hello {name} from Karachi! How are you?")
    print("Vendor: Ganne ka Juice 20 Rupay Glass 😋")  # Vendor shouting!

# Function to get square of number
def get_square(num):
    """This get square of number."""
    return num * num

# Function to print fruit names in Urdu
def show_fruits():
    """This show list of fruits in Urdu."""
    fruits_in_urdu = ["Anaar", "Angoor", "Narangi", "Tarbooz"]
    print("Fruits in Urdu:")
    for fruit in fruits_in_urdu:
        print(fruit)

# Function to count down from number
def countdown(start=5):
    """This count down from start number."""
    count = start
    while count > 0:
        print(count)
        count -= 1
    print("Countdown finish!")

# Main code that use all functions

# Check number status (positive, negative, zero)
number = -3
status = check_status(number)
print(f"Number {number} is {status}.\n")

# Say hello in Karachi with default name
say_hello()  # Default is "Kako"
say_hello("Sadaf")  # With name "Sadaf"

# Get square of a number
number_to_square = 4
square_value = get_square(number_to_square)
print(f"Square of {number_to_square} is: {square_value}\n")

# Show fruits in Urdu
show_fruits()

# Countdown from 5
countdown()

# Check multiple numbers with status
numbers = [1, -1, 0, 5, -10]
print("\nCheck status for more numbers:")
for num in numbers:
    print(f"Number {num} is {check_status(num)}.")
