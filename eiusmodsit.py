try:
    # Some code that may raise KeyError or IndexError
    my_dict = {'a': 1, 'b': 2}
    value = my_dict['c']  # Raises KeyError
except (KeyError, IndexError):
    print("An error occurred while accessing the dictionary or list.")
    # Handle the exception here
