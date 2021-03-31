#Agente enfrentado a un problema en el que
#los valores reales de las acciones (q(a))
#cambian en un tiempo determinado por la
#variable timestep_of_change. El agente
#actualiza sus estimados con alpha constante
#entre (0,1].

import numpy as np
import matplotlib.pyplot as plt
from simple_alpha import run_experiment

np.random.seed(2)

#número de acciones posibles
K = 5 #Modificar

epsilon = 0.1 #Modificar
alpha = 0.1 #Modificar
timesteps = 10_000 #Modificar

timestep_of_change = 500 #Modificar


run_experiment(alpha,epsilon,timesteps,timestep_of_change,n_actions=K)     



