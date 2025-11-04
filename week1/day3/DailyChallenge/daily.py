# Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()).

letter_indices = {}
word = input("Enter a word: ")
for index, letter in enumerate(word):
    if letter in letter_indices:
        letter_indices[letter].append(index)
    else:
        letter_indices[letter] = [index]

print(letter_indices)

# Goal: Create a program that prints a list of items that can be purchased with a given amount of money.
# Store Data:

# You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices (as strings with a dollar sign). The priority is defined by the position of the iten on the dictionary: from the most important to the less important.
# You will also be given a string (wallet) representing the amount of money you have.
# 2. Data Cleaning:

#You need to clean the dollar sign and the commas using python. Don’t hard code it.
#3. Determining Affordable Items:

#create a list called basket and add there the items that you can buy with the money you have on the wallet
#Don’t forget to update the wallet after buying an item.
#If the basket is empty (no items can be afforded), return the string “Nothing”.
#Otherwise, print the basket list in alphabetical order.
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
# Data Cleaning
cleaned_wallet = float(wallet.replace("$", "").replace(",", ""))
basket = []
for item, price in items_purchase.items():
    cleaned_price = float(price.replace("$", "").replace(",", ""))
    if cleaned_price <= cleaned_wallet:
        basket.append(item)
        cleaned_wallet -= cleaned_price

if not basket:
    print("Nothing")
else:
    print(sorted(basket))

