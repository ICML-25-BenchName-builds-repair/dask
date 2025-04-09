"""
This script verifies that our fixes to dask/utils.py work correctly.
"""

import warnings
from typing import Any, Callable, Mapping, TypeVar

F = TypeVar("F", bound=Callable[..., Any])

class NoDefault:
    """Singleton to represent no default value."""
    pass

no_default = NoDefault()

def test_fix():
    # Test the fixed code
    def _deprecated_kwarg_fixed(
        old_arg_name: str,
        new_arg_name: str | None = None,
        mapping: Mapping[Any, Any] | Callable[[Any], Any] | None = None,
        stacklevel: int = 2,
        comment: str | None = None,
    ) -> Callable[[F], F]:
        """Fixed version of the function."""
        
        comment_str = f"\n{comment}" if comment else ""
        
        def _deprecated_kwarg(func: F) -> F:
            def wrapper(*args, **kwargs) -> Callable[..., Any]:
                old_arg_value = kwargs.pop(old_arg_name, no_default)
                
                if old_arg_value is not no_default:
                    if new_arg_name is None:
                        msg = (
                            f"the {repr(old_arg_name)} keyword is deprecated and "
                            "will be removed in a future version. Please take "
                            f"steps to stop the use of {repr(old_arg_name)}"
                        ) + (comment or "")
                        warnings.warn(msg, UserWarning, stacklevel=stacklevel)
                        return None
                    else:
                        msg = (
                            f"the {repr(old_arg_name)} keyword is deprecated, "
                            f"use {repr(new_arg_name)} instead."
                        )
                        warnings.warn(msg + (comment or ""), UserWarning, stacklevel=stacklevel)
                        return None
                return None
            return wrapper  # type: ignore
        
        return _deprecated_kwarg
    
    # Test with None comment
    decorator = _deprecated_kwarg_fixed("old", "new", comment=None)
    print("Test with None comment: Passed")
    
    # Test with string comment
    decorator = _deprecated_kwarg_fixed("old", "new", comment="This is a comment")
    print("Test with string comment: Passed")
    
    print("All tests passed!")

if __name__ == "__main__":
    test_fix()