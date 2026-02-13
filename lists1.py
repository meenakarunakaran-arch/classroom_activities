"""
# List Operations in Python

# len(list)          -> Returns the length of the list
# max(list)          -> Returns the maximum value from the list
# min(list)          -> Returns the minimum value from the list

# list.append(obj)   -> Adds an object to the end of the list
# list.count(obj)    -> Returns how many times obj occurs in the list
# list.extend(seq)   -> Adds all elements of another sequence to the list

# list.index(obj)    -> Returns the lowest index where obj appears
# list.insert(i, obj)-> Inserts object at a specific index

# list.pop()         -> Removes and returns the last item (or given index)
# list.remove(obj)   -> Removes the first occurrence of obj from the list

# list.reverse()     -> Reverses the list in place
# list.sort()        -> Sorts the list in ascending order

"""
a = [1,2,3,4,5]
print(a)
print(len(a))
print(max(a))
print(min(a))
a.append(6)
print(a)
print(a.count(2))
a.extend([5,4,3])
print(a)
print(a.index(3))
a.insert(4,7)
print(a)
print(a.pop(5))
a.remove(6)
print(a)
a.reverse()
print(a)
a.sort()
print(a)