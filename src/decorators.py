import datetime
from functools import wraps
from typing import Any, Callable, Optional, Tuple


def log(filename: Optional[str] = None) -> Callable[[Callable], Callable]:
    """Декоратор для логгирования действий функции."""

    def decorator(func: Callable) -> Callable:
        """Обертка декоратора для функции."""

        @wraps(func)
        def wrapper(*args: Tuple[Any], **kwargs: Any) -> Any:
            """Внутренняя обертка для функции, выполняющая логирование."""
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"{timestamp} {func.__name__}"

            try:
                result = func(*args, **kwargs)
                log_message += " ok\n"
            except Exception as e:
                log_message += f" error: {type(e).__name__}. Inputs: {args} {kwargs}\n"
                result = None

            if filename:
                with open(filename, "a") as f:
                    f.write(log_message)
            else:
                print(log_message)

            return result

        return wrapper

    return decorator
