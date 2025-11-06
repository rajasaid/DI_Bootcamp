# Write a Python program that takes a single string of words as input, where the words are separated by commas (e.g., ‘apple,banana,cherry’). The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.
# Step 1: Get Input
#
#Use the input() function to get a string of words from the user.
#The words will be separated by commas.
#Step 2: Split the String
#Step 3: Sort the List
#Step 4: Join the Sorted List
#Step 5: Print the Result
#Print the resulting comma-separated string.
def sort_words(input_string):
    # Step 2: Split the String
    words_list = input_string.split(',')
    
    # Step 3: Sort the List
    sorted_words = sorted(words_list)
    
    # Step 4: Join the Sorted List
    result_string = ','.join(sorted_words)
    
    return result_string

    # Step 1: Get Input
user_input = input("Enter a string of words separated by commas: ").lower()
    
    # Get the sorted result
sorted_result = sort_words(user_input)
    
    # Step 5: Print the Result
print("Sorted words:", sorted_result)

# Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.
#Step 1: Define the Function
#Define a function that takes a string (the sentence) as a parameter.
#Step 2: Split the Sentence into Words
#Step 3: Initialize Variables
#Step 4: Iterate Through the Words
#Step 5: Compare Word Lengths
#Step 6: Return the Longest Word

def find_longest_word(sentence):
    # Step 2: Split the Sentence into Words
    words = sentence.split()
    
    # Step 3: Initialize Variables
    longest_word = ""
    
    # Step 4: Iterate Through the Words
    for word in words:
        # Step 5: Compare Word Lengths
        if len(word) > len(longest_word):
            longest_word = word
            
    # Step 6: Return the Longest Word
    return longest_word
# Example usage:
input_sentence = "Forgetfulness is by all means powerless!."
longest = find_longest_word(input_sentence)
print("The longest word is:", longest)
