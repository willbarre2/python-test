# "python helloworld.py" pour lancer ds terminal

# ligne unique
"""
lignes multiples
"""

livre = "Gatsby le Magnifique"
livre = "On the road"
print(livre)

nombre = 2.2
print(type(nombre))

fruits = ["pomme", "banane", "poire"] # tableau = liste
print(fruits[-1])
print(fruits[0][2])
fruits.append("orange")
fruits.remove("banane")
fruits.sort()
print(fruits)
print(len(fruits))

un_tuple = ("visse", "clout", "pointe") #les tuples sont immuables
print(un_tuple)

# objet = dictionnaire
infos_labradoodle = {
    "poids": "13 à 16 kg",
    "origine": "États-Unis"
}

infos_labradoodle['nom_scientifique'] = "Canis lupus familiaris"
infos_labradoodle["poids"] = "45 kg"
# del infos_labradoodle["origine"]
infos_labradoodle.pop('origine')

print(infos_labradoodle)
print("poids" in infos_labradoodle)

# a={} = b=dict()