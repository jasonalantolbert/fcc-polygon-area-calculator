import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        """
        Sets the width of the rectangle.
        @param width: The width of the rectangle.
        """
        self.width = width

    def set_height(self, height):
        """
        Sets the height of the rectangle.
        @param height: The height of the rectangle.
        """
        self.height = height

    def get_area(self) -> int:
        """
        Gets the area of the rectangle.
        @return: An integer representing the area of the rectangle.
        """
        return self.width * self.height

    def get_perimeter(self) -> int:
        """
        Gets the perimeter of the rectangle.
        @return: An integer representing the perimeter of the rectangle.
        """
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self) -> float:
        """
        Gets the diagonal of the rectnalge.
        @return: An float representing the diagonal of the rectangle.
        """
        return math.sqrt((self.width ** 2) + (self.height ** 2))

    def get_picture(self) -> str:
        """
        Constructs a group of asterisks in the shape of the rectangle.
        @return: A string containing a group of asterisks in the shape of the rectangle.
        """
        if self.width <= 50 and self.height <= 50:
            picture = ""
            for i in range(self.height):
                picture += f"{f'*' * self.width}\n"
            return picture
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape) -> int:
        """
        Gets the number of times the passed-in shape can fit inside the shape used to call this method.
        @param shape: An instance of class Square or Rectangle.
        @return: An integer representing the number of times the passed-in shape can fit inside the shape
        used to call this method.
        """

        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
        """
        Sets the side length of the square.
        @param side: The side length of the square.
        """
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        """
        Sets the width and height of the square. Effecitvely identical to Square.set_side().
        @param width: The width of the square.
        """
        super().set_width(width)
        super().set_height(width)
        self.side = width

    def set_height(self, height):
        """
        Sets the width and height of the square. Effecitvely identical to Square.set_side().
        @param height: The width of the square.
        """
        super().set_height(height)
        super().set_width(height)
        self.side = height

    def __str__(self):
        return f"Square(side={self.side})"
