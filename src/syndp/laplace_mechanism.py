import numpy as np

def laplace_mechanism(value : float, sensitivity: float, epsilon:float, seed=0):
    np.random.seed(seed)
    len_of_element = len(list(value))
    scale = sensitivity/epsilon
    noise = np.random.laplace(0, size=len_of_element, scale=scale)
    return value + noise.item()
