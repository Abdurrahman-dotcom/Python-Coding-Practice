print("Welcome to the Daily Expense Tracker!")
def output():
    print('')
    print("Menu:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total and average expense")
    print("4. Clear all expenses")
    print("5. Exit")
output()
total_expenses = 0 
expense = []
while True:
    num = int(input())
    if num == 1:
        f_num = float(input())
        expense.append(f_num)
        total_expenses+= f_num
        print('Expense added successfully!')
    elif num == 2:
        if not expense:
            print("No expenses recorded yet.")
        else:
            print('Your expenses:')
            for x in range(len((expense))):
                print(f'{x+1}. {expense[x]}')
    elif num == 3:

        if not expense:
            print("No expenses recorded yet.")
        else:
            print(f'Total expense: {total_expenses}')
            print(f'Average expense: {total_expenses/len(expense)}')     
    elif num == 4:
        expense.clear()  
        total_expenses = 0  
        print('All expenses cleared.')
    elif num == 5:
        print('Exiting the Daily Expense Tracker. Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.')