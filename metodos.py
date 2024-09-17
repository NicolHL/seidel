# Importar la biblioteca necesaria
import numpy as np

# Definición de la matriz A y el vector b
A = np.array([[3, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10]])

b = np.array([7.85, -19.3, 71.4])

# Inicialización
x = np.zeros_like(b)  # Vector de soluciones inicializado a cero
n_iterations = 10  # Número de iteraciones
tolerance = 1e-5  # Tolerancia para la convergencia

# Método de Gauss-Seidel
print("Resultados de cada iteración:")
for iteration in range(n_iterations):
    x_old = x.copy()

    for i in range(len(b)):
        # Suma de los términos
        sigma = sum(A[i][j] * x[j] for j in range(len(b)) if j != i)
        x[i] = (b[i] - sigma) / A[i][i]

    # Mostrar los resultados de la iteración
    print(f"Iteración {iteration + 1}: {x}")

    # Verificación de la convergencia
    if np.linalg.norm(x - x_old, ord=np.inf) < tolerance:
        print(f"Convergió en {iteration + 1} iteraciones.")
        break

# Resultados finales
print("Soluciones finales:")
print(x)