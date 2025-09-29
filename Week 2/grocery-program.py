groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}
shopping_list = []

answer = input("What do you want to buy? (type 'done' to finish): ")
while answer != "done":
    if answer in groceries:
        shopping_list.append(answer)
    else:
        print("Sorry, we don’t have that item")
    answer = input("What do you want to buy? (type 'done' to finish): ")
        
# Calculate total cost after shopping is done
totalcost = 0
for item in shopping_list:
    totalcost += groceries[item]

print("You bought:", shopping_list)
print("Total:", totalcost)
if totalcost > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")