class Rectangle:
  """Represent a rectangle and it's associated attributes."""

  def __init__(self, width, height):
    """Initialize attributes to make a rectangle."""
    self.height = height
    self.width = width

  def __str__(self):
    """String representation of square."""
    output = (f"Rectangle(width={self.width}, height={self.height})")
    return output

  def set_width(self, width):
    """Set the width of the rectangle."""
    self.width = width
    
  def set_height(self, height):
    """Set the height of the rectangle."""
    self.height = height

  def get_area(self):
    """Return the area of the rectangle."""
    area = self.width * self.height
    return area

  def get_perimeter(self):
    """Returns the perimiter of the rectangle."""
    perimiter = 2 * self.width + 2 * self.height
    return perimiter

  def get_diagonal(self):
    """Return the diagonal of the rectangle."""
    diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
    return diagonal

  def get_picture(self):
    """Return a string that represents the shape using n lines."""
    picture = ''
    if self.width > 50 or self.height > 50:
      picture = "Too big for picture."
    else:
      for i in range(self.height):
        picture += "*" * self.width + '\n'
    return picture
  
  def get_amount_inside(self, shape):
    """Return number of times shape fits inside."""
    amount = 0
    if self.width >= shape.width and self.height >= shape.height:
      amount = int(self.get_area() / shape.get_area())
      return amount
    else:
      return amount
      

class Square(Rectangle):
  """Represent aspects of a rectangle, specific to a square."""

  def __init__(self, width):
    """Initialize attributes to make a square."""
    height = width
    super().__init__(width, height)

  def __str__(self):
    """String representation of square."""
    output = (f"Square(side={self.width})")
    return output

  def set_side(self, side):
    self.width = side
    self.height = side
