import matplotlib.pyplot as plt
from load_csv import load


def convert_str_float(values: list) -> None:
    """Converts all strings (example : "10M") in float"""

    for i, n in enumerate(values):
        if isinstance(n, str) and n.endswith("M"):
            values[i] = float(n[:-1]) * 1_000_000


def main() -> int:
    """Retrieves infos from CSV file and creates a graph with it"""

    # DataFrame management
    df = load("population_total.csv")
    if df is None:
        print("Error loading CSV file")
        return 1
    df_country_1 = df[df["country"] == "Belgium"]
    df_country_2 = df[df["country"] == "France"]
    years_1 = list(map(int, df_country_1.columns[1:]))  # Converts years in int
    years_2 = list(map(int, df_country_2.columns[1:]))
    values_1 = list(df_country_1.iloc[0, 1:].values)
    values_2 = list(df_country_2.iloc[0, 1:].values)
    convert_str_float(values_1)
    convert_str_float(values_2)

    # pyplot management
    plt.plot(years_1, values_1, label="Belgium")  # Init graph with values
    plt.plot(years_2, values_2, label="France", color="green")
    plt.legend(loc="lower right")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.xticks(range(1800, 2050, 40))
    plt.xlim(1800, 2050)
    plt.ylabel("Population")
    plt.yticks(range(0, 80_000_000, 20_000_000),
               labels=[" ", "20M", "40M", "60M"])
    plt.show()

    return 0


if __name__ == "__main__":
    main()
