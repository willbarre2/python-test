# "python boucles.py" pour lancer ds terminal

races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

for x in range(4, 10):
    print(f"{x} bouteilles de bières au mur !")


capacite_maximale = 10
capacite_actuelle = 3
while capacite_actuelle < capacite_maximale:
    print(capacite_actuelle)
    capacite_actuelle += 1