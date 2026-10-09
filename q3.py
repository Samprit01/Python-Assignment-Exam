'''
A customer adds products to a shopping cart. 
Write a function that accepts a list of product names and 
performs the following operations:
•	Add a new product.
•	Remove a purchased or unwanted product.
•	Display the final cart.
•	Count the total number of products.

'''
cart = ['']


def add_prod(a:str):
    cart.append(a)

def rem_prod(a:str):
    cart.remove(a)

def disp():
    print([_ for _ in cart])

