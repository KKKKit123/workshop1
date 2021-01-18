# EX1
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set3 = set1.union(set2)
print(set3)  # Output: {'e', 'd', 'f', 'c', 'a', 'b'}

# EX2
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set1.update(set2)
print(set1)  # Output: {'f', 'b', 'a', 'c', 'd', 'e'}

# EX3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)  # Output: {'apple'}

# EX4
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)  # Output:{'google', 'microsoft', 'cherry', 'banana'}
