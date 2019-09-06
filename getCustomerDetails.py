import string

#Make a total price for delivery and pick-up
#delivery_total = shoplist_price + 3
#pickup_total = shoplist_price

#This is where I fill the boxes with information from the user
#Create a function that contains the details and displays them
#MAKE OPTION FUNCTION FOR PICK-UP OR DELIVERY
choice = input("Would you like to pick up your order or have it delivered? Type 'pick up' or 'delivery'")

if choice == "delivery":
    def customer_details_delivery():
    #Ask the customer for their name
        customer_name = input("What is your full name?")
    #Ask the customer for their address
        customer_address = input("What is your address?")
    #Ask the customer for their phone number
        customer_number = int(input("What is your phone number?"))
        print("Name: {}, Address: {}, Number: {}. Your total order will include a $3 delivery fee.".format(customer_name.capitalize(), string.capwords(customer_address), customer_number))


elif choice == "pick up":
    def customer_details_pickup():
        customer_name = input("What is your full name?")
        print("Ok {}. We will see you at pick up!".format(customer_name.capitalize()))


