import time
import threading

# Variable globale pour stocker l'heure actuelle
heure_actuelle = (0, 0, 0)

# Verrou pour assurer un accès sûr à l'heure actuelle
verrou_heure = threading.Lock()

# Fonction pour afficher l'heure au format hh:mm:ss
def afficher_heure():
    global heure_actuelle
    with verrou_heure:
        print(f"{heure_actuelle[0]:02d}:{heure_actuelle[1]:02d}:{heure_actuelle[2]:02d}")

# Fonction pour mettre à jour l'heure chaque seconde
def actualiser_heure():
    global heure_actuelle
    while True:
        time.sleep(1)  # Pause d'une seconde
        with verrou_heure:
            heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)
        afficher_heure()

# Fonction pour régler l'heure
def regler_heure(heures, minutes, secondes):
    global heure_actuelle
    with verrou_heure:
        heure_actuelle = (heures, minutes, secondes)
    afficher_heure()

# Fonction pour régler l'alarme
def regler_alarme(heures, minutes, secondes):
    alarme = (heures, minutes, secondes)
    while True:
        time.sleep(1)
        with verrou_heure:
            if heure_actuelle == alarme:
                print("Alarme! L'heure de l'alarme est atteinte.")
                break

# Lancement des threads
thread_actualiser_heure = threading.Thread(target=actualiser_heure)
thread_actualiser_heure.start()

# Exemples d'utilisation des fonctions
regler_heure(16, 30, 0)
regler_alarme(16, 31, 0)