from models.rectangle import Rectangle

def get_undocumented_functions(cls):
    """Get a list of functions in a class that are not documented."""
    undocumented_functions = []
    for name, value in vars(cls).items():
        if callable(value) and not name.startswith("__") and value.__doc__ is None:
            undocumented_functions.append(name)
    return undocumented_functions

undocumented_functions = get_undocumented_functions(Rectangle)

if not undocumented_functions:
    print("All functions in Rectangle are documented.")
else:
    print("Undocumented functions in Rectangle:", undocumented_functions)
