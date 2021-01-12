import numpy as np

class pixel(object):

    def __init__(self,x,y):
    
        self.x = x
        self.y = y
        
    def identique(self, other):
    
        if self.x == other.x and self.y == other.y:
            return True
            
        else:
            return False
            
    def __repr__(self):
        
        return f"x = {self.x} et y = {self.y}"
        
    def add_tab(self, largeur, hauteur):
    
        x = self.x
        y = self.y
        
        tab = np.zeros((largeur, hauteur))
        
        if x > 0:
            if y > 0:            
                tab[x - 1, y - 1] += 1            
            tab[x - 1, y] += 1
            if y < (hauteur - 1):
                tab[x - 1, y + 1] += 1
        if y > 0:
            tab[x, y - 1] += 1
        if y < (hauteur - 1):
            tab[x, y + 1] += 1
        if x < (largeur - 1):
            if y > 0:
                tab[x + 1, y - 1] += 1
            tab[x + 1, y] += 1
            if y < (hauteur - 1):
                tab[x + 1, y + 1] += 1
        return tab
