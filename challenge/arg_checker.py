import functools

def arg_checker(*arg_types):
    '''An argument checker decorator that checks both:
        - The number of variables that you use for a function
        - The type of each variable.
       Raises a TypeError if either of these fail''' 
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            if len(args) != len(arg_types):
                raise TypeError("Function requires exactly 3 arguments")
            
            if not all(isinstance(arg, arg_type) for arg, arg_type in zip(args, arg_types)):
                raise TypeError("Function arguments do not match specified types")

            return func(*args)
        return wrapper
    return decorator