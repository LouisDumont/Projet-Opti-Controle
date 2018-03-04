#!/usr/bin/python

import numpy as np
from numpy.linalg import norm
from time import process_time

from visualize import visualize

# Resolution d'un probleme d'optimisation sans contrainte
# Methode de gradient à fixe
def gradient_fixe(oracle, x0, iter_max = 5000, default_gradient_step = 0.0005, threshold = 0.000001, visual=True):
    # Initialisation des variables
    gradient_norm_list = []
    gradient_step_list = []
    loss_list = []
    
    # Pour calculer le temps de la descente de gradient
    time_start = process_time()

    # Boucle sur les iterations
    x = x0
    for k in range(iter_max):
        # Valeur du critère et du gradient
        loss, gradient = oracle(x)
        gradient_norm = norm(gradient)

        # Test de convergence
        if gradient_norm <= threshold:
            break
        
        # Calcul de la longueur du pas de gradient
        gradient_step = default_gradient_step
        
        # Mise à jour des variables
        x = x - gradient * gradient_step
        
        # Historique de l'évolution du gradient, du pas, et du critère
        gradient_norm_list.append(gradient_norm)
        gradient_step_list.append(gradient_step)
        loss_list.append(loss)
    
    # Resultat de l'optimisation
    loss_opt = loss
    x_opt = x
    gradient_opt = gradient
    time_cpu = process_time() - time_start
    print('Iteration :', k)
    print('Temps CPU :', time_cpu)
    print('Critere optimal :', loss_opt)
    print('Norme du gradient :', norm(gradient_opt))
    
    # Visualisation de la convergence
    if visual:
        visualize(gradient_norm_list, gradient_step_list, loss_list)
    
    return loss_opt, x_opt, gradient_opt
    
if __name__ == '__main__':
    oracle = lambda x: (x**2, np.array(x*2))
    x0 = np.array([2])
    loss_opt, x_opt, gradient_opt = gradient_fixe(oracle, x0)

