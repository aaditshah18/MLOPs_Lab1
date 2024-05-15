def add(x, y):
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        return ValueError("Both inputs must be ints or floats")
    
    return x + y


def subtract(x, y):
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        return ValueError("Both inputs must be ints or floats")
    
    return x - y


def multiply(x, y):
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        return ValueError("Both inputs must be ints or floats")
    
    return x * y

def divide(x, y):
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        return ValueError("Both inputs must be ints or floats")
    
    return x / y