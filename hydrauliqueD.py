from structure_r import *


def HydrauliqueD(pd):
    # Pressions aux noeuds
    p = [pr,pd]
    # Pertes de charge des arcs
    z = - np.transpose(A) * p
    # Debits des arcs
    q = z / sqrt(r*abs(z))
    # Flux aux noeuds
    f = [ Ar*q , fd ]
    return(q,z,f,p)