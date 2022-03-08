# "python3 conditions.py" pour lancer ds terminal

avec_soleil = True
en_semaine = False

if avec_soleil and not en_semaine:
   print("on va à la plage !")
elif avec_soleil and en_semaine:
   print("on va au travail !")
else:
   print("on reste à la maison !")


# opérateurs == != < <= > >=

nombre_de_sieges = 30
nombre_dinvites = 25

if nombre_dinvites < nombre_de_sieges:
   print("on peut encore inviter des gens")
else: 
   print("il y a trop d'invités!")