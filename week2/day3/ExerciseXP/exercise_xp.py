import random
import string
import datetime
from faker import Faker

# Goal: Implement dunder methods for a Currency class to handle string representation, integer conversion, addition, and in-place addition.

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):
        line = f"{self.amount} {self.currency}"
        if self.amount > 1:
            line+="s"
        return line
    def __repr__(self):
        return str(self)
    def __int__(self):
        return self.amount
    def __add__(self, other):
        if isinstance(other,Currency):
            if other.currency != self.currency:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
            else:
                return self.amount + other.amount
        elif type(other) == int:
            return self.amount + other
        else:
            raise TypeError("nor supported type to add to Currency Object")
    def __iadd__(self, other):
        if isinstance(other,Currency):
            if other.currency != self.currency:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
            else:
                self.amount += other.amount
                return self
        elif type(other) == int:
            self.amount += other
            return self 
        else:
            raise TypeError("nor supported type to add to Currency Object") 

## usage example:

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

# TypeError: Cannot add between Currency type <dollar> and <shekel>  
try:
    print(c1 + c3)
except TypeError as e:
    print(f"Exception happened: {e}")    
 

####
## Goal: Generate a random string of length 5 using the string module.
# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.

random_string = "".join(random.sample(string.ascii_letters,5))
print(random_string)

####
## Goal: Create a function that displays the current date.
# Use the datetime module to create a function that displays the current date.
today = datetime.date.today()
print(today)

####
## Goal: Create a function that displays the amount of time left until January 1st.
# Use the datetime module to calculate and display the time left until January 1st.

target_date = datetime.date(2026,1,1)
difference = (target_date - today).days
print(f"You have {difference} days for {target_date}")

##
# Instructions: Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.
try:
    birthday = input("Please Enter you birthday format <YYYY/MM/DD>:")
    dt = datetime.datetime.strptime(birthday, "%Y/%m/%d")
except Exception as e:
    print(f"Exception happened: {e}")
today = datetime.datetime.today()
days_lived = (today - dt).days
minutes_lived = days_lived * 24 * 60
print(f"You have been living for {minutes_lived} minutes")

####
## Goal: Use the faker module to generate fake user data and store it in a list of dictionaries.
# 
# Install the faker module and use it to create a list of dictionaries, where each dictionary represents a user with fake data.
fake = Faker()
users = []
def generate_fake_users(number_of_users):
    global users
    for _ in range(number_of_users):
        user = dict()
        user['name'] = fake.name()
        user['address'] = fake.address()
        user['language_code'] = fake.language_code()
        users.append(user)

generate_fake_users(10)
print(users)