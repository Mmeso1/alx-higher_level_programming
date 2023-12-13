from models.rectangle import Rectangle

def is_function_documented(func):
    """Check if a function has a docstring."""
    return func.__doc__ is not None

# Create an instance of the Base class
base_instance = Rectangle(2, 3)

# Check if draw_rectangle is documented
if is_function_documented(base_instance.draw_square):
    print("draw_rectangle is documented.")
else:
    print("draw_rectangle is not documented.")
