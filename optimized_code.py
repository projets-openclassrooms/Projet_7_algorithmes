import csv
from chrono import Timer


def read_stock_data(file_name):
    stocks = []
    with open(f"data/{file_name}", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            name = row["name"]

            price = float(row["price"])
            profit = float(row["profit"])
            if price > 0 and profit > 0:
                # Ignorer les valeurs négatives
                stocks.append(
                    {
                        "name": row["name"],
                        "price": int(float(row["price"]) * 100),
                        "profit": calculate_effective_cost(row),
                    }
                )
    return stocks


def calculate_effective_cost(stock):
    # print(stock['price'] * stock['profit'] / 100)
    price = float(stock["price"])
    percent = float(stock["profit"]) / 100
    return int(round(price * percent, 2) * 100)


def knapsack(stocks, budget):
    m = len(stocks)
    dp = [[0 for _ in range(budget + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, budget + 1):
            if stocks[i - 1]["price"] <= j:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - stocks[i - 1]["price"]] + stocks[i - 1]["profit"],
                )
            else:
                dp[i][j] = dp[i - 1][j]

    selected = []

    j = budget
    n = len(stocks)
    while j > 0 and n > 0:
        e = stocks[n - 1]

        if dp[n][j] == dp[n - 1][j - e["price"]] + e["profit"]:
            selected.append(e)
            j -= e["price"]
            # print(j)
        n -= 1

    return selected


def main():
    print("Veuillez choisir parmi les fichiers suivants:")
    print("1. phase1+P7.csv")
    print("2. dataset1_Python+P7.csv")
    print("3. dataset2_Python+P7.csv")

    file_choice = input("Entrez le numéro du fichier : ")
    file_mapping = {
        "1": "phase1+P7.csv",
        "2": "dataset1_Python+P7.csv",
        "3": "dataset2_Python+P7.csv",
    }
    selected_file = file_mapping.get(file_choice)
    # Demarrage application temps
    depart_chrono = Timer()
    depart_chrono.start()
    print("depart du chrono")
    # lecture du fichier
    stocks = read_stock_data(selected_file)
    # print(stocks)
    if stocks:
        selected_stocks = knapsack(stocks, 500 * 100)

        total_cost = sum(stock["price"] for stock in selected_stocks) / 100
        total_profit = sum(stock["profit"] for stock in selected_stocks) / 100
        # print(selected_stocks)
        print("\nActions sélectionnées:")
        for stock in selected_stocks:
            print(
                f"Nom: {stock['name']}, Coût: {stock['price']/100}, Profit: {stock['profit']/100}"
            )

        print(f"Coût total des actions sélectionnées: {total_cost}")
        print(f"Profit total: {total_profit}")
    else:
        print(f"Fichier {selected_file} vide ou incorrect.")
    print("=" * 25)
    depart_chrono.stop()
    temps_écoulé = depart_chrono.elapsed_time()
    print("Temps écoulé:", temps_écoulé, "secondes")


if __name__ == "__main__":
    main()
