

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {3, 7, 21}
my_fav_numbers.add(42)
my_fav_numbers.add(99)
my_fav_numbers.remove(99)
friend_fav_numbers = {5, 12, 21}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

#Given a tuple of integers, try to add more integers to the tuple.
my_tuple = (1,2,3,4)
my_second_tuple = my_tuple + tuple(range(5,10))
print(my_second_tuple)

#You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
print("Number of times 'Apples' appear in the list:", apple_count)
basket.clear()
print(basket)

#Recap: What is a float? What’s the difference between a float and an integer?
#Create a list containing the following sequence of mixed types: floats and integers:
#1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
#Avoid hard-coding each number manually.
#Think: Can you generate this sequence using a loop or another method?

mixed_numbers = [x * 0.5 for x in range(3, 11)]
print(mixed_numbers)

#Write a for loop to print all numbers from 1 to 20, inclusive.
#Write another for loop that prints every number from 1 to 20 where the index is even.
for num in range(1, 21):
    print(num)
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#Use an input to ask the user to enter their name.
#Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
#hint: check for the method isdigit()
#if the input is incorrect, keep asking for the correct input until it is correct
#if the input is correct print “thank you” and break the loop
name = input("What is your name?")
while True:
    if (len(name) < 3):
        name = input("Please give the correct name?")
        continue
    bad = False
    for c in name:
        if c.isdigit():
            bad = True
            break
    if bad == True:
        name = input("Please give the correct name?")
        continue
    else:    
        print("Thank you")
        break

#Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
#Store these fruits in a list.
#Ask the user to input the name of any fruit.
#If the fruit is in their list of favorite fruits, print:
#"You chose one of your favorite fruits! Enjoy!"
#If not, print:
#"You chose a new fruit. I hope you enjoy it!"
fruits = input("Please enter your favourite fuits seperated by spaces").split(" ")
a_fruit = input("Please input any fruit")
if a_fruit in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")    

#Write a loop that asks the user to enter pizza toppings one by one.
#Stop the loop when the user types 'quit'.
#For each topping entered, print:
#"Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.
toppings = []
while True:
    topping = input("Please choose a topping for your pizza: ")
    if topping == "quit":
        break
    toppings.append(topping)
cost = 10 + 2.5*len(toppings)    
print(f"Your Pizza Toppings are {toppings}, and the total cost is {cost}")

#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.
str_ages = input("Please enter the ages of the people in the family who wants to buy a movie ticket (seperated by spaces): ").split(" ")
ages = [int(age) for age in str_ages if type(age) == str and age != '' and age is not None]
total_cost = 0
for age in ages:
    if age < 3:
        continue
    elif 3 <= age <= 12:
        total_cost += 10
    else:
        total_cost += 15
print(f"The total cost for the family is {total_cost} USD")

#Bonus:
#Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
#Write a program to:
#Ask for each person’s age.
#Remove anyone who isn’t allowed to watch.
#Print the final list of attendees.
str_ages = input("Please enter your ages who want to buy a movie ticket (seperated by spaces): ").split(" ")
ages = [int(age) for age in str_ages if type(age) == str and age != '' and age is not None]
ages_to_remove = []
for age in ages:
    if age < 16:
        ages_to_remove.append(age)
for age in ages_to_remove:
    ages.remove(age)
print(f"the ages that are allowed to enter the movie are {ages}")
