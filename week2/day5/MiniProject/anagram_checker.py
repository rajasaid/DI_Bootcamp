# An anagram checker program that takes user input, validates it, and finds anagrams from a word list.
import os

class AnagramChecker:
    def __init__(self,file_path):
        words = []
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError("File not found!")
            with open(file_path, "r") as file:
                words += file.readlines()
        except Exception as e:
            print(f"Error Creating AnagramChecker Object: {e}")
        else:
            self.words = [w.lower().strip() for w in words]

    def is_valid_word(self, word):
        return True if word.lower() in self.words else False

    def is_anagram(self, word1, word2):
        sorted1 = sorted([c for c in word1])
        sorted2 = sorted([c for c in word2])
        return sorted1 == sorted2
    
    def get_anagrams(self, word):
        anagrams = [w for w in self.words if w != word and self.is_anagram(w,word)]
        return anagrams
    
    




