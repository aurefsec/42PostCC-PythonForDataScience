import matplotlib.pyplot as plt
from load_csv import load


def main() -> int:
    """Retrieves infos from CSV file and creates a scatter with it"""

    # DataFrame management
    df_1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_2 = load("life_expectancy_years.csv")
    if df_1 is None or df_2 is None:
        print("Error loading CSV file")
        return 1
    values_1 = df_1["1900"].values
    values_2 = df_2["1900"].values

    # pyplot management
    plt.scatter(values_1, values_2)  # scatter for points
    plt.title("1900")
    plt.ylabel("Life Expectancy")
    plt.yticks(range(20, 60, 5))
    plt.ylim(15, 55)
    plt.xlabel("Gross domestic product")
    plt.xscale("log")  # For the logarithmic scale
    plt.xticks((300, 1000, 10000), ["300", "1k", "10k"])
    plt.show()

    return 0


if __name__ == "__main__":
    main()
