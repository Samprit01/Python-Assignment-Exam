'''
Question 7: Daily Expense Tracker
A person records daily expenses in a list. 
Write a function to calculate the total expenses, average daily expense, 
and the days on which expenses exceeded ₹1,000.

'''



expense = [2000,500,7500,9000,6000,3500,1000]

def tracker(x):
    total_expense = sum(x)
    avg_expense = total_expense/len(x)
    exp_1000 = [_ for _ in x if _>1000]
    print(f"Total Expense: {total_expense}\nAverage Expense: {avg_expense} \nExpense exceeding 1000: {exp_1000}")



tracker(expense)