def calc_mean(args):
    '''
    Calculates and prints the mean (the average value) in a sequence
    of numbers. The sum of all values divided by the total number of values
    '''
    print(f"mean : {sum(args) / len(args):.1f}")


def calc_median(args, flag):
    '''
    Calculates and printsthe median (the middle number) in a sequence. If the
    sequence is even number takes the 2 midd numbers and divides their sum by 2
    '''
    args = list(args)
    args.sort()
    if (len(args) % 2 == 0):
        n1_index = int((len(args) + 1) / 2) - 1
        n2_index = n1_index + 1
        median = (args[n1_index] + args[n2_index]) / 2
    else:
        median = args[int((len(args)+ 1) / 2) - 1]
    if flag:
        print(f"median : {median}")
    return median

def calc_quartile(args):
    '''
    Calculates and prints the 25% Quartile and the 75% Quartile in a sequence
    of numbers.
    '''
    quartiles = []
    args = list(args)
    args.sort()
    if (len(args) % 2 == 0):
        lower_half_end = int((len(args)+ 1) / 2)
        lower_half = args[:lower_half_end]
        quartile_1 = calc_median(lower_half, 0)
        quartiles.append(quartile_1)
        upper_half_begin = lower_half_end
        upper_half = args[upper_half_begin:]
        quartile_2 = calc_median(upper_half, 0)
        quartiles.append(quartile_2)
        #print(args)
        #print(lower_half)
        #print(upper_half)
        print(f"quartile : {quartiles}")
    else:
        median = calc_median(args, 0)
        lower_half_end = args.index(median)
        lower_half = args[:lower_half_end]
        upper_half_begin = lower_half_end + 1
        upper_half = args[upper_half_begin:]
        quartile_1 = calc_median(lower_half, 0)
        quartiles.append(float(quartile_1))
        quartile_2 = calc_median(upper_half, 0)
        quartiles.append(float(quartile_2))
        #print(args)
        #print(lower_half)
        #print(upper_half)
        print(f"quartile : {quartiles}")


def calc_std(args, flag):
    '''
    Calculates and prints the Standard Deviation - the average
    distance from the mean value in q sequence of numbers
    '''
    mean = sum(args) / len(args)
    result = 0
    for num in args:
        result += pow((num - mean), 2)
    result /= len(args)
    standard_deviation = pow(result, 0.5)
    if flag:
        print(f"std : {standard_deviation}")
    return result


def calc_var(args):
    '''
    Calculates the variance. 
    '''
    variation = calc_std(args, 0)
    print(f"var : {variation}")

def calculate(value, args):
    '''
    Takes the stat value and the numbers that the
    stat should be performed on and goes into the corresponding
    function to finish the job
    -------
    @param
        - value -> The stat value string
        - args -> The numbers to perform the value on
    '''
    if value == "mean":
        calc_mean(args)
    elif value == "median":
        calc_median(args, 1)
    elif value == "quartile":
        calc_quartile(args)
    elif value == "std":
        calc_std(args, 1)
    else:
        calc_var(args)


def ft_statistics(*args: any, **kwargs: any) -> None:
    '''
    Takes *args a quantity of unknown number and makes the
    Mean, Median, Quartile (25% and 75%), Standard Deviation and
    Variance according to the **kwargs (Keyword Arguments)
    -------
    @param
        - *args: any -> unknown amount of numeric values
        - **kwargs: any -> unknown amount of keyword arguments
    '''
    try:    
        stats = ["mean", "median", "quartile", "std", "var"]
        for value in kwargs.values():
            if value not in stats:
                continue
            if len(args) == 0:
                print("ERROR")
                continue
            calculate(value, args)
    except Exception as e:
        print("Error: ", e)    
    
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
# - https://www.calculatorsoup.com/calculators/statistics/quartile-calculator.php
# - https://www.youtube.com/watch?v=esskJJF8pCc&ab_channel=DATAtab
