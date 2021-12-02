from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")

    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        # creation d'une image vide
        im_bin = Image()
        
        # affectation a l'image im_bin d'un tableau de pixels de meme taille
        # que self dont les intensites, de type uint8 (8bits non signes),
        # sont mises a 0
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))

        # TODO: boucle imbriquees pour parcourir tous les pixels de l'image im_bin
        # et calculer l'image binaire
        for i in range (self.H):
            for j in range (self.W):
                if self.pixels[i,j]<S:
                    im_bin.pixels[i,j]=0
                else : 
                    im_bin.pixels[i,j]=255
        return im_bin


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        im_loc=Image()
        c_min=self.W-1
        c_max=0
        l_min=self.H-1
        l_max=0
        
        """
        for l in range (self.H):
            for c in range (self.W):
                if self.pixels[l,c]==0:
                    l_min=l
                    step=True
         """           
                
                
                
        
        
        
        #test pour c_min
        for i in range (self.W):
            count_min=0
            for j in range (self.H):
                while self.pixels[i,j]==255:
                    count_min=count_min+1
                if count_min<c_min:
                    c_min=count_min
                    
        #test pour c_max
        for i in range (self.H):
            count_max=0
            indice_colonne=self.W
            
            while indice_colonne>0:
                if self.pixels[i,indice_colonne]==0:
                    count_max=indice_colonne
                    indice_colonne=0
                else:
                    indice_colonne=indice_colonne-1
            
            if count_max>c_max:
                c_max=count_max
        
        #test pour l_min
        for i in range (self.H):
            count_min=0
            for j in range (self.W):
                while self.pixels[i,j]==255:
                    count_min=count_min+1
                if count_min<l_min:
                    l_min=count_min
        
        #test pour l_max
        for i in range (self.W):
            count_max=0
            indice_ligne=self.H
            
            while indice_ligne>0:
                if self.pixels[i,indice_ligne]==0:
                    count_max=indice_ligne
                    indice_ligne=0
                else:
                    indice_ligne=indice_ligne-1
            
            if count_max>l_max:
                l_max=count_max
        
        
        im_loc.set_pixels(np.zeros((l_max-l_min, c_max-c_min), dtype=np.uint8))
        
        for l in range (l_max-l_min):
            for c in range (c_max-c_min):
                im_loc.pixels[l,c]=self.pixels[l_min+l,c_min+c]
        
        im_loc=self.pixels[l_min:l_max-1,c_min:c_max-1]
        return im_loc

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        pass


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        pass

