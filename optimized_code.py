import csv


def read_stock_data(file_name, scenario=None):
    stocks = []
    with open(f"data/{file_name}", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if 'name' in row and 'price' in row and 'profit' in row:
                price = float(row['price'])
                if scenario == "1":
                    if price < 0:
                        price = abs(price)
                elif scenario == "2":
                    if price < 0:
                        continue  # Ignorer les valeurs négatives
                elif price == 0:  # Si le prix est nul, assigner une valeur très petite
                    price = 0.00001
                stocks.append({
                    'name': row['name'],
                    'price': price,
                    'profit': float(row['profit'])
                })
            else:
                print(f"Erreur: ligne invalide dans le fichier {file_name}")
    return stocks


def calculate_effective_cost(stock):
    # print(stock['price'] * stock['profit'] / 100)
    return int(stock['price'] * stock['profit'] / 100)


def knapsack(stocks, budget):
    n = len(stocks)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if stocks[i - 1]['price'] <= j:
                dp[i][j] = max(dp[i - 1][j],
                               dp[i - 1][j - int(stocks[i - 1]['price'])] + calculate_effective_cost(stocks[i - 1]))
            else:
                dp[i][j] = dp[i - 1][j]

    selected = []

    j = budget

    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected.append(stocks[i - 1])
            j -= int(stocks[i - 1]['price'])
            # print(j)


    # for stock in selected:
    #     budget-= stock['price']
    #     # print(budget)

    return selected


def main():
    print("Veuillez choisir parmi les fichiers suivants:")
    print("1. phase1+P7.csv")
    print("2. dataset1_Python+P7.csv")
    print("3. dataset2_Python+P7.csv")

    file_choice = input("Entrez le numéro du fichier : ")
    file_mapping = {
        '1': 'phase1+P7.csv',
        '2': 'dataset1_Python+P7.csv',
        '3': 'dataset2_Python+P7.csv'
    }
    selected_file = file_mapping.get(file_choice)
    print("1. scenario 1")
    print("2. scenario 2")
    if selected_file:
        scenario_choice = input("Choisissez un scénario (scenario 1 / scenario 2) : ")
        stocks = read_stock_data(selected_file, scenario_choice)
        if stocks:
            # print(f"Contenu du fichier {selected_file}:")
            # for stock in stocks:
            #     print(stock['name'])
            selected_stocks = knapsack(stocks, 500)

            total_cost = sum(stock['price'] for stock in selected_stocks)
            total_profit = sum(calculate_effective_cost(stock) for stock in selected_stocks)

            print("\nActions sélectionnées:")
            for stock in selected_stocks:
                print(f"Nom: {stock['name']}, Coût: {stock['price']}, Profit: {stock['profit']}%")

            print(f"Coût total des actions sélectionnées: {total_cost}")
            print(f"Profit total: {total_profit}")
        else:
            print(f"Fichier {selected_file} vide ou incorrect.")
    else:
        print("Choix de fichier invalide.")


if __name__ == "__main__":
    main()
