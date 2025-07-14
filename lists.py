###########################################################################
#################           List Slices              ######################
###########################################################################

Fruits = ["Apple", "Orange", "Mango", "Kiwi"]
Prices = [10, 12, 20, 14]

# 0 based index

print(Fruits[2]) 
print(Prices[3])

# print(Fruits[4]) # Err. Index out of Range
# print(Prices[4]) # Err. Index out of Range
 
# Slice pattern [Start:Count:Step]

print("START")

print(Fruits[0:])
print(Fruits[1:])
print(Fruits[2:])
print(Fruits[3:])
print(Fruits[4:]) # Empty list. Not erring. However print(Fruits[4]) will throw error
print(Fruits[101:]) # Empty list. Not erring. print(Fruits[101]) will throw error

print("Count")

print(Fruits[:0]) # Empty list
print(Fruits[:1])
print(Fruits[:2])
print(Fruits[:3])
print(Fruits[:4])
print(Fruits[:5]) # Not error. Full list is printed
print(Fruits[:101]) # Not error. Full list is printed

print("STEP")

print(Fruits[::-2]) # STEPS by 2 in Backward from end of the list
print(Fruits[::-1]) # STEPS by 1 in Backward from end of the list
# print(Fruits[::0]) # This will Err. STEP Can not be 0
print(Fruits[::1])
print(Fruits[::2]) # Everyother
print(Fruits[::3])
print(Fruits[::4])
print(Fruits[::5])


print("START:COUNT:STEP")
# print(Fruits[0:0:0]) # This will Err. STEP Can not be 0
print(Fruits[0:1:1]) # Count is 1. So prints only Apple
print(Fruits[0:1:2]) # Count is 1. So prints only Apple
print(Fruits[0:1:3]) # Count is 1. So prints only Apple
print(Fruits[0:1:4]) # Count is 1. So prints only Apple
print(Fruits[0:1:5]) # Count is 1. So prints only Apple

print(Fruits[0:2:1])
print(Fruits[0:3:1])
print(Fruits[0:4:1])

# CHECK
print(Fruits[0:2:2])
print(Fruits[:2:2])
print(Fruits[0::2])

###########################################################################
#################           List Utilities              ###################
###########################################################################

print("---Sum, Min, Max---")
print(sum(Prices))
print(min(Prices))
print(max(Prices))

###########################################################################
#################           List Iteration              ###################
###########################################################################

print("---Fruits iterated---")
for fruit in Fruits:
    print(fruit)

print("---Fruits and prices iterated---")
for fruit, price in zip(Fruits, Prices):
    print(f"Fruit: {fruit}, Price: {price}")

print("---Fruits reversed---")
for fruit in reversed(Fruits):
    print(fruit)

print("---Range function---")
for i in range(6):
    print(i)

print("----Enumerate function---")
for i, fruit in enumerate(Fruits):
    print(f"Index: {i}, Fruit: {fruit}")
