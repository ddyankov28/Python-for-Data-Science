def ft_statistics(*args: any, **kwargs: any) -> None:
    '''
    Takes *args a quantity of unknown number and makes the
    Mean, Median, Quartile (25% and 75%), Standard Deviation and
    Variance according to the **kwargs (Keyword Arguments)
    -------
    @param
        - *args: any -> unknow amount of numeric values
        - **kwargs: any -> unknown amount of keyword arguments
    -------
    @rtype
        - None
    -------
    @return
        - None
    ''' 
    print(args)
    print("----")
    print(kwargs)    

# NOTES:
# - If you don't know how many arguments that will be passed into a function
#   add a '*' before the parameter name in the function definition.
#   This way the function will receive a tuple of args and cann access
#   the items accordingly
# - You can also send arguments with the key = value syntax. This way
#   the order of the arguments does not matter



# resources
# - https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp
# - https://www.w3schools.com/python/python_ml_mean_median_mode.asp
