
import math

#Goal:
#Create a Pagination class that simulates a basic pagination system.
#Step 1: Create the Pagination Class
#Define a class called Pagination to represent paginated content.
#It should optionally accept a list of items and a page size when initialized.
#Step 2: Implement the __init__ Method
#Accept two optional parameters:
#items (default None): a list of items
#page_size (default 10): number of items per page
#Behavior:
#If items is None, initialize it as an empty list.
#Save page_size and set current_idx (current page index) to 0.
#Calculate total number of pages using math.ceil.
#Step 3: Implement the get_visible_items() Method
#This method returns the list of items visible on the current page.
#Use slicing based on the current_idx and page_size.
#Step 4: Implement Navigation Methods
#These methods should help navigate through pages:
#go_to_page(page_num)
#→ Goes to the specified page number (1-based indexing).
#→ If page_num is out of range, raise a ValueError.
#first_page()
#→ Navigates to the first page.
#last_page()
#→ Navigates to the last page.
#next_page()
#→ Moves one page forward (if not already on the last page).
#previous_page()
#→ Moves one page backward (if not already on the first page).
##
# Note:
#
#Pages are indexed internally from 0, but user input is expected to start at 1.
#All navigation methods (except go_to_page) should return self to allow method chaining.
#Bonus
#Step 5: Add a Custom __str__() Method
#This magic method should return a string displaying the items on the current page, each on a new line.

class Pagination():
    def __init__(self, items = None, page_size = 10):
        if items is None:
            self.items = []
        else:
            self.items = items
        if page_size <= 0:
            raise ValueError("Value of page size must be a positive number!")
        else:    
            self.page_size = page_size
        self.__current_idx = 0
        self.total_pages = math.ceil(len(items) / page_size)
    
    def get_current_index(self):
        return self.__current_idx
    
    def get_visible_items(self):
        return self.items[self.__current_idx:self.__current_idx+self.page_size:1]
    
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page Number is out of range!")
        self.__current_idx = page_num*self.page_size - self.page_size
        return self
    
    def first_page(self):
        self.__current_idx = 0
        return self
    def last_page(self):
        self.__current_idx = self.total_pages*self.page_size - self.page_size
        return self
    def next_page(self):
        current_page = math.ceil(self.__current_idx/self.page_size) + 1
        if current_page < self.total_pages:
            self.__current_idx += self.page_size
        return self
    def previous_page(self):
        current_page = math.ceil(self.__current_idx/self.page_size) + 1
        if current_page > 1:
            self.__current_idx -= self.page_size
        return self
    def __str__(self):
        line = ""
        try:
            for page in range(1, self.total_pages+1):
                self.go_to_page(page)
                line += ", ".join(self.get_visible_items())
                line += "\n"
        except Exception as e:
            return "Internal bug!"
        else:        
            return line    
        
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
# print(str(p))
print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']
try:
    p.go_to_page(10)
except Exception as e:
    print(f"Error returned: {e}")
finally:    
    print(p.get_current_index() + 1)
# Output: ValueError
try:
    p.go_to_page(0)
except Exception as e:
    print(f"Error returned: {e}")