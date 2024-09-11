class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rect = Rectangle(10, 20)
for attr in rect:
    print(attr)



#OUTPUT
{'length': 10}
{'width': 20}

#In this implementation, iterating over the Rectangle instance first returns the length, then the width in the desired format.