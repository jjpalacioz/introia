"""
Ejercicio 3 - Neurona con activación SIGMOIDE, coste MSE y offset
=================================================================

Parte del Ejercicio 2 (neurona de 5 entradas), pero ahora:
    * Función de COSTE explícita:  MSE (y_real vs y_estimado)
    * Función de ACTIVACIÓN:        sigmoide  s(z) = 1 / (1 + e^-z)
    * Se incluye OFFSET (bias 'b')
    * Se repite la estimación de la "recta" (los pesos W_i)

Entrenamiento: DESCENSO DE GRADIENTE.
    A diferencia del escalón on/off, la sigmoide SÍ es derivable, por lo que
    ahora existe un gradiente útil y el MSE puede reducirse de verdad.

    coste:      MSE = (1/N) * sum( (y - y_est)^2 )
    y_est   = s(z),   z = sum(w_i * x_i) + b
    derivada de la sigmoide:  s'(z) = s(z) * (1 - s(z))

    Regla de la cadena (gradiente del MSE respecto a w_i):
        dMSE/dw_i = (2/N) * sum( (y_est - y) * s'(z) * x_i )
        dMSE/db   = (2/N) * sum( (y_est - y) * s'(z) )

NOTA: la sigmoide devuelve valores en (0, 1). Si la 'y' real está fuera de
ese rango, la neurona no podrá alcanzarla (sigue habiendo una limitación de
rango). Por eso se muestran DOS escenarios:
    A) y sin escalar  -> el rango de y desborda (0,1): la recta no encaja.
    B) y normalizada a (0,1) -> la sigmoide sí puede aproximarla y el MSE baja.

Implementado SOLO con la librería estándar de Python (sin numpy).
"""

import math
import random

# --------------------------------------------------------------------
# 1. Generación de los datos
# --------------------------------------------------------------------
random.seed(42)

N_MUESTRAS = 100
N_ENTRADAS = 5

# Pesos "reales" que generan y (misma recta que en el Ejercicio 2)
W_reales = [2.0, -1.0, 0.5, 3.0, -2.5]
BIAS_real = 1.5


def generar_datos():
    X, y = [], []
    for _ in range(N_MUESTRAS):
        fila = [random.uniform(-1.0, 1.0) for _ in range(N_ENTRADAS)]
        salida = sum(w * x for w, x in zip(W_reales, fila)) + BIAS_real
        salida += random.gauss(0.0, 0.1)  # ruido
        X.append(fila)
        y.append(salida)
    return X, y


# --------------------------------------------------------------------
# 2. Activación sigmoide y su derivada
# --------------------------------------------------------------------
def sigmoide(z):
    # Estable numéricamente para z muy negativo/positivo
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    ez = math.exp(z)
    return ez / (1.0 + ez)


def neurona(fila, W, b):
    """y_est = sigmoide( sum(w_i * x_i) + b )  (incluye offset b)."""
    z = sum(w * x for w, x in zip(W, fila)) + b
    return sigmoide(z)


# --------------------------------------------------------------------
# 3. Función de coste MSE
# --------------------------------------------------------------------
def mse(X, y, W, b):
    s = 0.0
    for fila, objetivo in zip(X, y):
        e = objetivo - neurona(fila, W, b)
        s += e * e
    return s / len(y)


# --------------------------------------------------------------------
# 4. Entrenamiento por descenso de gradiente
# --------------------------------------------------------------------
def entrenar(X, y, epochs=2000, lr=0.5, verbose=True):
    n = len(X[0])
    N = len(X)
    W = [random.uniform(-0.5, 0.5) for _ in range(n)]
    b = 0.0
    historial = []

    for epoca in range(epochs):
        grad_W = [0.0] * n
        grad_b = 0.0

        for fila, objetivo in zip(X, y):
            z = sum(w * x for w, x in zip(W, fila)) + b
            y_est = sigmoide(z)
            dsig = y_est * (1.0 - y_est)          # derivada de la sigmoide
            factor = (y_est - objetivo) * dsig     # (y_est - y) * s'(z)
            for i in range(n):
                grad_W[i] += factor * fila[i]
            grad_b += factor

        # Media y factor 2 del MSE
        for i in range(n):
            W[i] -= lr * (2.0 / N) * grad_W[i]
        b -= lr * (2.0 / N) * grad_b

        coste = mse(X, y, W, b)
        historial.append(coste)

        if verbose and (epoca % 200 == 0 or epoca == epochs - 1):
            print("Época {:4d} | MSE = {:8.5f}".format(epoca, coste))

    return W, b, historial


# --------------------------------------------------------------------
# 5. Utilidades
# --------------------------------------------------------------------
def normalizar_01(valores):
    lo, hi = min(valores), max(valores)
    rango = hi - lo
    return [(v - lo) / rango for v in valores], lo, hi


# --------------------------------------------------------------------
# 6. Ejecución
# --------------------------------------------------------------------
if __name__ == "__main__":
    X, y = generar_datos()

    print("=" * 64)
    print("Ejercicio 3: Neurona de 5 entradas - activación SIGMOIDE + MSE")
    print("=" * 64)
    print("Pesos reales: {}   Bias real: {}".format(W_reales, BIAS_real))
    print("Rango real de y: [{:.2f}, {:.2f}]".format(min(y), max(y)))

    # -------- Escenario A: y sin escalar --------
    print("\n" + "-" * 64)
    print("ESCENARIO A: sigmoide con 'y' SIN escalar")
    print("-" * 64)
    print("La sigmoide solo produce valores en (0,1), pero y sale de ese rango.")
    Wa, ba, _ = entrenar(X, y, epochs=2000, lr=0.5)
    print("\nMSE final (A): {:.5f}   <- alto: la recta NO encaja".format(
        mse(X, y, Wa, ba)))
    print("Pesos (A): {}".format([round(w, 3) for w in Wa]))
    print("Offset (A): {}".format(round(ba, 3)))

    # -------- Escenario B: y normalizada a (0,1) --------
    print("\n" + "-" * 64)
    print("ESCENARIO B: sigmoide con 'y' normalizada a (0,1)")
    print("-" * 64)
    y_norm, lo, hi = normalizar_01(y)
    Wb, bb, _ = entrenar(X, y_norm, epochs=2000, lr=0.5)
    coste_b = mse(X, y_norm, Wb, bb)
    print("\nMSE final (B): {:.5f}   <- bajo: ahora sí aproxima".format(coste_b))
    print("Pesos (B): {}".format([round(w, 3) for w in Wb]))
    print("Offset (B): {}".format(round(bb, 3)))

    # Ejemplos de predicción (desnormalizando a la escala original de y)
    print("\nEjemplos (y_real  vs  y_estimado desnormalizado):")
    for i in range(5):
        est_norm = neurona(X[i], Wb, bb)
        est_real = est_norm * (hi - lo) + lo
        print("  y_real = {:7.3f}   y_est = {:7.3f}".format(y[i], est_real))

    print("\n" + "=" * 64)
    print("CONCLUSIÓN")
    print("=" * 64)
    print("- Con la sigmoide (derivable) el descenso de gradiente SÍ reduce el")
    print("  MSE, a diferencia del escalón on/off del Ejercicio 2.")
    print("- Pero la sigmoide acota la salida a (0,1): si 'y' se sale de ese")
    print("  rango (Escenario A) la recta no encaja. Normalizando 'y' a (0,1)")
    print("  (Escenario B) la neurona aproxima bien y el MSE baja mucho.")
    print("- Para una regresión lineal 'pura' sin escalar, la activación ideal")
    print("  sería la LINEAL (identidad); la sigmoide es mejor para salidas")
    print("  acotadas o probabilidades.")
