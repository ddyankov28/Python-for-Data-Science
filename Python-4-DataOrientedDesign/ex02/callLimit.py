def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            try:
                nonlocal count
                if count == limit:
                    raise Exception(f"{function} call too many times")
                else:
                    count += 1
                    return function(*args, **kwds)
            except Exception as e:
                print("Error: ", e)
        return limit_function
    return callLimiter

# NOTES
# - Wrapper is a piece of code that is used to modify or extend the
#       behavior of an existing function, method or class without
#       modifying its source code. Main purpose is to add some
#       additional functionality to the original code without
#       changing its core logic

# resources 
# - https://www.geeksforgeeks.org/function-wrappers-in-python/
