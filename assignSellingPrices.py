#Display the items and the prices of each item

items = ['Apples', 'Bananas', 'Grapes', 'Watermelon', 'Oranges', 'Pineapples', 'Mangoes', 'Pears', 'Cherries', 'Carrots', 'Tomatoes', 'Cucumber', 'Spinach', 'Broccoli',
'Asparagus', 'Potatoes', 'Cheese', 'Milk', 'Yogurt', 'Nuts', 'Jam', 'Juice']
item_prices = [1, 1, 2, 2.5, 1, 2.1, 2.1, 1.3, 1.4, 0.5, 1.2, 1.7, 1.4, 1.6, 2.3, 1.2, 1.2, 2.5, 1.9, 1.2, 1.5, 2.2]
quantity_list = []
itempricenumberlist = []


#for item in items:
print('''Apples: $1 per 3
Bananas: $1 per 2
Grapes: $2 per bag
Watermelon: $2.50 per 1
Oranges: $1 per 3
Pinaapples: $2.10 per 1
Mangoes: $2.10 per 1
Pears: $1.30 per 2
Cherries: $1.40 per bag
Carrots: 50c per 1
Tomatoes: $1.20 per 3
Cucumber: $1.70 per 1
Spinach: $1.40 per bag
Broccoli: $1.60 per bunch
Asparagus: $2.30 per can
Potatoes: $1.20 per 1
Cheese: $1.20 per block
Milk: $2.50 per litre
Yogurt: $1.90 per tub
Nuts: $1.20 per bag
Jam: $1.50 per jar
Juice: $2.20 per litre''')

#Create a shopping list
shoplist = []

#Add option to add items to the list
add = input("Would you like to add an item to your list? Yes or No?")



while add.lower() == "yes":
    item = input("What would you like to add?")
    shoplist.append(item)


    while True:
        try:
          quantity = int(input("Enter the quantity:"))
          break
        except ValueError:

          print("That was not a valid number!")

    quantity_list.append(quantity)


    item_number = items.index(item)
    itempricenumber = item_prices[item_number]
    print("$",itempricenumber)

    itempricenumberlist.append(itempricenumber)

    add = input("Would you like to add another item to your list? Yes or No?")

if add.lower() == "no":
    print()
    print("Here is your list in alphabetical order:")
    shoplist.sort()
    quantity_list.sort()
    itempricenumberlist.sort()


    for i in range(len(shoplist)):
        print(quantity_list[i], "x", shoplist[i], " - $", round(itempricenumberlist[i] * quantity_list[i], 2))


else:
    print("That is not a valid option! Enter a valid option next time")


















