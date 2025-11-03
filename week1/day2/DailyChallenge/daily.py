#  Ask the user for two inputs:
# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

def generate_multiples(number, length): 
    multiples = []
    for i in range(1, length + 1):
        multiples.append(number * i)
    return multiples
def main():
    try:
        number = int(input("Enter a number (integer): "))
        length = int(input("Enter the length of the list (integer): "))
        if length < 0:
            print("Length should be a non-negative integer.")
            return
        multiples_list = generate_multiples(number, length)
        print("Generated list of multiples:", multiples_list)
    except ValueError:
        print("Invalid input. Please enter valid integers.")     

# Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.
# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
    try:
        user_string = input("Enter a string: ")
        def remove_consecutive_duplicates(s):
            if not s:
                return s
            result = [s[0]]
            for char in s[1:]:
                if char != result[-1]:
                    result.append(char)
            return ''.join(result)
        processed_string = remove_consecutive_duplicates(user_string)
        print("Processed string (without consecutive duplicates):", processed_string)
    except Exception as e:
        print("An error occurred while processing the string:", str(e))
        


if __name__ == "__main__":
    main()
