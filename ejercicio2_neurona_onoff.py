"""
Ejercicio 2 - Regresión Lineal Simple con una neurona artificial
================================================================

Objetivo:
    Usar una neurona artificial de 5 entradas, de forma iterativa,
    para encontrar los mejores W_i que acerquen y_estimado al y generado.

Función de activación:
    on/off (función escalón / step):   y = f(sum(w_i * x_i))
    f(z) = 1 si z >= 0,   0 si z < 0

NOTA PEDAGÓGICA:
    Se ESPERA que este planteamiento FALLE (mal resultado).
    La función de activación escalón (on/off) solo puede producir
    salidas 0 ó 1. Por tanto es imposible que aproxime una salida
    continua 'y' generada por una combinación lineal real.
    Además, la función escalón NO es derivable, así que no existe
    un gradiente útil para ajustar los pesos: el aprendizaje se
    estanca y el error se queda alto. Este ejercicio demuestra
    POR QUÉ una neurona con activación on/off no sirve para
    resolver un problema de regresión lineal.

Implementado SOLO con la librería estándar de Python (sin numpy).
"""

import random

# --------------------------------------------------------------------
# 1. Generación de los datos
# --------------------------------------------------------------------
random.seed(42)

N_MUESTRAS = 100
N_ENTRADAS = 5

# Pesos "reales" desconocidos que generan y (regresión lineal real)
W_reales = [2.0, -1.0, 0.5, 3.0, -2.5]
BIAS_real = 1.5


def gauss_ruido(sigma):
    return random.gauss(0.0, sigma)


# Matriz de entradas X (100 muestras, 5 entradas) y salida continua y
X = []
y = []
for _ in range(N_MUESTRAS):
    fila = [random.uniform(-1.0, 1.0) for _ in range(N_ENTRADAS)]
    salida = sum(w * x for w, x in zip(W_reales, fila)) + BIAS_real + gauss_ruido(0.1)
    X.append(fila)
    y.append(salida)


# --------------------------------------------------------------------
# 2. La neurona con activación on/off (escalón)
# --------------------------------------------------------------------
def activacion_onoff(z):
    """Función de activación on/off (escalón): 1 si z>=0, si no 0."""
    return 1.0 if z >= 0 else 0.0


def neurona(fila, W, b):
    """y_estimado = f(sum(w_i * x_i) + b) con f = on/off."""
    z = sum(w * x for w, x in zip(W, fila)) + b
    return activacion_onoff(z)


# --------------------------------------------------------------------
# 3. Entrenamiento iterativo (regla del perceptrón / ajuste por error)
# --------------------------------------------------------------------
def entrenar(X, y, epochs=200, lr=0.01):
    n_entradas = len(X[0])
    W = [random.uniform(-1.0, 1.0) for _ in range(n_entradas)]
    b = 0.0

    historial_error = []

    for epoca in range(epochs):
        # Acumuladores de ajuste
        grad_W = [0.0] * n_entradas
        grad_b = 0.0
        suma_err2 = 0.0

        for fila, objetivo in zip(X, y):
            y_est = neurona(fila, W, b)      # 0 ó 1
            error = objetivo - y_est          # objetivo continuo, estimado 0/1

            for i in range(n_entradas):
                grad_W[i] += error * fila[i]
            grad_b += error
            suma_err2 += error * error

        # Ajuste iterativo de pesos usando el error (estilo perceptrón)
        for i in range(n_entradas):
            W[i] += lr * grad_W[i]
        b += lr * grad_b

        mse = suma_err2 / len(y)
        historial_error.append(mse)

        if epoca % 20 == 0 or epoca == epochs - 1:
            print("Época {:3d} | MSE = {:8.4f}".format(epoca, mse))

    return W, b, historial_error


# --------------------------------------------------------------------
# 4. Ejecución
# --------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("Ejercicio 2: Neurona de 5 entradas con activación on/off")
    print("=" * 60)
    print("\nPesos reales usados para generar y: {}".format(W_reales))
    print("Bias real: {}\n".format(BIAS_real))

    print("Entrenamiento iterativo:")
    print("-" * 60)
    W_final, b_final, historial = entrenar(X, y, epochs=200, lr=0.01)

    print("-" * 60)
    print("\nPesos encontrados: {}".format([round(w, 4) for w in W_final]))
    print("Bias encontrado:   {}".format(round(b_final, 4)))

    y_est_final = [neurona(fila, W_final, b_final) for fila in X]
    mse_final = sum((o - e) ** 2 for o, e in zip(y, y_est_final)) / len(y)

    valores_unicos = sorted(set(y_est_final))

    print("\n" + "=" * 60)
    print("RESULTADOS")
    print("=" * 60)
    print("MSE final: {:.4f}   (cuanto más alto, peor)".format(mse_final))
    print("Rango real de y:        [{:.2f}, {:.2f}]".format(min(y), max(y)))
    print("Valores de y_estimado:  {}  <- ¡solo 0 y/o 1!".format(valores_unicos))

    print("\n>>> CONCLUSIÓN (fallo esperado):")
    print(">>> La activación on/off solo produce 0 ó 1, mientras que 'y'")
    print(">>> es un valor continuo. Es IMPOSIBLE aproximar una regresión")
    print(">>> lineal con esta función de activación. Además, al no ser")
    print(">>> derivable, no hay gradiente útil y el ajuste no converge.")
    print(">>> Para regresión lineal habría que usar activación LINEAL.")
