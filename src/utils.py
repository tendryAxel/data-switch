def printer(f: classmethod):
    name_about = f.__qualname__

    def function(*args, **kwargs):
        print(f"Start to {name_about}")
        result = f(*args, **kwargs)
        print(f"Finish to {name_about}")
        return result

    return function
