#!/usr/bin/python

import numpy as np
from numpy.linalg import norm
from time import process_time

from .wolfe_skel import *
from .visualize import visualize

# Resolution d'un probleme d'optimisation sans contrainte
def newton(oracle, x_0, iter_max = 5000, threshold = 0.000001, visual=True, verbose=False):
    # Initialisation des variables
    direction_norm_list = []
    direction_step_list = []
    loss_list = []
    
    # Pour calculer le temps de la descente de direction
    time_start = process_time()

    # Boucle sur les iterations
    x = x_0
    for k in range(iter_max):
        # Valeur du critère, du direction et de la hessienne
        loss, direction, hessian = oracle(x, compute_hessian=True)
        direction = dot(inv(hessian), direction)
        direction_norm = norm(direction)

        # Test de convergence
        if direction_norm <= threshold:
            break
        
        # Calcul de la longueur du pas de direction
        direction_step, ok = wolfe(1, x, -direction, oracle)
        # Mise à jour des variables
        x = x - direction * direction_step
        if verbose:
            print('Iter :', k, '; direction_step={}'.format(direction_step), '; direction_norm={}'.format(direction_norm))
        
        # Historique de l'évolution de la direction, du pas, et du critère
        direction_norm_list.append(direction_norm)
        direction_step_list.append(direction_step)
        loss_list.append(loss)
    
    # Resultat de l'optimisation
    loss_opt = loss
    x_opt = x
    direction_opt = direction
    time_cpu = process_time() - time_start
    print('Iteration :', k)
    print('Temps CPU :', time_cpu)
    print('Critere optimal :', loss_opt)
    print('Norme de la direction :', norm(direction_opt))
    print('X optimal :', x_opt)
    
    # Visualisation de la convergence
    if visual:
        visualize(direction_norm_list, direction_step_list, loss_list)
    
    return loss_opt, x_opt, direction_opt
