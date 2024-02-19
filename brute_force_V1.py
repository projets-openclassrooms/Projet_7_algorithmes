import csv
import itertools

from chrono import Timer


def lire_actions_de_csv(nom_fichier):
    actions = []

    with open(nom_fichier, newline='') as fichier_csv:
        lecteur_csv = csv.DictReader(fichier_csv, delimiter=',')

        for row in lecteur_csv:
            nom = row["name"]
            cout = float(row["price"])

            benefice = float(row["profit"])
            actions.append({"nom": nom, "price": cout, "profit": benefice})

    return actions


def bruteforce(actions, budget):
    best_combination = None
    max_profit = 0

    # Générer toutes les combinaisons possibles d'actions d'un tableau avec iterations
    for combination in itertools.product([0, 1], repeat=len(actions)):
        total_cost = sum(action["price"] for action, include in zip(actions, combination) if include)
        if total_cost <= budget:
            total_profit = sum(
                action["profit"] * action["price"] for action, include in zip(actions, combination) if include)
            if total_profit > max_profit:
                max_profit = total_profit
                best_combination = combination

    return best_combination, max_profit


# Demarrage application
depart_chrono = Timer()
depart_chrono.start()
print("depart du chrono")
nom_fichier_csv = "data/dataset2_Python+P7.csv"
actions = lire_actions_de_csv(nom_fichier_csv)

# print(actions)

budget = 500
best_combination, max_profit = bruteforce(actions, budget)

print("Meilleure combinaison d'actions pour maximiser le profit avec un budget de", budget, "euros:")
print("=" * 25)
print("{:<13} {:<4}".format("Nom Action", "Prix"))
for action, include in zip(actions, best_combination):

    if include:
        print(f"{action["nom"]:<13}{action["price"]:<4}€")
print("Profit total:", max_profit, "euros")
print("=" * 25)
depart_chrono.stop()
temps_écoulé = depart_chrono.elapsed_time()
print("Temps écoulé:", temps_écoulé, "secondes")
