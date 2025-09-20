# Mini Project: Week-wise Canteen Menu

# Dictionary: day -> {item_no: (item, price)}
weekly_menu = {
    "monday": {
        1: ("Poha", 20),
        2: ("Tea", 10),
        3: ("Samosa", 15)
    },
    "tuesday": {
        1: ("Idli", 30),
        2: ("Coffee", 15),
        3: ("Sandwich", 40)
    },
    "wednesday": {
        1: ("Paratha", 25),
        2: ("Lassi", 30),
        3: ("Chole Bhature", 50)
    },
    "thursday": {
        1: ("Maggi", 25),
        2: ("Tea", 10),
        3: ("Pakora", 20)
    },
    "friday": {
        1: ("Dosa", 40),
        2: ("Cold Drink", 20),
        3: ("Vada Pav", 15)
    },
    "saturday": {
        1: ("Thali", 80),
        2: ("Roti Sabzi", 50),
        3: ("Jalebi", 30)
    },
    "sunday": {
        1: ("Chole Kulche", 60),
        2: ("Ice Cream", 40),
        3: ("Pasta", 50)
    }
}

# Special dish of the day
special_dish = {
    "monday": "Poha with a twist of peanuts",
    "tuesday": "Steamy Idli served with spicy chutney",
    "wednesday": "Chole Bhature – the king of taste",
    "thursday": "Maggi magic for your hunger",
    "friday": "Crispy Dosa – south Indian delight",
    "saturday": "Full Thali – feast like a king",
    "sunday": "Chole Kulche – perfect Sunday vibes"
}

print("==========================================")
print("         WELCOME TO THE COLLEGE CANTEEN   ")
print("       Good food = Good mood! Stay Happy  ")
print("==========================================")

day = input("Enter day of the week: ").lower()

if day not in weekly_menu:
    print("Sorry, no menu available for this day.")
else:
    print(f"\nMenu for {day.title()}:")
    menu = weekly_menu[day]
    for key, value in menu.items():
        print(f"{key}. {value[0]} - Rs.{value[1]}")

    # Show special dish line
    print("\nSpecial Dish:", special_dish[day])

    order = {}
    while True:
        try:
            choice = int(input("\nEnter item number (0 to finish): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            break
        elif choice in menu:
            try:
                qty = int(input("Enter quantity: "))
            except ValueError:
                print("Please enter a valid quantity.")
                continue
            order[choice] = order.get(choice, 0) + qty
        else:
            print("Invalid choice. Try again.")

    # Bill Calculation
    if order:
        print("\n============= BILL RECEIPT =============")
        print(f"Day: {day.title()}")
        total = 0
        for item_no, qty in order.items():
            item, price = menu[item_no]
            cost = price * qty
            total += cost
            print(f"{item} x {qty} = Rs.{cost}")

        print("----------------------------------------")
        print(f"Total Bill = Rs.{total}")
        print("========================================")
        print("Thank you for visiting our Canteen")
        print("Come hungry, leave happy")
        print("========================================")
    else:
        print("\nNo items selected. Visit again when hungry!")
