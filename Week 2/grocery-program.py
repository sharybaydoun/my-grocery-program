groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}

shopping_cart = {}
answer = input("What do you want to buy and how many? (type 'done' to finish): ")
while answer != "done":
    parts = answer.split()
    if len(parts) == 2 and parts[0] in groceries and parts[1].isdigit():
        item = parts[0]
        quantity = int(parts[1])
        shopping_cart[item] = shopping_cart.get(item, 0) + quantity
    else:
        print("Sorry, we don’t have that item or the format is wrong (use: item quantity)")
    answer = input("What do you want to buy and how many? (type 'done' to finish): ")
  
    
# Calculate total cost after shopping is done
totalcost = 0
for item in shopping_cart:
      totalcost += groceries[item] * shopping_cart[item]
      if item == "milk" and shopping_cart[item] > 2:
        totalcost -=1



print("You bought:", shopping_cart)
print("Total:", totalcost)
if totalcost > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")