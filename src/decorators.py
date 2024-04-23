from functools import wraps
import datetime


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f'{timestamp} {func.__name__}'

            try:
                result = func(*args, **kwargs)
                log_message += 'ok \n'
            except Exception as e:
                log_message += f'error: {type(e).__name__}. Inputs: {args} {kwargs}\n'
                result = None

            if filename:
                with open(filename, 'a') as f:
                    f.write(log_message)
            else:
                print(log_message)

            return result
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)





