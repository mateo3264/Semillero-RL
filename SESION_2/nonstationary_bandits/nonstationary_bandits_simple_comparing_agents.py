#Agentes enfrentados a un problema en el que
#los valores reales de las acciones (q(a))
#cambian en un tiempo determinado por la
#variable timestep_of_change. Los agentes
#actualizan sus estimados con 1/n(a) y alpha constante
#entre (0,1]. Se ve el desempeño de los dos
#agentes en las gráficas.

import numpy as np
import matplotlib.pyplot as plt
from comparing_agents import run_experiment

#para permitir replicación del experimento
np.random.seed(5) 

K = 5 

epsilon = 0.1

alpha = 0.01

timesteps = 200_000

timestep_of_change = 35_000




run_experiment(alpha,epsilon,timesteps,timestep_of_change,n_actions=K)

