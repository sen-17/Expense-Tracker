from datetime import datetime

expenses = []
def main():
    try:
        while True:
            choice = menu()

            if choice == 1:
                add_expense()

            elif choice == 2:
                update_expense(expenses)
            
            elif choice == 3:
                delete_expenses(expenses)

            elif choice == 4:
                view_expenses(expenses)

            elif choice == 5:
                expense_summary(expenses)

            elif choice == 6:
                specific_month_summary(expenses)
            
            else:
                print("Invalid choice. Please select again.")

    except ValueError:
        print("Please input a real number")


def menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. Update Expense")
    print("3. Delete Expense")
    print("4. View Expense")
    print("5. Expense Summary")
    print("6. View Specific Month Expense Summary")
    print("0. Exit")

    return int(input("Which menu would you like to do? "))


def add_expense():
    try:
        print("\nInput the following instructions:")
        date_string = input("Date (MM-DD-YYYY): ")
        date = datetime.strptime(date_string, "%m-%d-%Y")
        description = input("Description: ")
        amount = float(input("Amount: "))

        expenses.append({
            "date": date, 
            "description": description,
            "amount": amount
            })
        print("Expenses added successfully!")

    except ValueError:
        print("Invalid input. Please follow the format correctly.")


def delete_expenses(expenses_list):
    try:
        index = int(input("Enter the ID to delete: ")) - 1
        if 0 <= index < len(expenses_list):
            removed = expenses_list.pop(index)
            print("Deleted:", removed) 
        else:
            print("Invalid ID.")
    except ValueError:
        print("Please enter a valid number.")


def view_expenses(expenses_list):
    if not expenses_list:
        print("No expenses recorded.")
        return 
    
    print("\nID | Date      | Description   | Amount ")
    print("------------------------------------------")

    for i, exp in enumerate(expenses_list , 1):
        print(f"{i:<3} | {exp['date'].strftime('%m-%d-%Y')} | {exp['description']:<17} | ${exp['amount']:.2f}")

def expense_summary(expenses_list):
    total = sum(exp['amount'] for exp in expenses_list)
    print(f"\n Your total expenses: ${total:.2f}")

def update_expense(expenses_list):
    view_expenses(expenses_list)
    try:
        index = int(input("Enter the ID to update: ")) - 1
        if 0 <= index < len(expenses_list):
            print("Leave blank to keep current value.")
            date_string = input("New date (MM-DD-YYYY): ")
            description = input("New description: ")
            amount = input("New amount: ")

            if date_string:
                expenses_list[index]["date"] = datetime.strptime(date_string, "%m-%d-%Y")
            if description:
                expenses_list[index]["description"] = description
            if amount:
                expenses_list[index]["amount"]= float(amount)

            print("Expense updated.")
        else:
            print("Invalid ID.")        
    except ValueError:
            print("Invalid input.")

def specific_month_summary(expenses_list):
    month = input("Enter month number (e.g., 06 for June): ")
    year = input("Enter year(e.g., 2025): ")
    total = 0.0
    print("\n Expenses for that month: ")

    for exp in expenses_list:
        if exp["date"].strftime("%m") == month and exp["date"].strftime("%Y") == year:
            print(f"- {exp['date'].strftime('%m-%d-%Y')}: {exp['description']} - ${exp['amount']}")
            total += exp['amount']
        
    print(f"\n Total for {month}/{year}: ${total:.2f}")

if __name__ == "__main__":
    main()





    

    







    

        


    