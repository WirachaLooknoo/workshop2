Python Lists

#Access List items
thislist = ["apple", "banana",  "cherry"]

print(thislist[0])  # Output: apple
print(thislist[1])  # Output: banana
print(thislist[2]) # Output: cherry

print(thislist[-1])  # Output: cherry
print(thislist[-2])	# Output: banana
print(thislist[-3])	# Output: apple

print(thislist[1:])	# Output: ['banana' ,  'cherry']
------------------------------------------------
#Change item Value
thislist  =  ["apple", "banana",  "cherry"]
thislist [1]  = "watermelon"

print(thislist) # Output:  ["apple", "watermelon",  "cherry" ]
------------------------------------------------
#Add List Items
#EXAMPLE 1
thislist = ["apple",  "banana",  "cherry" ]
thislist.append("orange")

print(thislist)  # Output: ['apple', 'banana', 'cherry', 'orenge' ]

#EXAMPLE 2
thislist = ["apple",  "banana",  "cherry" ]
thislist.insert(1, "orange")
print(thislist)    # Output: ['apple', 'orenge', 'banana', 'cherry' ]
----------------------------------------------------
#Remove List Items
# EXAMPLE 1
thislist = ["apple",  "banana",  "cherry" ]
thislist.remove("banana")
print(thislist)  # Output: ['apple',  'cherry' ]

# EXAMPLE 2
thislist = ["apple",  "banana",  "cherry" ]
thislist.pop(1)
print(thislist)  # Output: ['apple',  'cherry' ]

# EXAMPLE 3
thislist = ["apple",  "banana",  "cherry" ]
thislist.pop()
print(thislist)  # Output: ['apple',  'banana' ]

# EXAMPLE 4
thislist = ["apple",  "banana",  "cherry" ]
del thislist[0]
print(thislist)  # Output: ['banana',  'cherry' ]

# EXAMPLE 4
thislist = ["apple",  "banana",  "cherry" ]
thislist.clear()
print(thislist)  # Output: [ ]
-----------------------------------------
#Sort List
# EXAMPLE 1
thislist = [100,  50,  65,  82,  23]
thislist.sort()
print(thislist)  # Output: [ 23,  50,  65,  82,  100]

# EXAMPLE 2
thislist = [100,  50,  65,  82,  23]
thislist.sort(reverse=True)
print(thislist)  # Output: [ 100,  82,  65,  50,  23]
---------------------------------------------
#Join List
list1 = [1,  2,  3]
list2 = [4,  5,  6]

list3  =  list1 +  list2

print(list3)  # Output: [1,  2,  3,  4,  5,  6]
-----------------------------------------------
#Loop List
fruit_list  = ["apple",  "banana",  "cherry" ]
for  fruit  in  fruit_list:
	print(fruit)

# Output:
#  apple
#  banana
#  cherry
