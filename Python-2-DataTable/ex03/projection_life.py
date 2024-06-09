from load_csv import load
import matplotlib.pyplot as plt


def main():
    '''
    Loads the 2 files in the repo and displays the projection of life
    expectancy in relation to the gross national product of the year
    1900 for each country. The graph has a title, a legend for each
    axis and a legend for each graph
    '''
    try:
        income = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        dfIncome = load(income)
        dfLife = load("life_expectancy_years.csv")
        income = [value for value in dfIncome["1900"]]
        print(income)
        life = [value for value in dfLife["1900"]]
        print(life)
        plt.scatter(income, life)
        plt.title("1900")
        xTicks = ([0, 1000, 3000, 5000, 7000, 9000, 10000])
        xLabels = ["0", "1k", "3k", "5k", "7k", "9k", "10k"]
        plt.xticks(xTicks, xLabels)
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.show()
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
