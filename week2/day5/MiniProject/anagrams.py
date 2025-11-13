import anagram_checker

#Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

#It should do the following:
#Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

#If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
#Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
#Only alphabetic characters are allowed. No numbers or special characters.
#Whitespace should be removed from the start and end of the user’s input.

#Once your code has decided that the user’s input is valid, it should find out the following:
#All possible anagrams to the user’s word.
#Create an AnagramChecker instance and apply it to the steps created above.
#Display the information about the word in a user-friendly, nicely-formatted message such as:

FILE_PATH = "./sowpods.txt"

def check_number_of_words(input_string):
    words = input_string.strip().split()
    return len(words) == 1

def main():
    anagram_checker_obj = anagram_checker.AnagramChecker(FILE_PATH)
    print(anagram_checker_obj.words)

    while True:
        user_input = input("Enter a word to find its anagrams (or type 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        if not user_input.isalpha():
            print("Invalid input. Please enter a valid word containing only alphabetic characters.")
            continue
        if not check_number_of_words(user_input):
            print("Please enter exactly one word.")
            continue
        if not anagram_checker_obj.is_valid_word(user_input):
            print(f"'{user_input}' is not a valid word in the word list. Please try again.")
            continue
        print("This is a valid English word.")    
        anagrams = anagram_checker_obj.get_anagrams(user_input.lower())
        if anagrams:
            print(f"Anagrams for your word '{user_input}': {', '.join(anagrams)}")
        else:
            print(f"No anagrams found for '{user_input}'.")

if __name__ == "__main__":
    main()
