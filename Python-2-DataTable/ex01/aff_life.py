from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def main():
    try:
        dataFrame = load("life_expectancy_years.csv")
        dataFrameAustria = dataFrame[dataFrame["country"] == "Austria"]
        xArray = []
        y = dataFrameAustria.loc[9]
        for col in dataFrameAustria.columns:
            xArray.append(col)
        xArray1 = xArray[1:]
        x = np.array(xArray1)
        y = y[1:]
        yp = np.array(y, dtype=float)
        print(x)
        print(y)
        plt.plot(x, yp)
        plt.title("Austria Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()

    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
