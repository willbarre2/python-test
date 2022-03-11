import csv
# j'ouvre le fichier input.csv
with open('input.csv') as fichier_csv:
    #la première ligne est reconnue comme entête et les autres listes dans des dictionnaires
    reader = csv.DictReader(fichier_csv, delimiter=',')
    noms = []
    heures = []
    for ligne in reader:
        noms.append(ligne['nom'])
        heures.append(ligne['heures_travaillees'])
en_tete = ["nom", "salaire"]  
# je créé un fichier output.csv j'y sauve l'entête, puis pour chaque lignes les nom et les slaires (heures*15)
with open('output.csv', 'w') as output_csv:
    writer = csv.writer(output_csv, delimiter=',')
    writer.writerow(en_tete)
    for nom, heure in zip(noms, heures):
        salaire = int(heure)*15
        ligne = [nom, salaire]
        print(ligne)
        writer.writerow(ligne)