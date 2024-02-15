import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        if self.start_time is None:
            print("Le timer n'a pas encore ete demarre.")
            return None
        elif self.end_time is None:
            print("Le timer est toujours en cours. Utilisez la methode stop() pour l'arrêter.")
            return None
        else:
            temps_ecoule = self.end_time - self.start_time
            heures = int(temps_ecoule // 3600)
            minutes = int((temps_ecoule % 3600) // 60)
            secondes = int(temps_ecoule % 60)
            return "{}h {}mn {}s".format(heures, minutes, secondes)