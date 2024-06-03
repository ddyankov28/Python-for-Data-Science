from load_csv import load
import matplotlib.pyplot as plt
import numpy as np

def convertToMillion(population: np.array) -> np.array:
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
    return np.array(newPopulation)


def main():
    dataFrame = load("population_total.csv")
    dataFrameAustria = dataFrame[dataFrame["country"] == "Austria"]
    austriaY = dataFrameAustria.loc[dataFrameAustria.index[0]]
    x = dataFrameAustria.columns
    stopIndex = list(x).index("2050") + 1
    x = np.array(x[1:stopIndex])
    austriaY = np.array(austriaY[1:stopIndex])
    austriaY = convertToMillion(austriaY)
    toCompare = input("Enter a country to compare with Austria: ")
    dataFrametoCompare = dataFrame[dataFrame["country"] == toCompare]
    toCompareY = dataFrametoCompare.loc[dataFrametoCompare.index[0]]
    toCompareY = np.array(toCompareY[1:stopIndex])
    toCompareY = convertToMillion(toCompareY)
    
    plt.plot(x, toCompareY, label=toCompare)
    plt.plot(x, austriaY, label="Austria")
    plt.title("Population Projections")
    plt.ylabel("Population")
    plt.xticks(x[::40])
    plt.xlabel("Year")
    plt.ylim(0,1500)
    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    main()
