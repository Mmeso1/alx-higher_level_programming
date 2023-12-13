from models.base import Base

def is_function_documented(func):
    """Check if a function has a docstring."""
    return func.__doc__ is not None

# Create an instance of the Base class
base_instance = Base()

# Check if draw_rectangle is documented
if is_function_documented(base_instance.draw_rectangle):
    print("draw_rectangle is documented.")
else:
    print("draw_rectangle is not documented.")
