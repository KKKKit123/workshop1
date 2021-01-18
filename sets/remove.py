# EXAMPLE 1
thislist = {"apple", "banana", "cherry"}
thislist.remove("banana")
print(thislist)  # Output: { 'apple', 'cherry }

# EXAMPLE 2
thislist = {"apple", "banana", "cherry"}
thislist.discard("banana")
print(thislist)  # Output: [ 'cherry', 'apple']

# EXAMPLE 3
thislist = {"apple", "banana", "cherry"}
thislist.pop()
print(thislist)  # Output: [ 'cherry', 'banana']

# EXAMPLE 4
thislist = {"apple", "banana", "cherry"}
thislist.clear()
print(thislist)  # Output: set()