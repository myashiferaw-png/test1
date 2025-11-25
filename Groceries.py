Groceries={"tofu": 5.99,
            "spinach": 6.99,
            "fish": 54.99,
            "pasta": 5.99,
            "chocolate": 4.99,
            "kimchi": 12.99,
            "taco shell": 7.99}
mycart={}
total=0
print("Hello, welcome to M&M Groceries.")
print("Please choose your selection from our fresh groceries. When complete please type checkout.")
print("your selections are." , list(Groceries.keys()))
while True:
    item=input("Choose your item ").lower().strip()
    if item == "checkout":
        break
    if item in Groceries:
        try: 
            qty=int(input(f" How many {item}: "))
            if qty <=0:
                print("invalid amount, please enter one or more")
                continue
        except ValueError:
            print("You need to enter a number")
            continue
        if item in mycart:
            mycart[item] +=qty
        else:
            mycart[item] = qty
    else:
        print("You have made invalid selection. Please choose from the list")

print ("*******FINAL BILL********")
for item, qty in mycart.items():
    price=Groceries[item]
    itemtotal=price*qty
    total +=itemtotal
    print(f"{item} x{qty}= ${itemtotal:.2f}")

print(f"Total: ${total:.2f}")