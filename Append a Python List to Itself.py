# We have a list of integers, and we want to double it
# in Python by duplicating its contents.
lst = [1, 2, 3]

# The first solution that may come to mind for a novice
# or inexperienced programmer is to use the append method.
lst.append(lst)
print(lst)  # [1, 2, 3, [...]]
# At the end of the list, we get [...]. What is it?

# Can we access the new element of the list using the 3rd index?
print(lst[3])  # [1, 2, 3, [...]]

# Weird, we get the same list. Let's try going deeper
# and getting the 3rd element of the 3rd element of the list, and so on.
print(lst[3][3][3][3][3][3][3][3][3][3][3][3])  # [1, 2, 3, [...]]

# We still get the same list. Maybe we can try accessing the last element of the list instead.
print(lst[-1])  # [1, 2, 3, [...]]

# Or the last element of the last element of the list, and so on.
print(lst[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1])  # [1, 2, 3, [...]]

# How many elements are in the list?
print(len(lst))  # 4

# What happens if we add the list to itself again?
lst.append(lst)
print(lst)  # [1, 2, 3, [...], [...]]

# Now at the end of the list, we have two [...].
# Can we access the last element or the second to last element of the list?
print(lst[-1], lst[-2])  # [1, 2, 3, [...], [...]] [1, 2, 3, [...], [...]]

# We get the same list twice. Can we remove the last element of the list?
lst.pop(-1)
print(lst)  # [1, 2, 3, [...]]

# So maybe we can remove the second element inside of the list [...] ?
lst[-1].pop(1)
print(lst)  # [1, 3, [...]]

# Wow! We lost the second element of the main list. How many elements are in the list now?
print(len(lst))  # 3

# can we change the second element of the main list?
lst[1] = 100
print(lst)  # [1, 100, [...]]

# We can! So maybe we can change the second element inside the list [...]?
lst[-1][1] = 200
print(lst)  # [1, 200, [...]]


# Now we can be confident that[...] is not a list, but a reference to the main list.
# If we get the id of the main list and the id of the list referenced by the last element
# of the main list, we will see that they are the same.
print(id(lst), id(lst[-1]))  # 1975548556608 1975548556608
print(id(lst[1]), id(lst[-1][1]))  # 1975542768272 1975542768272

# Can we append the main list to the list referenced by the last element of the main list, creating nested lists?
lst[2].append([lst])
lst[3][0].append([lst])
lst[4][0].append([lst])
print(lst)  # [1, 200, [...], [[...]], [[...]], [[...]]]

lst[-1][0][-1][0][-1][0][-1][0][-1][0][0] = 300
print(lst)  # [300, 200, [...], [[...]], [[...]], [[...]]]

# Can we reverse the order of the elements in the list?
lst.reverse()
print(lst)  # [[[...]], [[...]], [[...]], [...], 200, 300]

# Can we insert the value 500 at the beginning of the list?
lst.insert(0, 500)
print(lst)

# Can we multiply the second element of the list by 5
print(lst[1]*5)

# How many elements are in the list now?
print(len(lst))  # 7

# There are only 7 elements.

# What happens if we square each element of the list if the element is even?
# print("square", [x*2 for x in lst if x % 2 == 0])
# TypeError: unsupported operand type(s) for %: 'list' and 'int'

# We get an error because we have a list inside the list
# and we can't multiply a list by an integer.

# Is there a solution to double the list without referencing the main list?
# We can fix the append method, as we did in the previous video, by overriding the append method.


class Lst(list):
    def append(self, element):
        if element is self:
            element *= 2


lst = Lst([1, 2, 3])
print(lst)
lst.append(lst)
print(lst)  # [1, 2, 3, 1, 2, 3]

# It works. Can we append other values to the list using this method?

lst.append(4)
print(lst)  # [1, 2, 3, 1, 2, 3]
# No, we can't. This is because we have overridden the append method
# and have not called the append method of the list class.


class Lst(list):
    def append(self, element):
        if element is self:
            element *= 2
        else:
            super().append(element)


lst = Lst([1, 2, 3])
lst.append(lst)  # [1, 2, 3, 1, 2, 3]
lst.append(4)  # [1, 2, 3, 1, 2, 3, 4]
lst += [9, 8, 7]  # [1, 2, 3, 1, 2, 3, 4, 9, 8, 7]

# It's working now, but do we really need to override the append method?
# Is there a better way to do this?

# Yes, we can use the extend method instead.
lst = [2, 0]
lst.extend(lst)
print(lst)  # [2, 0, 2, 0]

# We can also use the multiplication operator.
lst = lst * 2
print(lst)  # [2, 0, 2, 0, 2, 0, 2, 0]

# We can use the addition operator.
lst = lst + lst
print(lst)  # [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]

# As a bonus, we can use a list comprehension, but we get a slightly different result
lst = [x for x in lst for _ in range(2)]
# [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0]
print(lst)


# We sometimes want the duplicated list to be nested within the original list.
lst = [1, 2, 3]
# We can use [:] to create a copy of the original list
lst.append(lst[:])
print(lst)  # [1, 2, 3, [1, 2, 3]]

# The second method
lst = [1, 2, 3]
lst = lst + [lst]
print(lst)  # [1, 2, 3, [1, 2, 3]]

# The third method is to use a list comprehension
lst = [1, 2, 3]
lst.append([x for x in lst])
print(lst)  # [1, 2, 3, [1, 2, 3]]
