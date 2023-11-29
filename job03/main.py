import time

class Horloge:
    def __init__(self, heure, minute, seconde, mode_24h=True):
        self.heure = heure
        self.minute = minute
        self.seconde = seconde
        self.mode_24h = mode_24h
        self.pause = False

    def afficher_heure(self):
        if not self.pause:
            if self.mode_24h:
                heure_format = "{:02d}:{:02d}:{:02d}".format(
                    self.heure, self.minute, self.seconde
                )
            else:
                am_pm = "AM" if self.heure < 12 else "PM"
                heure_format = "{:02d}:{:02d}:{:02d} {}".format(
                    self.heure % 12 if self.heure % 12 != 0 else 12,
                    self.minute,
                    self.seconde,
                    am_pm,
                )

            print("Heure actuelle:", heure_format)

    def mettre_en_pause(self):
        self.pause = True

    def relancer(self):
        self.pause = False

# Exemple d'utilisation
horloge = Horloge(12, 30, 0, mode_24h=True)

# Afficher l'heure normalement
horloge.afficher_heure()

# Mettre en pause l'horloge pendant 5 secondes
horloge.mettre_en_pause()
time.sleep(5)

# Relancer l'horloge et afficher l'heure à nouveau
horloge.relancer()
horloge.afficher_heure()