"""
Use the format() method to insert numbers into strings:
"""
age = 36
txt = "My name is Nobuyoshi, and I am {}"
print(txt.format(age))

print()

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
item_number = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,item_number,price))

print()

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
mysecond_order = "I want to pay {2} dollars for {0} pieces of item {1}"
print(mysecond_order.format(quantity,item_number,price))