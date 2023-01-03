friends = ["Monica", "Chandler", "Joey", "Phoebe"]


class Lst(list):
    def insert(self, index, element=None):
        if not element:
            element, index = index, 0
        super().insert(index, element)


friends = Lst(friends)
friends.insert("Ross")
print(friends)
friends.insert(2, "Rachel")
print(friends)
