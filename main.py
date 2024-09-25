def sort(width, height, length, mass):
    # Check if the arguments are of the expected type and greater than zero
    if not all(isinstance(arg, (int, float)) and arg > 0 for arg in [width, height, length, mass]):
        raise ValueError("All arguments must be positive integers or floats.")
    
    # Calculate the volume of the package
    volume = width * height * length
    
    # Determine if the package is bulky
    is_bulky = volume >= 10^6 or width >= 150 or height >= 150 or length >= 150
    
    # Determine if the package is heavy
    is_heavy = mass >= 20
    
    # Sort the package based on the criteria
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

if __name__ == "__main__":
    # Example usage with correct argument types and positive values:
    try:
        print(sort(1, 1, 1, 1))  # Should return "STANDARD"
        print(sort(100, 100, 100, 10))  # Should return "SPECIAL"
        print(sort(150, 100, 100, 10))  # Should return "SPECIAL"
        print(sort(100, 100, 100, 20))  # Should return "REJECTED"
        print(sort(150, 150, 150, 20))  # Should return "REJECTED"
    except ValueError as e:
        print(e)

    # Example usage with incorrect argument types or non-positive values:
    try:
        print(sort("100", -100, 100, 10))  # This will raise a ValueError
    except ValueError as e:
        print(e)


    try:
        print(sort(100, 100, 100, 0))  # This will raise a ValueError
    except ValueError as e:
        print(e)