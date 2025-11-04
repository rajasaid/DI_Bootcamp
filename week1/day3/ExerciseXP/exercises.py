

# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)  # Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


# Write a program that calculates the total cost of movie tickets for a family based on their ages.
# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for name, age in family.items():
    if age < 3:
        print(f"{name} is free to enter.")
        total_cost += 0
    elif 3 <= age <= 12:
        print(f"{name} has to pay $10.")
        total_cost += 10
    else:
        print(f"{name} has to pay $15.")
        total_cost += 15
print(f"Total cost for the family is: ${total_cost}")  # Output: Total cost for the family is: $50

#Bonus:
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.
family = {}
num_members = int(input("Enter the number of family members: "))
for _ in range(num_members):
    name = input("Enter the name of the family member: ")
    age = int(input(f"Enter the age of {name}: "))
    family[name] = age
total_cost = 0
for name, age in family.items():
    if age < 3:
        print(f"{name} is free to enter.")
        total_cost += 0
    elif 3 <= age <= 12:
        print(f"{name} has to pay $10.")
        total_cost += 10
    else:
        print(f"{name} has to pay $15.")
        total_cost += 15
print(f"Total cost for the family is: ${total_cost}")

# Create and manipulate a dictionary that contains information about the Zara brand.
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
#major_color: 
 #   France: blue, 
 #   Spain: red, 
 #   US: pink, green
# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
print(f"Zara's clients are: {', '.join(brand['type_of_clothes'])}.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(f"The last international competitor is: {brand['international_competitors'][-1]}.")
print(f"The major colors in the US are: {', '.join(brand['major_color']['US'])}.")
print(f"The number of keys in the brand dictionary is: {len(brand)}.")
print(f"The keys in the brand dictionary are: {', '.join(brand.keys())}.")

# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)
print(brand)

# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# 1. Create a dictionary that maps characters to their indices:
disney_users_A = {user: index for index, user in enumerate(users)}
print(disney_users_A)  
# 2. Create a dictionary that maps indices to characters:
disney_users_B = {index: user for index, user in enumerate(users)}
print(disney_users_B)
# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
disney_users_C = {user: index for index, user in enumerate(sorted(users))}
print(disney_users_C)

