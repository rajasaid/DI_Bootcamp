import random

# Create a function that displays a message about what you’re learning.
# Define a function named display_message().
# This function should not take any parameters.
# For example: “I am learning about functions in Python.”
def display_message():
    print("I am learning about functions in Python.")

# Call the function to see the message
display_message()

# Create a function that displays a message about a favorite book.
# Define a function named favorite_book().
# This function should accept one parameter called title.
# The function needs to output a message like “One of my favorite books is <title>”.
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
# Call the function with a book title
favorite_book("Alice in Wonderland")

# Create a function that describes a city and its country.
# Define a function named describe_city().
# This function should accept two parameters: city and country.
# Give the country parameter a default value, such as “Unknown”.
# Inside the function, set up the code to display a sentence like “ is in “.
# Replace <city> and <country> with the parameter values.
#Call the describe_city() function with different city and country combinations.
# Try calling it with and without providing the country argument to see the default value in action.
# Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")
# Call the function with different combinations
describe_city("Reykjavik", "Iceland")
describe_city("Paris")

# Create a function that generates random numbers and compares them.
# Create a function that accepts a number between 1 and 100 as a parameter
# Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.
# If they are the same, print a success message. Otherwise, print a fail message and display both numbers.
# Call the function with a number between 1 and 100.
def compare_random_number(user_number):
    if user_number < 1 or user_number > 100: 
        print("Please provide a number between 1 and 100.")
        return
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Success! You guessed the correct number.")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")
# Call the function with a number
compare_random_number(42)

# Create a function to describe a shirt’s size and message, with default values.
# Define a function called make_shirt().
# This function should accept two parameters: size and text.
# Set up the function to display a sentence summarizing the shirt’s size and message.
# call the function then Modify the make_shirt() function so that size has a default value of “large” and text has a default value of “I love Python”.
# Call make_shirt() to make a large shirt with the default message.
# Call make_shirt() to make a medium shirt with the default message.
# Call make_shirt() to make a shirt of any size with a different message.
# bonus - Call make_shirt() using keyword arguments (e.g., make_shirt(size="small", text="Hello!")).
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is: '{text}'")
# Call the function with different scenarios
make_shirt()
make_shirt(size="medium")
shirt_desc = {"small": "I'm small shirt", "medium": "I'm medium shirt", "large": "I'm large shirt"}
size,text = random.choice(list(shirt_desc.items()))
make_shirt(size=size, text=text)
make_shirt(size="small", text="Hello!") 

# Modify a list of magician names and display them in different ways.
# Create a list called magician_names with the given names:
# ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Create a function called show_magicians() that takes the magician_names list as a parameter.
# Inside the function, iterate through the list and print each magician’s name.
# Create a function called make_great() that takes the magician_names list as a parameter.
# Inside the function, use a for loop to iterate through the list and add “the Great” before each magician’s name.
# Call make_great() to modify the list.
# Call show_magicians() to display the modified list.
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]
make_great(magician_names)
show_magicians(magician_names)

# Generate a random temperature and provide advice based on the temperature range.
# Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.
# Create a function called main(). Inside this function:
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.”
# Inside main(), provide advice based on the temperature:
# Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
# Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
# Between 16°C and 23°C: e.g., “Nice weather.”
# Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
# Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”
def get_random_temp():
    return random.randint(-10, 40)
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 < temp <= 23:
        print("Nice weather.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    else:  # temp > 32
        print("It’s really hot! Stay cool.")
# Call the main function to execute the program
main()

# Bonus - Modify get_random_temp() to return a random floating-point number using random.uniform() for more accurate temperature values.
def get_random_temp():
    return round(random.uniform(-10, 40), 2)
# Call main() again to see the effect of the change
main()
# bonus - Instead of directly generating a random temperature, ask the user for a month (1-12) and determine the season using if/elif conditions.
# Modify get_random_temp() to return temperatures specific to each season.
def get_random_temp():
    month = int(input("Enter the month (1-12): "))
    if month in [12, 1, 2]:  # Winter
        return round(random.uniform(-10, 5), 2)
    elif month in [3, 4, 5]:  # Spring
        return round(random.uniform(5, 15), 2)
    elif month in [6, 7, 8]:  # Summer
        return round(random.uniform(15, 30), 2)
    else:  # Autumn
        return round(random.uniform(10, 20), 2)
# Call main() again to see the effect of the seasonal temperature change
main()
