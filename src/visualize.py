#!/usr/bin/python

import matplotlib.pyplot as plt

def visualize(direction_norm_list, direction_step_list, loss_list, log_scale=True):
    plt.subplot(3, 1, 1)
    plt.gca().set_title("Evolution de la norme de la direction")
    if log_scale:
        plt.gca().set_yscale('log')
    plt.plot(direction_norm_list, label="Norme de la direction")
    
    plt.subplot(3, 1, 2)
    plt.gca().set_title("Evolution du pas")
    plt.plot(direction_step_list, label="Pas")
    
    plt.subplot(3, 1, 3)
    plt.title("Evolution du critère")
    plt.plot(loss_list, label="Critère")
    plt.tight_layout()
    plt.show()
