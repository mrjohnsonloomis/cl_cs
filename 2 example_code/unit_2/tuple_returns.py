from math import pi

def calculate_circle_properties(radius):
    """
    Calculates multiple properties of a circle and returns them as a tuple.
    This demonstrates how a single function can return multiple related values.
    
    Arguments:
        radius (float): The radius of the circle
        
    Returns:
        tuple: (circumference, area, diameter)
    """
    
    
    # Calculate different properties
    circumference = 2 * pi * radius
    area = pi * radius ** 2
    diameter = 2 * radius
    
    # Return multiple values as a tuple
    return circumference, area, diameter  # Python automatically packs these into a tuple

def main():
    # Basic tuple unpacking
    #radius = 78
    circ, area, diam = calculate_circle_properties(78)
    
    # Print individual values
    print(f"For a circle with radius {78}:")
    print(f"Circumference: {circ:.2f}")
    print(f"Area: {area:.2f}")
    print(f"Diameter: {diam:.2f}")
    
    # Alternative: receive as a single tuple
    print("\nDemonstrating alternate tuple handling:")
    circle_data = calculate_circle_properties(78)
    print(f"Raw tuple: {circle_data}")
    print(f"Accessing by index: {circle_data[0]:.2f}")


main()