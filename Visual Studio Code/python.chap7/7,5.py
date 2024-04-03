class Point:
    """
    A class representing a point in a two-dimensional space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """

    def __init__(self, x, y):
        """
        Initialize a new Point object.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        """
        self.x = float(x)
        self.y = float(y)

    def distance_to(self, other):
        """
        Calculate the Euclidean distance between this point and another point.

        Args:
            other (Point): The other Point object.

        Returns:
            float: The Euclidean distance between the two points.
        """
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance

    def move_by(self, dx, dy):
        """
        Move the point by a specified amount in the x and y directions.

        Args:
            dx (float): The amount to move in the x-direction.
            dy (float): The amount to move in the y-direction.
        """
        self.x += float(dx)
        self.y += float(dy)

    def __str__(self):
        """
        Get a string representation of the point.

        Returns:
            str: A string representation of the point in the format "(x, y)".
        """
        return f"({self.x}, {self.y})"
