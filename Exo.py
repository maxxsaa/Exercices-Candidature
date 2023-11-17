#1 Écrire un code qui calcule l’indice de masse corporelle d’une personne (IMC = poids /taille2)


def imc(poids,taille):
    return(poids/taille**2)

#2 Écrire un code qui affiche les 3 premiers caractères d’une chaîne de caractère

def trois(mot):
    return mot[0:3]


#3 Écrire un code qui affiche les 3 derniers caractères d’une chaîne de caractère

def trois_derniers(mot):
    return mot[-3:]



#4 Écrire un code qui intervertit le contenu de deux variables

var1 = 'a'
var2 = 'b'

def inv(var1, var2) :
    (var1, var2) = (var2, var1)
    return (var1, var2)


#5 Écrire un code qui calcule le nombre de cuillères à soupe qu’il faut pour avoir X grammes de
# sucre, X étant une variable. Le programme doit afficher au final le texte suivant: 
#« Pour x grammes de sucre, il faut y cuillères à soupe».

def cui(x):
    y = x/15
    return 'Pour x grammes de sucre, il faut '+str(y)+' cuillères à soupe.'


#6 Écrire un code qui crée une liste avec 3 éléments entiers représentant une note d’examen sur 20

note1 = 15
note2 = 12
note3 = 8

liste = [note1, note2, note3]

#7 Ajouter une quatrième note

note4 = 10
liste.append(note4)

#8 Ajouter 1 point à la deuxième note

liste[1] += 1


#9 Calculer la moyenne des 4 notes

def moy(liste):
    tot = 0
    for i in liste : 
        tot += i
    moy = tot/len(liste)
    return moy


#10 Écrire un code qui écrit tous les entiers de 0 jusqu'à un nombre passé en paramètre.

def fonc(n):
    for i in range(n) :
        print(i)
        

#11 Écrire un code qui trouve le nombre le plus petit dans une liste de nombres.

liste_nombre = [2,3,4,5,18,1]
nombre_min = min(liste_nombre)
print(nombre_min)

#12 Écrire un code qui retourne les éléments communs à deux listes de nombres entiers.

liste1 = [2,3,4,5,18,1]
liste2 = [5,3,2,5,15,1]
com = list(set(liste1) & set(liste2))
print(com)


#13 Écrire une fonction qui calcule l’amende relative à un excès de vitesse. La fonction prendra deux paramètres: la vitesse maximale et
# la vitesse constatée. Les tarifs sont les suivants:
#– Dépassement de 0 à 10 km/h: € 53
#– Dépassement > 10km/h: € 53 + € 6 par km au dessus de 10 km/h
# – Dépassement > 40km/h: un nombre aléatoire entre € 80 et € 4.000

import random

def amende(x, max):
    if 1 < (x - max) < 11 :
        return "53 d'amende"
    elif 10 < (x - max) < 40 :
        sup = (x - max) - 10
        return (53 + sup*6)
    elif (x - max) > 40 :
        return random.randint(80, 4000)
    else:
        return "pas d'amende"



#14 Écrire une fonction qui prend en paramètre la date de naissance d’une personne et qui calcule son âge en années.
import datetime


def age(annéenaissance):
    age = 2023 - annéenaissance
    return age


#15 Améliorer la fonction de calcul d’âge en lui faisant calculer l’âge en années, mois et jours.

from datetime import datetime 

def age2(date):
    date_format = "%Y-%m-%d"
    date_naissance = datetime.strptime(date, date_format)
    aujrd = datetime.now()
    diff = aujrd - date_naissance

    ans = diff.days // 365
    mois = (diff.days % 365) // 30
    jours = (diff.days % 365) % 30
    return(ans, mois, jours)


#16 Créer un jeu de 52 cartes, puis:
#– Mélanger le jeu aléatoirement.
#– Piocher la première carte.
#– Parcourir le jeu jusqu’à trouver une carte de même valeur.
# – Retenez le nombre de cartes qu’il a fallu parcourir pour tomber sur la première paire.
#– Exécutez 1000 fois cette opération  et calculez la moyenne de cartes à parcourir.

import random 

valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
symboles = ['Coeur','Carreau','Trèfle','Pique']

jeu = [(valeur,symbole) for valeur in valeurs for symbole in symboles]

random.shuffle(jeu)

premiere = jeu[0]

for carte in jeu[1:] :
    if carte[0] == premiere[0] :
        print(carte)
        break
