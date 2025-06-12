"""
Total elements in this code:
- Keywords: 6 (class, def, if, return, __main__, __init__)
- Identifiers: 8 (MyClass, my_func, print, obj, var1, var2, local_var, self)
- Literals: 3 (10, 20, 30)
- Comments: 2
- Variables: 4 (var1, var2, local_var, obj)
- Classes: 1 (MyClass)
- Functions: 2 (__init__, my_func)
- Docstrings: 2 (module, class)
"""

"""Module docstring."""

class MyClass:  # Class
    """Class docstring."""

    def __init__(self):  # Function 1
        self.var1 = 10  # Variable 1 (instance)
        self.var2 = 20  # Variable 2 (instance)

def my_func():  # Function 2
    local_var = 30  # Variable 3 (local)
    return local_var

# Single-line comment 1
# Single-line comment 2

if __name__ == "__main__":  # Keywords (if, __main__)
    obj = MyClass()  # Literals (10, 20)
    print(my_func())  # Identifiers (print, my_func)