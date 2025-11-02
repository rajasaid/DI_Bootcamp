import random


#Ask for User Input:
#The string must be exactly 10 characters long.
#2. Check the Length of the String:

#If the string is less than 10 characters, print: "String not long enough."
#If the string is more than 10 characters, print: "String too long."
#If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
#3. Print the First and Last Characters:

#Once the string is validated, print the first and last characters.
#4. Build the String Character by Character:

#Using a for loop, construct and print the string character by character. Start with the first character, then the first two characters, and so on, until the entire string is printed.
def string_game():
    user_string = input("Please enter a string that is exactly 10 characters long: ")
    if len(user_string) < 10:
        print("String not long enough.")
        return
    elif len(user_string) > 10:
        print("String too long.")
        return
    else:
        print("Perfect string")
        print(f"First character: {user_string[0]}")
        print(f"Last character: {user_string[-1]}")
        
        constructed_string = ""
        for char in user_string:
            constructed_string += char
            print(constructed_string)

# Bonus: Jumble the String (Optional)
#As a bonus, try shuffling the characters in the string and print the newly jumbled string.

    jumbled_string = ''.join(random.sample(user_string, len(user_string)))
    print(f"Jumbled string: {jumbled_string}")

if __name__ == "__main__":
    string_game()
