from load_csv import load
import matplotlib.pyplot as plt


def main():
    '''
    Loads .CSV into a Pandas DataFrame and displays the country info
    The graph has its own title and a legen for each axis
    '''
    try:
        dataFrame = load("life_expectancy_years.csv")
        country = input("Enter a country: ")
        dataFrameCountry = dataFrame[dataFrame["country"] == country]
        y = dataFrameCountry.loc[dataFrameCountry.index[0]]
        x = dataFrameCountry.columns
        x = x[1:]
        y = y[1:]
        plt.plot(x, y)
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.xticks(x[::40])
        plt.show()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt by User")
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()

# resources
# - https://www.w3schools.com/python/matplotlib_pyplot.asp
# - https://mathworks.com/help/matlab/ref/xticks.html
