import matplotlib.pyplot as plt
from load_csv import load


def main() -> int:
    """Retrieves infos from CSV file and creates a graph with it"""

    # DataFrame management
    df = load("life_expectancy_years.csv")
    if df is None:
        print("Error loading CSV file")
        return 1
    df_country = df[df["country"] == "France"]
    years = list(map(int, df_country.columns[1:]))  # Converts years in int
    values = df_country.iloc[0, 1:].values  # iloc to interpret [0, 1:]

    # pyplot management
    plt.plot(years, values)  # Init graph with values
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks([year for year in years if year % 40 == 0])
    plt.show()

    return 0


if __name__ == "__main__":
    main()
