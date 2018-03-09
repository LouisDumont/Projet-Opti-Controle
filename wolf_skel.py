#!/usr/bin/python
import numpy as np
from oracle import *
from numpy import dot

def wolf(alpha, x, D, oracle):
    
    # Coefficients de la recherche lineaire
    omega1 = 0.1
    omega2 = 0.9
    alphamin = 0.0
    alphamax = np.inf
    ok = 0
    dltx = 0.00000001
    
    # Algorithme de Fletcher-Lemarechal
    
    # Appel de l'oracle au point initial
    [F,G] = oracle(x)
    # Initialisation de l'algorithme
    alphan = alpha
    xn     = x
    # Boucle de calcul du pas
    # xn represente le point pour la valeur courante du pas,
    # xp represente le point pour la valeur precedente du pas.
    while (ok==0):
        xp = xn
        xn = x + dot(alphan,D)
        
        # Calcul des conditions de Wolfe
        # TO DO
        
        #Test de la valeur de alphan :
        #- si les deux conditions de Wolfe sont verifiees,
        #   faire ok = 1 : on sort alors de la boucle while
        #- sinon, modifier la valeur de alphan : on reboucle.
        # TO DO
        
        # Test d'indistinguabilite
        if (abs(xn-xp)<dltx):
            ok = 2
    
    return(alphan,ok)