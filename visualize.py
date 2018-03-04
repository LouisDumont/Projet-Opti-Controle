import matplotlib.pyplot as plt

def visualize(gradient_norm_list, gradient_step_list, loss_list):
    plt.subplot(3, 1, 1)
    plt.gca().set_title("Evolution de la norme du gradient")
    plt.plot(gradient_norm_list, label="Norme du gradient")
    plt.subplot(3, 1, 2)
    plt.gca().set_title("Evolution du pas de gradient")
    plt.plot(gradient_step_list, label="Pas de gradient")
    plt.subplot(3, 1, 3)
    plt.title("Evolution du critère")
    plt.plot(loss_list, label="Critère")
    plt.tight_layout()
    plt.show()
