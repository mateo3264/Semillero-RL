#Agente enfrentado a un problema en el que
#los valores reales de las acciones (q(a))
#cambian en un tiempo de terminado por la
#variable timestep_of_change

import numpy as np
import matplotlib.pyplot as plt
from simple_1_n import run_experiment

np.random.seed(3)

#Número de acciones posibles
K = 7 #Modificar

#Probabilidad de explorar
epsilon = 0.01 #Modificar

#Número total de intentos
timesteps = 10_000 #Modificar

#En que intento (timestep) se hará el cambio de los valores de las acciones
timestep_of_change = 1000 #Modificar


run_experiment(epsilon,timesteps,timestep_of_change,n_actions=K)
