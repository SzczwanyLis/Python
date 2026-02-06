import inspect
from functools import wraps

def Parametr(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        params_info = {name: type(value).__name__ for name, value in bound_args.arguments.items()}
        
        print(f"{params_info}")
        return func(*args, **kwargs)
    return wrapper

@Parametr
def przyklad(a, b, c):
    pass
przyklad(a=5.23, b="hehe",c=3 )