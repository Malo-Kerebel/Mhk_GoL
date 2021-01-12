from Pixel import pixel
import random
import numpy as np
import time
import os

def pixel_present(x, y):

    for pixel in list_pixel:
        if pixel.x == x and pixel.y == y:
            return True
    return False

largeur = 50
hauteur = 250
N = largeur * hauteur / 10 #un 10ème des cases seront remplis

list_pixel = []

i = 0
while i < N:

    list_pixel.append(pixel(random.randint(0,largeur - 1),random.randint(0,hauteur - 1)))
    
    for other in list_pixel[:-1]:
        if list_pixel[-1].identique(other):
            i -= 1
            del(list_pixel[-1])#supprime l'élement de la liste, on ne veut pas plusier pixel au même endroit
    i += 1

del(i)
while True:
    
    tab = np.zeros((largeur,hauteur))
    for pixels in list_pixel:    
        tab += pixels.add_tab(largeur, hauteur)
    
        
    for i in range(largeur):
        for j in range(hauteur):
            if tab[i,j] == 2  and pixel_present(i,j):
                tab[i,j] += 1
             
    list_pixel = []
    string = "|"
    for i in range(largeur):
        for j in range(hauteur):
            if tab[i,j] == 3:
                list_pixel.append(pixel(i,j))
                string += "@"
            else:
                string += " "
        string += "|\n|"
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(string)
    time.sleep(1) 
                

