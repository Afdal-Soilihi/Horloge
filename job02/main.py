def afficher_heure(heure, minute, seconde, mode_24h=True):
    if mode_24h:
        heure_format = "{:02d}:{:02d}:{:02d}".format(heure, minute, seconde)
    else:
        am_pm = "AM" if heure < 12 else "PM"
        heure_format = "{:02d}:{:02d}:{:02d} {}".format(
            heure % 12 if heure % 12 != 0 else 12, minute, seconde, am_pm
        )

    return heure_format

# Exemples d'utilisation
heure_24h = (16, 30, 0)
heure_12h = (8, 45, 0)

print("Mode affichage 24h:", afficher_heure(*heure_24h, mode_24h=True))
print("Mode affichage 12h:", afficher_heure(*heure_12h, mode_24h=False))
      