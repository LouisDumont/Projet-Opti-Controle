import matplotlib.pyplot as plt

def Visualg(logG, logP, Cout):
    plt.subplot(3, 1, 0)
    plt.plot(logG, label="Norme du gradient (échelle log)")
    plt.subplot(3, 1, 1)
    plt.plot(logP, label="Pas de gradient (échelle log)")
    plt.subplot(3, 1, 2)
    plt.plot(Cout, label="Evolution du critere")
    plt.show()
