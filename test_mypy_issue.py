from typing import Optional

def test_function(comment: Optional[str] = None):
    # This will cause a mypy error
    msg = "Base message"
    result = msg + comment
    print(result)

if __name__ == "__main__":
    # This will work at runtime if comment is not None
    test_function("with comment")
    
    # This will fail at runtime if comment is None
    try:
        test_function(None)
    except TypeError as e:
        print(f"Error: {e}")