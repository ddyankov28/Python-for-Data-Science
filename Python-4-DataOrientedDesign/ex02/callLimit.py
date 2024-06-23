def callLimit(limit: int):
    '''
    This is the main function that is acting like the home of the
    decorator and accepts an int limit that later will be checked
    how often the function passed will be called
    '''
    count = 0

    def callLimiter(function):
        '''
        The actual decorator function. Returns a new function that
        wraps the function passed as an argument
        '''
        def limit_function(*args: any, **kwds: any):
            '''
            The actual function to check how often the function passed
            was called. Raises exception if the count exceeds the limit
            '''
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
