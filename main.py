
# set()Un set est un ensemble de clefs non ordonnées et non redondant où l'on peut savoir si un élément est présent sans avoir à parcourir toute la liste (une sorte de dictionnaire où les valeurs seraient ignorées, seules les clefs comptent).

#exemple
animals = ["chien","tigre","loup","tigre","loup","lion","lion"]
unique_animals = set(animals)
print(unique_animals)

# le resultat sera {'chien', 'lion', 'loup', 'tigre'} ,il ne s'agit pas d'un dictionnaire. les element en double ne sont donne qu'une fois.


#add() permet d'ajouter un element au set

unique_animals.add("tortue")
print(unique_animals)
# le resultat sera {'tortue', 'chien', 'lion', 'loup', 'tigre'}

#remove retire un element 

unique_animals.remove("tigre")
print(unique_animals)
# le resultat sera {'lion', 'chien', 'loup', 'tortue'}

#list() transforme notre set en liste

unique_animals= list(unique_animals)
print(unique_animals)
# le resultat sera ['lion', 'loup', 'tortue', 'chien']

#En resume nous nous retrouvons avec une liste qui avait des element multiple a une liste avec des element unique.