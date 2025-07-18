# Geometry Toolkit
# Problem Statement: Develop a class ShapeCalculator to calculate areas. 
# If one argument is passed, treat it as a circle radius and calculate the area. 
# If two arguments are passed, treat them as length and width of a rectangle. 
# Implement a single method area() with default parameters to simulate overloading. 
# Ensure it returns appropriate outputs in each case.

class ShapeCalculator:
    # Method 1
    def area(self, *args):
        if len(args) == 1:
            radius = args[0]
            return 3.14 * radius * radius
        elif len(args) == 2:
            length, width = args
            return length * width
        else:
            raise ValueError("Invalid number of arguments")
    # Method 2
    def area1(self, radius=0, length=0, width=0):
        if radius:
            return 3.14 * radius * radius
        elif length and width:
            return length * width
        else:
            raise ValueError("Invalid arguments: Provide either radius or both length and width")

shape1 = ShapeCalculator()
circle = shape1.area(5)
rectangle = shape1.area(5, 10)
print(f"circle : {circle} rectangle : {rectangle} \n")

circle = shape1.area1(10)
rectangle = shape1.area1(length=10,width=10)
print(f"circle : {circle} rectangle : {rectangle} \n")

