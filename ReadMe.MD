# Package Sorting Utility

## Introduction
This utility is designed to help automate the sorting of packages into different categories based on their size and weight. It categorizes packages into `STANDARD`, `SPECIAL`, and `REJECTED` stacks, facilitating efficient handling and processing.

## Features
- **Volume and Weight Calculation**: Automatically calculates the volume and weight of packages to determine their categories.
- **Category Sorting**: Sorts packages into `STANDARD`, `SPECIAL`, or `REJECTED` based on predefined criteria.
- **Input Validation**: Ensures all input values are positive integers or floats, enhancing reliability.

## Installation
This utility does not require installation if you are running it as a standalone Python script. Ensure you have Python 3.6 or later installed on your system.

If this utility is part of a larger package or application, please follow the specific installation instructions provided for that application.

## Usage
To use this utility, import the `sort` function from the script and pass the dimensions (width, height, length in centimeters) and mass (in kilograms) of the package to it.

### Example:

```python
from main import sort

# Example package details
width = 100
height = 100
length = 99
mass = 10

# Determine the category
category = sort(width, height, length, mass)
print(f"The package belongs to the '{category}' stack.")