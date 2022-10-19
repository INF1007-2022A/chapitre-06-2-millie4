#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames
import matplotlib.colors

def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    resulting_dict = {}
    for n in range(len(some_list)):
        resulting_dict.update({some_list[n]:n})
    return resulting_dict


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    inventaire_couleurs = []
    for color in colors:
        hex_value = matplotlib.colors.to_hex(matplotlib.colors.to_rgb(color))
        inventaire_couleurs.append((color,hex_value))
    return inventaire_couleurs


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350
    liste_entiers = []
    n = 0
    while n < 10000:
        if n > 15 and n < 350:
            n += 1
        else:
            liste_entiers.append(n)
            n+=1
    return liste_entiers


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    mse_dict = {}
    for model in model_dict:
        valeurs = model_dict[model]
        mse = 0
        for i in range(1,len(valeurs)):
            mse += len(valeurs) * (valeurs[i][0] - valeurs[i][1])^2
        mse_dict.update({model:mse})
    return mse_dict


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    
    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    #print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")

if __name__ == '__main__':
    main()
