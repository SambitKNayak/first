# class Point:        # capital P in Point ---> capital first letter --> pascal naming convention for class names
#     # functions:
#     def mov(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
# point1 = Point()  # creating an object of Point class and named it point1
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()
# point2.x = 1
# print(point2.x)
# point2.mov()
#
class Point:
    # functions:

    def __init__(self, x, y):  # constructor # initialize our object with x and y coordinates
        # self is the reference to our current object
        self.x = x
        self.y = y
    def mov(self):
        print("move")
    def draw(self):
        print("draw")


point = Point(10, 20)
print(f'{point.x}, {point.y}')
point.x = 11
print(point.x)

# 10, 20
# 11

class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f'{self.name} talks and hi ! im here')

sambit = Person("Sambit Nayak")
print(sambit.name)
sambit.talk()

# Sambit Nayak
# Sambit Nayak talks