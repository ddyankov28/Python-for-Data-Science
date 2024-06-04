from load_csv import load
import matplotlib.pyplot as plt


def checkInvalidChars(valueString: str) -> bool:
    '''
    Checks if a population Value is in correct format
    -------
    @param:
        - valueString: str -> the list item that holds the value
    -------
    @rtype:
        - bool
    -------
    @return:
        - TRUE if there is invalid char
        - FALSE if there is nothing wrong with the valueString
    '''
    allowedChars = list("0123456789.kMB")
    return any(char not in allowedChars for char in valueString)


def convertToMillion(population: list) -> list:
    '''
    Converts population value to a corresponding million value
    -------
    @param:
        - population: list -> the list that holds all the population values
    -------
    @rtype:
        - list
    -------
    @return:
        - New list containing only million Values
    '''
    for valueString in population:
        if checkInvalidChars(valueString):
            raise AssertionError("Wrong char in data")
    newPopulation = []
    for number in population:
        if 'k' in number:
            number = number[:-1]
            number = float(number) * 1000
            number = float(number) / 1000000
            number = f"{number:.2f}"
        elif 'M' in number:
            number = number[:-1]
        elif 'B' in number:
            number = number[:-1]
            number = float(number) * 1000
        else:
            number = float(number) / 1000000
            number = f"{number:.2f}"
        newPopulation.append(float(number))
    return newPopulation


def main():
    '''
    Loads .CSV into a Pandas DataFrame and displays Austria info versus
    other country of user choice. The graph has a title, a legend for
    each axis and a legend for each graph. Years displayed 1800 to 2050
    '''
    try:
        dataFrame = load("population_total.csv")
        xAxis = dataFrame.columns
        stopIndex = list(xAxis).index("2050") + 1
        xAxis = xAxis[1:stopIndex]

        dataFrameAustria = dataFrame[dataFrame["country"] == "Austria"]
        austriaY = dataFrameAustria.loc[dataFrameAustria.index[0]]
        austriaY = convertToMillion(austriaY[1:stopIndex])

        toCompare = input("Enter a country to compare with Austria: ")
        dataFrametoCompare = dataFrame[dataFrame["country"] == toCompare]
        toCompareY = dataFrametoCompare.loc[dataFrametoCompare.index[0]]
        toCompareY = toCompareY[1:stopIndex]
        toCompareY = convertToMillion(toCompareY)

        plt.plot(xAxis, toCompareY, label=toCompare)
        plt.plot(xAxis, austriaY, label="Austria", color="green")
        plt.title("Population Projections")
        plt.ylabel("Population")
        plt.xticks(xAxis[::40])
        plt.xlabel("Year")
        plt.legend(loc="lower right")

        yTicks = plt.gca().get_yticks()
        plt.yticks(yTicks[1:-1:2], [f"{tick:.0f}M" for tick in yTicks[1:-1:2]])
        plt.show()
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()

# resources
# - https://www.geeksforgeeks.org/matplotlib-pyplot-gca-in-python/
# - https://www.geeksforgeeks.org/matplotlib-pyplot-yticks-in-python/
# - https://www.w3schools.com/python/matplotlib_labels.asp
