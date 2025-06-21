import logging
from functools import wraps

def log_call(func):
    @wraps(func)
    def fn(*args, **kwargs):
        arg_list = [repr(a) for a in args]
        kwarg_list = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        all_args = ", ".join(arg_list + kwarg_list)
        log_msg = f"Calling: {func.__name__}({all_args})"
        logging.info(log_msg)
        return func(*args, **kwargs)
    return fn
