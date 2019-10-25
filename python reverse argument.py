from functools import wraps

def reversed_args(f):
    @wraps(f)
    def g(*args):
        return f(*args[::-1])
    return g
