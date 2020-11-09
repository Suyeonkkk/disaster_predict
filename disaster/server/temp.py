from math import pi

def area_ellipse(radius_x: float, radius_y: float) -> float:
    """
    Calculate the area of a ellipse

    >>> area_ellipse(10, 10)
    314.1592653589793
    >>> area_ellipse(10, 20)
    628.3185307179587
    >>> area_ellipse(-10, 20)
    Traceback (most recent call last):
        ...
    ValueError: area_ellipse() only accepts non-negative values
    >>> area_ellipse(10, -20)
    Traceback (most recent call last):
        ...
    ValueError: area_ellipse() only accepts non-negative values
    >>> area_ellipse(-10, -20)
    Traceback (most recent call last):
        ...
    ValueError: area_ellipse() only accepts non-negative values
    """
    if radius_x < 0 or radius_y < 0:
        raise ValueError("area_ellipse() only accepts non-negative values")
    return pi * radius_x * radius_y