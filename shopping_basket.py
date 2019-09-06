import sys
import time
#Create a list containing the items
items = ['Apples', 'Bananas', 'Grapes', 'Watermelon', 'Oranges', 'Pineapples', 'Mangoes', 'Pears', 'Cherries', 'Carrots', 'Tomatoes', 'Cucumber', 'Spinach', 'Broccoli',
'Asparagus', 'Potatoes', 'Cheese', 'Milk', 'Yogurt', 'Nuts', 'Jam', 'Juice']
#Item Prices list
item_prices = [1, 1, 2, 2.5, 1, 2.1, 2.1, 1.3, 1.4, 0.5, 1.2, 1.7, 1.4, 1.6, 2.3, 1.2, 1.2, 2.5, 1.9, 1.2, 1.5, 2.2]
#Store the user's quantities
quantity_list = []
#According to the index of the items chosen the same indexes from the prices list will be stored to match the item's price
itempricenumberlist = []
#Create a shopping list
shoplist = []

max_quantity = 15

class NotPositiveError(UserWarning):
	pass

menu = print('''Menu:
Fruits:
Apples: $1 per 3
Bananas: $1 per 2
Grapes: $2 per bag
Watermelon: $2.50 per 1
Oranges: $1 per 3
Pinaapples: $2.10 per 1
Mangoes: $2.10 per 1
Pears: $1.30 per 2
Cherries: $1.40 per bag

Vegetables:
Carrots: 50c per 1
Tomatoes: $1.20 per 3
Cucumber: $1.70 per 1
Spinach: $1.40 per bag
Broccoli: $1.60 per bunch
Asparagus: $2.30 per can
Potatoes: $1.20 per 1

Milk & Dairy Products:
Cheese: $1.20 per block
Milk: $2.50 per litre
Yogurt: $1.90 per tub

Other:
Nuts: $1.20 per bag
Jam: $1.50 per jar
Juice: $2.20 per litre''')

print("")

print("""Choose an option:
1: Add an item to your basket
2: Remove an item from your basket
3: View your basket
4: View the item menu
5: Send your order
6: Cancel your order
0: Close program
If you want to remove an item it must be on your shopping list before trying to remove it, otherwise the program will close""")

while True:
    try:
        option = int(input("Enter an option: "))
        break
    except ValueError:
        print("Please enter a number")


#Ask the user which option they want to choose
while option != 0:
#If option 1 is chosen add an item
    if option == 1:

        print("")

        item = input("Enter an item: ")
        shoplist.append(item)
        while True:
            try:
                quantity = int(input("Enter the quantity:")) # this can generate a valueError if user does not enter a number
                if quantity <= 0:
                    raise NotPositiveError

                if quantity > max_quantity:
                    print("The maximum is 15 at a time!")
                    continue

                #break
            except ValueError:
                print("That was not a valid number!")
                #continue the loop and skip everything below
                continue

            except NotPositiveError:
                print("The number was either 0 or not positive, please enter a number above 0.")
                continue

            break

        quantity_list.append(quantity)
        print(quantity_list)  # this allows for testing if the append function works

        item_number = items.index(item)
        itempricenumber = item_prices[item_number]

        itempricenumberlist.append(itempricenumber)
#If option 2 is chosen remove an item
    elif option == 2:
        print("Here is your shopping list:")
        for i in range(len(shoplist)):
            print(quantity_list[i], "x", shoplist[i])
        remove_item = input("Enter an item that your want to remove from your list: ")
        shoplist.remove(remove_item)
        quantity_list.remove(quantity)

#If option 3 is chosen the user can view their shopping list
    elif option == 3:
        print("Here is your shopping list:")
        for i in range(len(shoplist)):
            print(quantity_list[i], "x", shoplist[i], "$", round(quantity_list[i]*itempricenumberlist[i],2))
#If option 4 is chosen the user can view the menu
    elif option == 4:
        menu = print('''Menu:
Fruits:
Apples: $1 per 3
Bananas: $1 per 2
Grapes: $2 per bag
Watermelon: $2.50 per 1
Oranges: $1 per 3
Pinaapples: $2.10 per 1
Mangoes: $2.10 per 1
Pears: $1.30 per 2
Cherries: $1.40 per bag

Vegetables:
Carrots: 50c per 1
Tomatoes: $1.20 per 3
Cucumber: $1.70 per 1
Spinach: $1.40 per bag
Broccoli: $1.60 per bunch
Asparagus: $2.30 per can
Potatoes: $1.20 per 1

Milk & Dairy Products:
Cheese: $1.20 per block
Milk: $2.50 per litre
Yogurt: $1.90 per tub

Other:
Nuts: $1.20 per bag
Jam: $1.50 per jar
Juice: $2.20 per litre''')

#If option 5 is chosen the user can either finalise and send through their order, showing the bill and stopping the program after, or continue the order
    elif option == 5:
        final_order = input("Do you want to finalise your order? Type 'yes' or 'no'")
        if final_order == "yes":
            print("Here is your final order:")
            for i in range(len(shoplist)):
                print(quantity_list[i], "x", shoplist[i], "$", round(quantity_list[i]*itempricenumberlist[i],2))

                #print("Delivery fee: ${}".format(delivery_total))
                #print("Paper bags: ${}".format(paper_bags))

                #print("Your order total is $ []. Have a good day!")
            time.sleep(10)
            sys.exit()



        elif final_order == "no":
            print("")

        else:
            print("That is not a valid option!")
            continue
#If option 6 is chosen the user can choose to either cancel the order or continue the order

    elif option == 6:
        cancel_order = input("Are you sure you want to cancel your order? Type 'yes' or 'no'?")
        if cancel_order == "yes":
            sys.exit()

        elif cancel_order == "no":
            print("")

        else:
            print("That is not a valid option!")
            continue

    elif option != 0:
        print("You didn't enter a valid option")
    print("")
    print("""Choose an option:
1: Add an item to your basket
2: Remove an item from your basket
3: View your basket
4: View the item menu
5: Send your order
6: Cancel your order
0: Close program
If you want to remove an item it must be on your shopping list before trying to remove it, otherwise the program will close""")

    while True:
        try:
            option = int(input("Enter an option: "))
            break
        except ValueError:
            print("Please enter a number")






#for item in items:

'''
Apples: $1 per 3
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
Juice: $2.20 per litre'''

