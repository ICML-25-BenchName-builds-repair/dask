import warnings
from typing import Any, Callable, Mapping

from dask.utils import _deprecated_kwarg

# Test the _deprecated_kwarg function with None comment and no new_arg_name
def test_deprecated_kwarg_with_none_comment_no_new_arg():
    @_deprecated_kwarg(old_arg_name="old", new_arg_name=None, comment=None)
    def func(old=None):
        return old

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = func(old="value")
        assert len(w) == 1
        assert "deprecated" in str(w[0].message)
        assert result == "value"

# Test the _deprecated_kwarg function with None comment and with new_arg_name
def test_deprecated_kwarg_with_none_comment_with_new_arg():
    @_deprecated_kwarg(old_arg_name="old", new_arg_name="new", comment=None)
    def func(new=None):
        return new

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = func(old="value")
        assert len(w) == 1
        assert "deprecated" in str(w[0].message)
        assert result == "value"

# Test the _deprecated_kwarg function with string comment
def test_deprecated_kwarg_with_string_comment():
    @_deprecated_kwarg(old_arg_name="old", new_arg_name="new", comment=" Additional info.")
    def func(new=None):
        return new

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = func(old="value")
        assert len(w) == 1
        assert "deprecated" in str(w[0].message)
        assert "Additional info" in str(w[0].message)
        assert result == "value"

if __name__ == "__main__":
    test_deprecated_kwarg_with_none_comment_no_new_arg()
    test_deprecated_kwarg_with_none_comment_with_new_arg()
    test_deprecated_kwarg_with_string_comment()
    print("All tests passed!")