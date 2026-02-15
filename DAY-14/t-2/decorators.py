from functools import wraps

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Completed {func.__name__}")
        return result
    return wrapper
