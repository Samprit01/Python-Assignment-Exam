'''

Question 2: Online Mobile Store
An online store maintains a list of mobile prices. 
Write a function to display all mobiles costing more than 
₹20,000, calculate the total inventory value, and 
find the most expensive mobile price.

'''


def mobile_inventory(x):
    expensive_mob = max(x)
    total_inventory = sum(x)
    mobile20k = [_ for _ in x if _>20000]
    print(f"Expensive mobile: {expensive_mob} \nTotal Inventory price: {total_inventory} \nMobile>20000: {mobile20k}")

price = {30000,25000,65000,10000,9000,26000}
mobile_inventory(price)