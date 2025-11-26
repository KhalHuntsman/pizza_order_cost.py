#!/usr/bin/python3

# Author: <Hunter Steele>
# Date: <11/20/25>
# version: 1.3

size = input("Would you like a small or large pizza? (small or large) ").lower() # determine the size of the pizza, .lower() for case insensitivity per ChatGPT suggestion
toppings = float(input("What toppings would you like? (toppings are $1 each, half toppings are 0.5 each)")) # use float to allow for half toppings
del_distance = int(input("How far will we be delivering to you? (round to the nearest whole mile)")) # determine how far delivery will be

# determine pizza size cost
if size == "large":
    size_cost = 12
elif size == "small":
    size_cost = 8
else:
    print("Your input is incorrect, please give a proper input.")
    exit()

# toppings cost
toppings_cost = toppings #toppings are $1 per topping or 0.50 for a half topping

# delivery cost, checks distance and sets order status plus del cost if any
if del_distance >= 30:
    print("Unfortunately you are outside of our delivery radius, we apologize for any inconvenience, have a nice day!")
    order = "cancelled"
    exit()
elif del_distance == 0:
    print("Your order has been marked for pickup only!")
    del_cost = -2
    order = "pickup"
elif del_distance <= 5:
    del_cost = 2
    order = "delivery"
elif del_distance > 5:
    del_cost = 2 + (del_distance - 5)
    order = "delivery"

# total cost calculation
total_del_cost = size_cost + toppings_cost + del_cost

total_pickup_cost = size_cost + toppings_cost

# set result for a pizza marked for delivery
delivery_result = (f"You want a {size} pizza with {toppings} toppings delivered {del_distance} miles, giving you a total cost of {total_del_cost}! Will that be cash or card?")

# set result for a pizza marked for pickup
pickup_result = (f"You want a {size} pizza with {toppings} toppings for pickup giving you a total cost of {total_pickup_cost}! Will that be cash or card?")

# print result
if order == "pickup":
    print(pickup_result)
elif order == "delivery":
    print(delivery_result)

'''
<used chat GPT for minor suggestions such as:
    removing multiplications by 1 for toppings and delivery distance,
    adding "exit()" after invalid inputs or canelled orders to prevent a potential continuation of the program to error out>
'''

'''
<revised after comment from professor, check github commentary>
'''