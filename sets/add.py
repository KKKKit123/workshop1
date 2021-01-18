# EXAMPLE 1
thislist = {"apple", "banana", "cherry"}
thislist.add("orange")
print(thislist)  # Output: {'cherry', 'apple', 'banana', 'orange'}

# EXAMPLE 2
thislist = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thislist.update(tropical)
print(thislist)  # Output: {'mango', 'pineapple', 'apple', 'papaya', 'cherry', 'banana'}