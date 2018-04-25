#!/usr/bin/python

import numpy as np
from numpy.linalg import norm
from time import process_time

from .wolfe_skel import *
from .visualize import visualize

# Resolution d'un probleme d'optimisation sans contrainte
# Methode pseudo-newtonienne: BFGS

def bfgs(oracle, x0, iter_max = 5000, threshold = 0.000001, visual=True, verbose=False):
    # Initialisation des variables
    gradient_norm_list = []
    gradient_step_list = []
    loss_list = []
    
    # Pour calculer le temps de la descente de gradient
    time_start = process_time()

    # Boucle sur les iterations
    size = x0.size
    x = x0
    x_previous = x
    W_n = np.eye(size)
    loss, gradient, hess = oracle(x)
    d_n = -np.dot(W_n, gradient)
    alpha, ok = wolfe(1, x, d_n, oracle)
    x = x_previous + alpha * d_n
    for k in range(iter_max):
        # Calcul de la perte et du gradient
        loss_previous, gradient_previous = loss, gradient
        loss, gradient, hess = oracle(x)
        # Calcul des écarts précédents
        delta_x = x - x_previous
        delta_grad = gradient - gradient_previous
        # Calcul de l'approximée de la hessienne
        aux_xg = np.outer(delta_x, delta_grad)/np.vdot(delta_grad, delta_x)
        #print(aux_xg.size)
        aux_gx = np.outer(delta_grad, delta_x)/np.vdot(delta_grad, delta_x)
        #print(aux_gx.size)
        aux_xx = np.outer(delta_x, delta_x)/np.vdot(delta_grad, delta_x)
        #print(aux_xx.size)
        W_n = np.dot(np.dot(np.eye(size) - aux_xg, W_n), np.eye(size) - aux_gx) + aux_xx
        # Calcul de la direction de descente
        d_n = - np.dot(W_n, gradient)
        # Calcul du pas de gradient
        gradient_step, ok = wolfe(1, x, d_n, oracle)
        # Mise à jour du point
        x_previous = x
        x = x_previous + gradient_step * d_n
        

        # Historique de l'évolution du gradient, du pas, et du critère
        gradient_norm = np.linalg.norm(gradient)
        if verbose:
            print('Iter :', k, '; gradient_step={}'.format(gradient_step), '; gradient_norm={}'.format(gradient_norm))
        gradient_norm_list.append(gradient_norm)
        gradient_step_list.append(gradient_step)
        loss_list.append(loss)
        
        # Test de convergence
        if gradient_norm <= threshold:
            break
    
    # Resultat de l'optimisation
    loss_opt = loss
    x_opt = x
    gradient_opt = gradient
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
    loss_opt, x_opt, gradient_opt = bfgs(oracle, x0, threshold=1e-16, verbose=True)
