#!/usr/bin/python

import numpy as np
import random

# Nom du reseau
nom = "Parametrable"

# Initialisation du generateur aleatoire
T = 7 # Nombre de niveaux
gral = 123 # Graine Aleatoire
random.seed(gral)

# Dimensions du reseau
m  = (2**(T+1)) - 1
mr = 1
md = m - mr
n  = ((2**(T+1))-1) + ((2**(T+1))-1) - (T+1) - 1

# Numeros des noeuds initiaux et finaux des arcs
orig = []
dest = []

# Arcs de l'arbre
num = 1
for t in range (0,T):
      ni = (2**t);
      nf = (2**(t+1)) - 1;
      nz = 2 * (nf-ni+1);
      #aorg = [ [ni:nf] ; [ni:nf] ];
      aorg = np.array([range(ni,nf+1),range(ni,nf+1)])
      #orig = [ orig aorg(1:nz)' ];
      orig = np.concatenate((orig,aorg.flatten('F')), axis=0)
      #dest = [ dest [num+1:num+nz] ];
      dest = np.concatenate((dest,np.array(range(num+1,num+nz+1))), axis=0)
      num = num + nz;
      
# Arcs du coarbre
for t in range(1, T+1):
      ni = (2**t);
      nf = (2**(t+1)) - 1;
      #orig = [ orig [ni:nf-1] ];
      orig = np.concatenate((orig,np.array(range(ni,nf))), axis=0)
      #dest = [ dest [ni+1:nf] ];
      dest = np.concatenate((dest,np.array(range(ni+1,nf+1))), axis=0)
      
# Coordonnees des noeuds
absn = []
for t in range(0,T+1):
      ni = (2**t);
      nf = (2**(t+1)) - 1;
      na = 2**(T-t+1);
      nb = 2**(T-t);
      #num = na*[0:nf-ni] + nb;
      num = na*np.array(range(0,nf-ni+1)) + nb
      #absn = [ absn num ];
      absn = np.concatenate((absn,num),axis=0)
ordn = []
for t in range(0,T+1):
      ni = (2**t);
      nf = (2**(t+1)) - 1;
      #ordn = [ ordn (T-t+1)*ones(1,nf-ni+1) ];
      ordn = np.concatenate((ordn,(T-t+1)*np.ones(nf-ni+1)),axis=0)

# Resistances des arcs
r = 1000 * np.random.rand(n,1)

# Pressions au pied du reservoir (en m)
pr = np.array([200])

# Flux aux noeuds de demande (en m3/s)
fd = 0.1 * (np.random.rand(md,1)-0.5)
      
      