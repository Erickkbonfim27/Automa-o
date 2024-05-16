"""
Pereceptron de uma única camada
@author= Erick Kopak Bonfim
"""
import numpy as np

entradas = np.array([
        2,
        7,
        5,
    ])
pesos = np.array([
    0.8,
    0.1,
    0   
    ])

def soma(e, p):
    return e.dot(p)

s = soma(entradas, pesos)

def step_Function(soma):
    if soma > 1:
        return 1
    return 0
r = step_Function(s)