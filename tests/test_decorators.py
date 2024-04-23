import pytest

from src.decorators import log


@log()
def test_function_success() -> str:
    return "success"


@log(filename="test_log.txt")
def test_function_success_file() -> str:
    return "success"


@log()
def test_function_error() -> str:
    raise ValueError("Test error")


@log(filename="test_log.txt")
def test_function_error_file() -> str:
    raise ValueError("Test error")


if __name__ == "__main__":
    pytest.main()
    test_function_success()
    test_function_success_file()
    test_function_error()
    test_function_error_file()
