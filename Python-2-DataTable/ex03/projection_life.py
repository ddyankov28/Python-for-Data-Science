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
        dfIncome = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        dfLife = load("life_expectancy_years.csv")
        # print(dfIncome[["1900"]])
        # print("--------------------")
        # print(dfLife[["1900"]])
        income = [value for value in dfIncome["1900"]]
        print(income)
        life = [value for value in dfLife["1900"]]
        print(life)
        plt.scatter(income,life)
        plt.show()
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()