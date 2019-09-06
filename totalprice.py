print("""This is a test to calculate to total price of an order. The values in the list will be replaced with the fixed prices
and the quantities that the user enters. This multiplies the index of each list together and then finds the sum of the
lists to figure out the total price of the order""""")
quantity_list = [1, 2, 3, 4]
itempricenumberlist = [5, 3, 6, 7]
#print((quantity_list, itempricenumberlist), [x * y for x, y in zip(quantity_list, itempricenumberlist)],sum(x * y for x, y in zip(quantity_list, itempricenumberlist)))

print("$", sum(x * y for x, y in zip(quantity_list, itempricenumberlist)))
