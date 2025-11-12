import random 
import json

FILE_NAME = "./words.txt"

# Goal: Create a program that generates a random sentence of a specified length from a word list.
# Download the provided word list and save it in your development directory.
# Create a function to read the words from the file.
# Create a function to generate a random sentence of a given length.
# Create a main function to handle user input and program flow.

def get_words_from_file(filename):
    words = []
    try:
        with open(filename, "r") as file:
            words += file.readlines()
            for i, word in enumerate(words):
                words[i] = word.rstrip("\n")
    except FileNotFoundError as e:
        print(f"File was not found: {e}")
    else:
        return words

def get_random_sentence(length):
    words = get_words_from_file(FILE_NAME)
    sentence_lst = []
    for _ in range(length):
        word = random.choice(words)
        sentence_lst.append(word.lower())
    return " ".join(sentence_lst)

def main():
    try:
        length = int(input("PLease enter desired length of sentence between 2 and 20: "))
        if length < 2 or length > 20:
            raise ValueError("Length must be an integer between 2 and 20")
    except Exception as e:
        print (f"Error: {e}")
        exit()
    else:
        print(get_random_sentence(length))


main()


####
## Goal: Access a nested key in a JSON string, add a new key, and save the modified JSON to a file.
# Access the nested “salary” key.
# Add a new key “birth_date” wich value is of format “YYYY-MM-DD”, to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Save the modified JSON to a file.
#
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data_dict = json.loads(sampleJson)
print(data_dict["company"]["employee"]["payable"]["salary"]) ## printing the Salary
employee = data_dict["company"]["employee"]
employee["birth_date"] = "1978-07-29"
try:
    with open("my_json.json", "w") as file:
        json.dump(data_dict, file, indent=2)
except Exception as e:
    print(f"File Error: {e}")        


