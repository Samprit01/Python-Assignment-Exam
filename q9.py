'''
Question 9: Mobile Product Details
An electronics store stores mobile details in a tuple containing brand, 
model, price, and storage capacity. Write a function to display the details and 
check whether the mobile price is below
₹30,000.

'''






m_name = ("Samsung","s22",75000,128)


def mobile_print(x):
    brand,model,price,storage = x
    price_check = lambda x:x<30000
    print(f"Brand: {brand}")
    print(f"Model: {model}")
    print(f"Price: {price}")
    print(f"Storage: {storage}")
    print(f"Price less than 30000: {price_check(price)} ")

mobile_print(m_name)