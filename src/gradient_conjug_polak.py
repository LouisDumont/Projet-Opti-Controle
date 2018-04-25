#!/usr/bin/python

import numpy as np
from numpy.linalg import norm
from time import process_time
from wolfe_skel import *

from .visualize import visualize

# Resolution d'un probleme d'optimisation sans contrainte
# Methode de gradient conjugué - variante de Polak-Ribières

def gradient_polak(oracle, x0, iter_max=5000, threshold=0.000001, visual=True):
    # Initialisation des variables
    gradient_norm_list = []
    gradient_step_list = []
    loss_list = []
    
    # Pour calculer le temps de la descente de gradient
    time_start = process_time()
    
    
    # Boucle sur les iterations
    # Initialisation
    x_n = x0
    x_previous = x_n
    loss_previous, grad_previous, hess_previous = oracle(x_previous)
    d_previous = -grad_previous
    for k in range(iter_max):
        # Calcul de la nouvelle direction de descente
        loss_n, grad_n, hess_n = oracle(x_n)
        beta = dot(grad_n-grad_previous, grad_n)/(np.linalg.norm(grad_previous)**2)
        d_n = -grad_n + beta * d_previous
        # Calcul de alpha optimal
        alpha_n, ok = wolfe(1, x_n, d_n, oracle)
        # Calcul du nouveau minimum et mise à jour des vairables
        x_previous = x_n
        grad_previous = grad_n
        d_previous = d_n
        x_n = x_previous + alpha_n*d_n
        
        # Sections d'affichage
        gradient_norm = np.linalg.norm(grad_n)
        # Historique de l'évolution du gradient, du pas, et du critère
        gradient_norm_list.append(gradient_norm)
        gradient_step_list.append(alpha_n)
        loss_list.append(loss_n)
        
        # Test de convergence
        if gradient_norm <= threshold:
            break
        
    # Resultat de l'optimisation
    loss_opt = loss_n
    x_opt = x_n
    gradient_opt = grad_n
    time_cpu = process_time() - time_start
    print('Iteration :', k)
    print('Temps CPU :', time_cpu)
    print('Critere optimal :', loss_opt)
    print('Norme du gradient :', norm(gradient_opt))
    print('X optimal :', x_opt)
    
    # Visualisation de la convergence
    if visual:
        visualize(gradient_norm_list, gradient_step_list, loss_list)
    
    return loss_opt, x_opt, gradient_opt        
            
if __name__ == '__main__':
    oracle = lambda x: (x**2, np.array(x*2), None)
    x0 = np.array([2])
    loss_opt, x_opt, gradient_opt = gradient(oracle, x0, threshold=1e-16)
