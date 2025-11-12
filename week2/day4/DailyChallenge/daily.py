from collections import Counter
import string
import re
from faker import Faker


# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.

FILE_NAME = "./daily_input.txt"

class Text:
    def __init__(self , a_str):
        if type(a_str) is not str:
            raise TypeError("you can create Text Objects only from strings")
        self.text = a_str
    
    def word_frequency(self, word):
        words = self.text.split()
        frequency = words.count(word)
        if frequency == 0:
            return None
        else:
            return frequency
    
    def most_common_word(self):
        words = self.text.split()
        frequency_dict = Counter(words)
        max_word = ""
        max_val = 0.
        for word, val in frequency_dict.items():
            if val > max_val:
                max_word = word
                max_val = val
        return max_word
    
    def unique_words(self):
        words = self.text.split()
        return list(set(words))
    @classmethod
    def from_file(cls, path):
        lines = []
        try:
            with open(path, "r") as file:
                lines += file.readlines()
                a_str = "\n".join(lines)
                return cls(a_str)
        except FileNotFoundError as e:
            print(f"Error: {e}")


class TextModification(Text):
    def __init__(self, a_str):
        super().__init__(a_str)

    def remove_punctuation(self):
        # string.punctuation
        characters = []
        for c in self.text:
            if c not in string.punctuation:
                characters.append(c)
        return "".join(characters)
    
    def remove_stop_words(self):
        stop_words = ["i", "me", "my", "myself", "we", "our", "ours", 
                      "ourselves", "you", "your", "yours", "yourself", 
                      "yourselves", "he", "him", "his", "himself", "she", 
                      "her", "hers", "herself", "it", "its", "itself", "they", 
                      "them", "their", "theirs", "themselves", "what", "which", 
                      "who", "whom", "this", "that", "these", "those", "am", ""
                      "is", "are", "was", "were", "be", "been", "being", 
                      "have", "has", "had", "having", "do", "does", "did", 
                      "doing", "a", "an", "the", "and", "but", "if", "or", 
                      "because", "as", "until", "while", "of", "at", "by", 
                      "for", "with", "about", "against", "between", "into",
                      "through", "during", "before", "after", "above", 
                      "below", "to", "from", "up", "down", "in", "out", 
                      "on", "off", "over", "under", "again", "further", 
                      "then", "once", "here", "there", "when", "where", 
                      "why", "how", "all", "any", "both", "each", "few", 
                      "more", "most", "other", "some", "such", "no", "nor", 
                      "not", "only", "own", "same", "so", "than", "too", "very", 
                      "s", "t", "can", "will", "just", "don", "should", "now"]
        
        words = self.text.split()
        no_stop_words = [w for w in words if w not in stop_words]
        return " ".join(no_stop_words)
    
    def remove_special_characters(self):
        return re.sub(r"[:punct:]", "",self.text)
    

### Usage Example:

fake = Faker()
long_text = fake.text(max_nb_chars=5000)
long_text2 = fake.text(max_nb_chars=2000)
my_text = Text(long_text)
my_text_mod = TextModification(long_text2)
print(my_text.word_frequency("the"))
print(my_text.most_common_word())
print(my_text.unique_words())
my_text_from_file = Text.from_file(FILE_NAME)
print(my_text_from_file.most_common_word())
print(my_text_mod.remove_stop_words())





