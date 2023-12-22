class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        area = self.length * self.width
        return area

# Example usage:
if __name__ == "__main__":
    # Create a Rectangle object with length 5 and width 3
    my_rectangle = Rectangle(5, 3)

    # Calculate and print the area of the rectangle
    area_of_my_rectangle = my_rectangle.compute_area()
    print(f"The area of the rectangle is: {area_of_my_rectangle}")
