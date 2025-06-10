#!/usr/bin/env python3

# """
# This is a module level docstring
# Total docstrings in this file: 2
# Total classes: 1
# Total functions: 3
# Total variables: 5
# Total comments: 8
# Total keywords used: 12 (def, class, if, else, return, for, in, import, from, as, with, pass)
# Total identifiers: 8
# Total literals: 6
# """

# Importing required modules
import math
from typing import List, Dict

# Global variables
CONSTANT_VALUE = 100  # A numeric literal
message = "Hello, World!"  # A string literal
numbers = [1, 2, 3, 4, 5]  # A list literal

class TestClass:
    """
    This is a class docstring
    This class demonstrates various Python constructs
    """
    
    def __init__(self, name: str):
        self.name = name
        self.value = 42

    def calculate_something(self, x: int) -> float:
        # This is a calculation function
        result = math.sqrt(x) + CONSTANT_VALUE
        return result

    @staticmethod
    def process_list(items: List[int]) -> Dict[str, int]:
        output = {}
        for i, item in enumerate(items):
            if item % 2 == 0:
                output[f"even_{i}"] = item
            else:
                output[f"odd_{i}"] = item
        return output

# Function outside class
def main():
    test_obj = TestClass("parser_test")
    test_obj.calculate_something(16)
    TestClass.process_list(numbers)

if __name__ == "__main__":
    main() 