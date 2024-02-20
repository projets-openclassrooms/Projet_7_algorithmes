import csv


def read_stock_data(file_name):
    stocks = []
    with open("data/" + file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stocks.append({
                'name':row['name'],
                'price':row['price'],
                'profit':row['profit']
            })
    return stocks

def filtre_stocks(stocks):
    lignes_filtrees =[stock for stock in stocks if stock['price']>=0]

    return lignes_filtrees

def calculate_effective_cost(stock):
    return stock['price'] * stock['profit'] / 100

def knapsack(stocks, budget):

    n = len(stocks)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]


    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if stocks[i - 1]['price'] <= j:
                # dp[i][j] = max(dp[i - 1][j],
                #                dp[i - 1][j - int(stocks[i - 1]['price'])] + calculate_effective_cost(
                #                    stocks[i - 1]))
                dp[i][j] = max(dp[i - 1][j],
                               dp[i - 1][j - int(stocks[i - 1]['price'])] + stocks[i-i]['price']*stocks[i-i]['profit'])
            else:
                dp[i][j] = dp[i - 1][j]
    print(i)
    selected = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected.append(stocks[i - 1])
            j -= int(stocks[i - 1]['price'])

    return selected

def main():
    print("Veuillez choisir parmi les fichiers suivants:")
    print("1. phase1+P7.csv")
    print("2. dataset1_Python+P7.csv")
    print("3. dataset2_Python+P7.csv")

    file_choice = input("Entrez le numéro du fichier : ")
    file_mapping = {
        '1': 'phase1+P7.csv',
        '2': 'dataset1_Python+P7_filtre.csv',
        '3': 'dataset2_Python+P7_filtre.csv'
    }
    selected_file = file_mapping.get(file_choice)
    if selected_file:
        stocks = read_stock_data(selected_file)
        stocks = filtre_stocks(stocks)
        if stocks:
            print(f"Contenu du fichier {selected_file}:")
            for stock in stocks:
                print(stock)
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
