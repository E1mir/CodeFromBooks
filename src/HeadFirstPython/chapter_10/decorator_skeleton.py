from functools import wraps


def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Code to execute BEFORE calling the decorated function.
        # 2. Call the decorated function
        return func(*args, **kwargs)

    # 3. Code used for executing decorating function
    return wrapper
