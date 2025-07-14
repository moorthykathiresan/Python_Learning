###########################################################################
#############           String Interpolation              #################
###########################################################################

name = "Kathir"

print(f"Hello, {name}")

###########################################################################

interpolation = f"Hello, {name}"

print(interpolation)

###########################################################################

formatted = "Hello, {}"

formatted = formatted.format(name)

print(formatted)

item = "book"
price = 19.99
order = "I want to buy a {} for {:.2f} dollars.".format(item, price)
print(order)

###########################################################################
#################           String Utilities              ################# 
###########################################################################

print(formatted.upper())
print(formatted.lower())
print(formatted.replace("Hello", "Hi"))
print(formatted.replace("Notmatched", "NotReplaced"))

###########################################################################