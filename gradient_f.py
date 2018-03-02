import numpy as np

from visualg import *

def Gradient_F(Oracle,xini):
    #Resolution d'un probleme d'optimisation sans contrainte
    #Methode de gradient a fixe
    
    #Parametres de la methode$
    
    #titre = "Parametres du gradient a pas fixe"
    #labels = ["Nombre maximal d''iterations"; "Valeur du pas de gradient"; "Seuil de convergence sur ||G||"]
    #typ = list("vec",1,"vec",1,"vec",1)
    #default = ["5000";"0.0005";"0.000001"]
    #[ok,iter,alphai,tol] = getvalue(titre,labels,typ,default);
    iter = 5000 #label = "Nombre maximal d'iterations"
    alphai = 0.0005 #label = "Valeur du pas de gradient"
    tol = 0.000001 #label = "Seuil de convergence sur ||G||"
    
    #Initialisation des variables
    
    logG = [];
    logP = [];
    Cout = [];
    timer();
    
    #Boucle sur les iterations
    
    x = xini
    kstar = iter
    
    for k in range (0,iter):
        #Valeur du critère et du gradient
        ind = 4
        [F,G] = Oracle(x,ind)
        #Test de convergence
        if np.abs(G)<=tol:
            kstar = (k+1);
            break
        #Calcul de la direction de descente
        D = -G
        #Calcul de la longueur du pas de gradient
        alpha = alphai
        #Mise à jour des variables
        x = x + (alpha*D)
        #Evolution du gradient, du pas, et du critère
        logG = [logG, log10(np.abs(G))]
        logP = [logP, log10(alpha)]
        Cout = [Cout, F]
    
    #Resultat de l'optimisation
    fopt = F
    xopt = x
    gopt = G
    tcpu = timer()
    print('Iteration : '+ string(kstar)\n)
    print('Temps CPU : ' + string(tcpu)\n)
    print('Critere optimal : ' + string(fopt)\n)
    print('Norme du gradient : ' + string(np.abs(gopt))\n)
    
    #Visualisation de la convergence
    Visualg(logG,logP,Cout)
    
    