# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.
Hot_Dog = 3.5
Chili_Dog = 4.5
Cheese = 0.5
Peppers = 0.75
Grilled_onions = 1
Tax = 0.07
order = str(input("Please state your order: "))
if order == "hot dog":
    print ("Your total is $", (Hot_Dog*Tax)+Hot_Dog)
elif order == "hot dog and cheese":
    print ("Your total is", ((Hot_Dog+Cheese)*Tax)+(Hot_Dog+Cheese))
elif order == "hot dog and peppers":
    print ("Your total is", ((Hot_Dog+Peppers)*Tax)+(Hot_Dog+Peppers))
elif order == "hot dog and grilled onions":
    print("Your total is", ((Hot_Dog+Grilled_onions)*Tax)+(Hot_Dog+Grilled_onions))
elif order == "hot dog and cheese and grilled onions":
    print("Your total is", ((Hot_Dog+Grilled_onions+Cheese)*Tax)+(Hot_Dog+Grilled_onions+Cheese))
elif order == "hot dog and grilled onions and peppers":
    print("Your total is", ((Hot_Dog+Grilled_onions+Peppers)*Tax)+(Hot_Dog+Grilled_onions+Peppers))
elif order == "hot dog and grilled onions and cheese and peppers":
    print("Your total is",((Hot_Dog+Grilled_onions+Cheese+Peppers)*Tax)+(Hot_Dog+Grilled_onions+Peppers+Cheese))
elif order == "hot dog and cheese and peppers":
    print("Your total is", ((Hot_Dog+Cheese+Peppers)*Tax)+(Hot_Dog+Cheese+Peppers))
if order == "chili dog":
    print ("Your total is $", (Chili_Dog*Tax)+Chili_Dog)
elif order == "chili dog and cheese":
    print ("Your total is", ((Chili_Dog+Cheese)*Tax)+(Chili_Dog+Cheese))
elif order == "chili dog and peppers":
    print ("Your total is", ((Chili_Dog+Peppers)*Tax)+(Chili_Dog+Peppers))
elif order == "chili dog and grilled onions":
    print("Your total is", ((Chili_Dog+Grilled_onions)*Tax)+(Chili_Dog+Grilled_onions))
elif order == "chili dog and cheese and grilled onions":
    print("Your total is", ((Chili_Dog+Grilled_onions+Cheese)*Tax)+(Chili_Dog+Grilled_onions+Cheese))
elif order == "chili dog and grilled onions and peppers":
    print("Your total is", ((Chili_Dog+Grilled_onions+Peppers)*Tax)+(Chili_Dog+Grilled_onions+Peppers))
elif order == "chili dog and grilled onions and cheese and peppers":
    print("Your total is",((Chili_Dog+Grilled_onions+Cheese+Peppers)*Tax)+(Chili_Dog+Grilled_onions+Peppers+Cheese))
elif order == "chili dog and cheese and peppers":
    print("Your total is", ((Chili_Dog+Cheese+Peppers)*Tax)+(Chili_Dog+Cheese+Peppers))
