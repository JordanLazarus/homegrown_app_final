import string
import sys
import time

print("Welcome to Gills!")

class NotPositiveError(UserWarning):
	pass

#Create a function that contains the details and displays them
#MAKE OPTION FUNCTION FOR PICK-UP OR DELIVERY
def customer_details_delivery():
    #Ask the customer for their name and force user to not leave it blank
    while True:
        customer_name = input("What is your full name?")
        if not customer_name.strip():
            print("Enter your name. It is required.")
            continue
        else:
            break

    #Ask the customer for their address and force user to not leave it blank
    while True:
        customer_address = input("What is your address?")
        if not customer_address.strip():
            print("Enter your address. It is required.")
            continue
        else:
            break

    #Ask the customer for their phone number and force a positive integer
    while True:
        try:
            customer_number = int(input("What is your phone number?"))
            if customer_number <= 0:
                raise NotPositiveError

        except ValueError:
            print("That was not a valid number!")
            #continue the loop and skip everything below
            continue

        except NotPositiveError:
            print("The number was either 0 or not positive, please enter a number above 0.")
            continue

        break


    print("Name: {}, Address: {}, Number {}. Your total order will include a $3 delivery fee.".format(customer_name.capitalize(), string.capwords(customer_address), customer_number))
    return "Name:", customer_name.capitalize(), "Address:", string.capwords(customer_address), "Number:", customer_number

def customer_details_pickup():
    while True:
        customer_name = input("What is your full name?")
        if not customer_name.strip():
            print("Enter your name. It is required.")
            continue
        else:
            break
    print("Ok {}. We will see you at pick up!".format(customer_name.capitalize()))
    return "Name:", customer_name.capitalize()

while True:
    choice = input("Would you like to pick up your order or have it delivered? Type 'pick up' or 'delivery'").lower()

    if choice == "delivery":
        delivery_details = customer_details_delivery()
        time.sleep(7.5)
        break

    elif choice == "pick up":
        pickup_details = customer_details_pickup()

        time.sleep(7.5)
        break

    else:
        print("That wasn't a valid option")
        continue


print("")



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
#Create a delivery fee to add onto the total
delivery_fee = 3
#Create paper bags fee to add onto the total
paper_bags_price = 1

box_size = ["Small", "Medium", "Large"]

max_quantity = 15



menu = print('''MENU:
FRUIT:
Apples: $1 per 3
Bananas: $1 per 2
Grapes: $2 per bag
Watermelon: $2.50 per 1
Oranges: $1 per 3
Pinaapples: $2.10 per 1
Mangoes: $2.10 per 1
Pears: $1.30 per 2
Cherries: $1.40 per bag

VEGETABLES:
Carrots: 50c per 1
Tomatoes: $1.20 per 3
Cucumber: $1.70 per 1
Spinach: $1.40 per bag
Broccoli: $1.60 per bunch
Asparagus: $2.30 per can
Potatoes: $1.20 per 1

MILK & DAIRY PRODUCTS:
Cheese: $1.20 per block
Milk: $2.50 per litre
Yogurt: $1.90 per tub

OTHER:
Nuts: $1.20 per bag
Jam: $1.50 per jar
Juice: $2.20 per litre''')

print("")

print("""Choose an option:
1: Add an item to your cart
2: Remove an item from your cart
3: View your cart
4: View the item menu
5: Process your order
6: Cancel your order
0: Close program""")

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

        loop_add = True
        while loop_add:
            item = input("Enter an item: ").capitalize()
            if item in items:
                shoplist.append(item)
                loop_add = False
            else:
                print("Please enter an item on the menu.")

        while True:
            try:
                quantity = int(input("Enter the quantity:")) # this can generate a valueError if user does not enter a number
                if quantity <= 0:
                    raise NotPositiveError

                if quantity > max_quantity:
                    print("The maximum is 15 at a time!")
                    continue


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
        #if the user has items in their cart they can continue to remove an item
        if shoplist:
            print("Here is your shopping cart:")
            print("=========================================")
            for i in range(len(shoplist)):
                print(quantity_list[i], "x", shoplist[i], "$", round(quantity_list[i] * itempricenumberlist[i],2))
            print("=========================================")


            loop_remove = True
            while loop_remove:
                remove_item = input("Enter an item that your want to remove from your cart: ").capitalize()
                if remove_item in shoplist:
                    # update quantity to be the number corresponding to the item chosen
                    quantity = quantity_list[shoplist.index(remove_item)]
                    quantity_list.remove(quantity)
                    shoplist.remove(remove_item)
                    loop_remove = False

                else:
                    print("")
                    print("Please enter an item on your shopping cart.")

            # update price to be the number corresponding to the item chosen
            item_number = items.index(remove_item)
            itempricenumber = item_prices[item_number]
            itempricenumberlist.remove(itempricenumber)

            print("Here is your shopping cart:")
            print("=========================================")
            for i in range(len(shoplist)):
                print(quantity_list[i], "x", shoplist[i], "$", round(quantity_list[i] * itempricenumberlist[i],2))
            print("=========================================")
        #else the user will be sent back to options
        else:
            print("")
            print("Your shopping cart is empty")

#If option 3 is chosen the user can view their shopping cart
    elif option == 3:
        print("Here is your shopping cart:")
        print("=========================================")
        for i in range(len(shoplist)):
            print(quantity_list[i], "x", shoplist[i], "$", round(quantity_list[i]*itempricenumberlist[i],2))
        print("=========================================")
#If option 4 is chosen the user can view the menu
    elif option == 4:
        menu = print('''MENU:
FRUIT:
Apples: $1 per 3
Bananas: $1 per 2
Grapes: $2 per bag
Watermelon: $2.50 per 1
Oranges: $1 per 3
Pinaapples: $2.10 per 1
Mangoes: $2.10 per 1
Pears: $1.30 per 2
Cherries: $1.40 per bag

VEGETABLES:
Carrots: 50c per 1
Tomatoes: $1.20 per 3
Cucumber: $1.70 per 1
Spinach: $1.40 per bag
Broccoli: $1.60 per bunch
Asparagus: $2.30 per can
Potatoes: $1.20 per 1

MILK & DAIRY PRODUCTS:
Cheese: $1.20 per block
Milk: $2.50 per litre
Yogurt: $1.90 per tub

OTHER:
Nuts: $1.20 per bag
Jam: $1.50 per jar
Juice: $2.20 per litre''')

#If option 5 is chosen the user can either finalise and send through their order, showing the bill and stopping the program after, or continue the order
    elif option == 5:
        #if the user has items in their cart they can continue checkout
        if shoplist:
            final_order = input("Do you want to finalise your order? Type 'yes' or 'no':").lower()
            if final_order == "yes":
                totalprice = sum((x * y for x, y in zip(quantity_list, itempricenumberlist)))
                paper_bags = input("Would you like to use paper bags instead of boxes? Paper Bags cost $1 in total. Type 'yes' or 'no':").lower()
                if paper_bags == 'yes':

                    #if the user chose delivery and paper bags the fees for both are added onto the total and bill
                    if choice == "delivery":

                            print("")
                            print(delivery_details)
                            print("Here is your final order:")
                            print("=========================================")
                            for i in range(len(shoplist)):
                                print(quantity_list[i], "x", shoplist[i], "$", round(quantity_list[i]*itempricenumberlist[i],2))

                            print("Paper bags: $ {}".format(paper_bags_price))
                            print("Delivery Fee: $ {}".format(delivery_fee))

                            print("=========================================")
                            print("Your order total is $", round(totalprice, 2) + paper_bags_price + delivery_fee, ". Thank you for shopping at Gills! Have a good day!")

                            time.sleep(10)
                            sys.exit()

                    #if the user chose pick up and paper bags the fee for the paper bags is added onto the total and bill
                    elif choice == "pick up":


                        print("")
                        print(pickup_details)
                        print("Here is your final order:")
                        print("=========================================")
                        for i in range(len(shoplist)):
                            print(quantity_list[i], "x", shoplist[i], "$", round(quantity_list[i]*itempricenumberlist[i],2))

                        print("Paper bags: $ {}".format(paper_bags_price))

                        print("=========================================")
                        print("Your order total is $", round(totalprice, 2) + paper_bags_price,". Thank you for shopping at Gills! Have a good day!")

                        time.sleep(10)
                        sys.exit()



                elif paper_bags == 'no':

                    #This is where I fill the boxes with information from the user
                    def choosebox(useritemnumber, boxlist):
                        if useritemnumber < 10:
                            return boxlist[0]
                        elif useritemnumber < 20:
                            return boxlist[1]
                        else:
                            return boxlist[2]
                    result = choosebox(sum(quantity_list), box_size)
                    print("")
                    print("You will get a", result, "Sized Box with your order")

                    #if the user chose delivery and boxes the fee for the delivery is added onto the total and bill and the box size is said at the top
                    if choice == "delivery":

                        print("")
                        print(delivery_details)
                        print("Here is your final order:")
                        print("=========================================")
                        for i in range(len(shoplist)):
                            print(quantity_list[i], "x", shoplist[i], "$", round(quantity_list[i]*itempricenumberlist[i],2))

                        print("Delivery Fee: $ {}".format(delivery_fee))

                        print("=========================================")
                        print("Your order total is $", round(totalprice, 2) + delivery_fee, ". Thank you for shopping at Gills! Have a good day!")

                        time.sleep(10)
                        sys.exit()

                    #if the user chose pick up and boxes the box size is said at the top
                    elif choice == "pick up":


                        print("")
                        print(pickup_details)
                        print("Here is your final order:")
                        print("=========================================")
                        for i in range(len(shoplist)):
                            print(quantity_list[i], "x", shoplist[i], "$", round(quantity_list[i]*itempricenumberlist[i],2))


                        print("=========================================")
                        print("Your order total is $", round(totalprice, 2),". Thank you for shopping at Gills! Have a good day!")

                        time.sleep(10)
                        sys.exit()




                else:
                    print("That is not a valid option!")
                continue



            elif final_order == "no":
                print("")

            else:
                print("That is not a valid option!")
                continue
        #else the program breaks the loop and brings user back to options
        else:
            print("")
            print("Your shopping cart is empty. You must enter an item before you checkout.")


#If option 6 is chosen the user can choose to either cancel the order or continue the order

    elif option == 6:
        cancel_order = input("Are you sure you want to cancel your order? Type 'yes' or 'no'?").lower()
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
1: Add an item to your cart
2: Remove an item from your cart
3: View your cart
4: View the item menu
5: Process your order
6: Cancel your order
0: Close program""")

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


