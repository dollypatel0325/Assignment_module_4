import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        area = math.pi * (self.radius ** 2)
        return area

    def compute_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

# Example usage:
if __name__ == "__main__":
    # Create a Circle object with radius 4
    my_circle = Circle(4)

    # Calculate and print the area and perimeter of the circle
    area_of_my_circle = my_circle.compute_area()
    perimeter_of_my_circle = my_circle.compute_perimeter()

    print(f"The area of the circle is: {area_of_my_circle}")
    print(f"The perimeter of the circle is: {perimeter_of_my_circle}")
