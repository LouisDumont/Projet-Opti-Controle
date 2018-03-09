#!/usr/bin/python
import numpy as np
from numpy import dot

def wolf(alpha, x, D, oracle):
    
    # Coefficients de la recherche lineaire
    omega_1 = 0.1
    omega_2 = 0.9
    alpha_min = 0.0
    alpha_max = np.inf
    ok = 0
    dltx = 0.00000001
    
    # Algorithme de Fletcher-Lemarechal
    
    # Appel de l'oracle au point initial
    loss, gradient, _ = oracle(x)
    # Initialisation de l'algorithme
    alpha_n = alpha
    xn     = x
    # Boucle de calcul du pas
    # xn represente le point pour la valeur courante du pas,
    # xp represente le point pour la valeur precedente du pas.
    while (ok==0):
        xp = xn
        xn = x + alpha_n*D
        
        # Calcul des conditions de Wolf
        loss_n, gradient_n, _ = oracle(xp)
        wolf_1 = (loss_n - loss) <= (omega_1 * alpha_n * dot(gradient, D))
        wolf_2 = (dot(gradient_n,D) >= omega_2 * dot(gradient, D))
        #print(wolf_1)
        #Test de la valeur de alphan :
        #- si les deux conditions de Wolfe sont verifiees,
        #   faire ok = 1 : on sort alors de la boucle while
        #- sinon, modifier la valeur de alphan : on reboucle.
        if wolf_1:
            if wolf_2:
                ok = 1
            else:
                if alpha_max==np.inf: alpha_n = 2 * alpha_min
                else: alpha_n = (1/2) * (alpha_min + alpha_max)
        else:
            alpha_max = alpha_n
            alpha_n = (1/2) * (alpha_min + alpha_max)
        
        loss, gradient = loss_n, gradient_n
                
        # Test d'indistinguabilite
        if (np.linalg.norm(xn-xp)<dltx):
            ok = 2
    
    return(alpha_n,ok)
    
if __name__=="__main__":
    x = np.random.normal(size=n-md)
    D = np.random.normal(size=n-md)
    wolf(1,x,D,oracle)