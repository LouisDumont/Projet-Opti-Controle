#!/usr/bin/python

import numpy as np
from time import process_time

from visualg import *

# Resolution d'un probleme d'optimisation sans contrainte
# Methode de gradient a fixe
def Gradient_F(Oracle, xini):
    # Parametres de la methode
    max_iter = 5000 # Nombre maximal d'iterations
    alphai = 0.0005 # Valeur du pas de gradient
    tol = 0.000001  # Seuil de convergence sur la norme de G
    
    # Initialisation des variables
    logG = []
    logP = []
    Cout = []
    time_start = process_time()

    # Boucle sur les iterations
    x = xini
    for k in range (0, max_iter):
        # Valeur du critère et du gradient
        F, G = Oracle(x)
        # Test de convergence
        if np.abs(G)<=tol:
            break
        # Calcul de la direction de descente
        D = -G
        # Calcul de la longueur du pas de gradient
        alpha = alphai
        # Mise à jour des variables
        x = x + D*alpha
        # Evolution du gradient, du pas, et du critère
        logG.append(np.log(np.abs(G)))
        logP.append(np.log(alpha))
        Cout.append(F)
    
    # Resultat de l'optimisation
    fopt = F
    xopt = x
    gopt = G
    time_cpu = process_time() - time_start
    print('Iteration :', k)
    print('Temps CPU :', time_cpu)
    print('Critere optimal :', fopt)
    print('Norme du gradient :', gopt.norm())
    
    # Visualisation de la convergence
    Visualg(logG, logP, Cout)
    return fopt, xopt, gopt
    
    
