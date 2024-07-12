"""
Módulo para obtener evolución temporal de la probabilidad de encontrar un fermion en una grilla unidimensional de tamaño N utilizando el método de Runge-Kutta de cuarto orden.
"""

import numpy as np

def estado_inicial(N):
    """
    Función para crear el estado inicial (grilla).

    Args:
        N (int): Tamaño de la grilla.

    Returns:
        numpy.ndarray:
            Arreglo NumPy que representa el estado inicial con un fermión en la posición central.
    """
    estado_inicial = np.zeros(N)
    estado_inicial[N//2] = 1 
    return estado_inicial


def matriz_ham(T, epsilon):
    """
    Función para crear la matriz Hamiltoniana.

    Args:
        t_i (numpy.ndarray): Elementos de las diagonales adyacentes a la diagonal principal de la matriz Hamiltoniana.
        epsilon (numpy.ndarray): Valores de la diagonal principal de la matriz Hamiltoniana.

    Returns:
        numpy.ndarray:
            Matriz Hamiltoniana generada.
    """
    N = epsilon.size
    matriz = np.zeros((N, N))
    matriz[np.diag_indices(N)] = epsilon 
    np.fill_diagonal(matriz[:,1:], T)
    np.fill_diagonal(matriz[1:,:], T) 
    return matriz
    
# calculo de la ecuacion de schrodinger
def ecu_sch(matriz_ham, grilla_actual):
    """
    Función que multiplica la matriz Hamiltoniana por la ecuacion de onda.

    Args:
        matriz_ham (numpy.ndarray): Matriz hamiltoniana que determina la eolucion en la grilla.
        grilla_actual (numpy.ndarray): Estado de la grilla que se desea evolucionar.

    Returns:
        numpy.ndarray:
            Evolucion de la grilla.
    """
    matriz_hamc = -1.0j * matriz_ham
    return matriz_hamc @ grilla_actual


# Función para la evolución temporal según la ecuación de Schrödinger
def ecu_schrodinger_rk4(matriz_ham, grilla_actual, dt):
    """
    Función para la evolución temporal según la ecuación de Schrödinger con el método de Runge-Kutta de cuarto orden.

    Args:
        matriz_ham (numpy.ndarray): Matriz Hamiltoniana que define el sistema físico.
        grilla_actual (numpy.ndarray): Estado actual de la función de onda.
        dt (float): Paso de tiempo.

    Returns:
        numpy.ndarray:
            Nuevo estado de la grilla después de la evolución temporal.
    """
    k1 = ecu_sch(matriz_ham, grilla_actual)
    k2 = ecu_sch(matriz_ham, grilla_actual + (dt/2) * k1)
    k3 = ecu_sch(matriz_ham, grilla_actual + (dt/2) * k2)
    k4 = ecu_sch(matriz_ham, grilla_actual + dt * k3)
    
    grilla_nueva = grilla_actual + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
    
    return grilla_nueva


def inicio(t_i, epsilon, tiempos):
    """
    Función principal para evolucionar la grilla en el tiempo.

    Args:
        t_i (numpy.ndarray): Valores de probabilidad para el movimiento del fermion.
        epsilon (numpy.ndarray): Valores del potencial para el fermion.
        tiempos (numpy.ndarray): Tiempos para los cuales se evaluará la función de onda.

    Returns:
        numpy.ndarray:
            Valores de probabilidad de encontrar el fermion en cada punto de la grilla.
    """
    dt = tiempos[1] - tiempos[0]
    N = epsilon.size
    grilla_actual = estado_inicial(N)
    matriz_hamiltoniana = matriz_ham(t_i, epsilon)
    shape = [0.0 for i in range(len(tiempos))]
    shape[0] = np.abs(grilla_actual)**2
    for t in range(1, tiempos.size):
        # Aquí ponemos la probabilidad en cada tiempo
        shape[t] = np.abs(grilla_actual)**2
        # Evolución
        grilla_actual = ecu_schrodinger_rk4(matriz_hamiltoniana, grilla_actual, dt)
        
    return shape





