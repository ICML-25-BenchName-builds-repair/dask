"""
This script demonstrates the type error in dask/utils.py.
It shows the issue with string concatenation with potentially None values.
"""

def simulate_error():
    # Simulate the error in dask/utils.py
    comment = None
    
    try:
        # This will raise a TypeError because you can't concatenate str and None
        msg = "This is a message"
        result = msg + comment
        print(f"Result: {result}")
    except TypeError as e:
        print(f"Error: {e}")
    
    # Fix: Check if comment is None before concatenation
    comment = None
    msg = "This is a message"
    result = msg + (comment or "")
    print(f"Fixed result: {result}")
    
    # With a real comment
    comment = " with additional info"
    result = msg + (comment or "")
    print(f"With comment: {result}")

if __name__ == "__main__":
    simulate_error()