# Ejercicio 3 — Neurona con activación sigmoide, coste MSE y offset

## Enunciado

Partiendo del [Ejercicio 2](Ejercicio2-Regresion-Lineal-Simple.md) (neurona de
5 entradas), ahora:

- Incluir como **función de coste el MSE** (`y_real` vs `y_est`).
- Cambiar la función de activación a **sigmoide**.
- Incluir **offset** (bias `b`).
- Repetir la estimación de la recta (los `W_i`).

## Archivos

- [`ejercicio3_neurona_sigmoide.py`](ejercicio3_neurona_sigmoide.py) —
  implementación (solo librería estándar de Python, sin dependencias).

## Cómo ejecutar

```bash
python3 ejercicio3_neurona_sigmoide.py
```

## Formulación

```
z      = sum(w_i * x_i) + b          (incluye offset b)
y_est  = sigmoide(z) = 1 / (1 + e^-z)
coste  = MSE = (1/N) * sum( (y - y_est)^2 )
```

A diferencia del escalón on/off del Ejercicio 2, la **sigmoide es derivable**,
así que ahora hay gradiente útil y se puede entrenar por **descenso de
gradiente**:

```
s'(z)      = s(z) * (1 - s(z))
dMSE/dw_i  = (2/N) * sum( (y_est - y) * s'(z) * x_i )
dMSE/db    = (2/N) * sum( (y_est - y) * s'(z) )
```

## Un detalle importante: el rango de la sigmoide

La sigmoide solo produce valores en **(0, 1)**. La `y` real de este problema
está en `[-4.25, 8.48]`, fuera de ese rango. Por eso el script prueba **dos
escenarios**:

### Escenario A — `y` sin escalar

```
Época    0 | MSE = 8.05952
...
Época 1999 | MSE = 6.31352

MSE final (A): 6.31352   <- alto: la recta NO encaja
```

El MSE mejora respecto al azar inicial pero **se estanca alto**: la sigmoide no
puede alcanzar valores fuera de (0,1).

### Escenario B — `y` normalizada a (0, 1)

```
Época    0 | MSE = 0.04894
...
Época 1999 | MSE = 0.00046

MSE final (B): 0.00046   <- bajo: ahora sí aproxima

Ejemplos (y_real  vs  y_estimado desnormalizado):
  y_real =  -0.154   y_est =  -0.304
  y_real =  -2.370   y_est =  -2.060
  y_real =   1.872   y_est =   2.023
  y_real =  -0.220   y_est =  -0.325
  y_real =  -1.053   y_est =  -1.085
```

Al normalizar la salida al rango de la sigmoide, la neurona **aproxima bien** la
recta y el MSE baja muchísimo. Los `y_estimado` (desnormalizados) siguen de
cerca a los `y_real`.

## Comparación con el Ejercicio 2

| Aspecto              | Ej. 2 (on/off)         | Ej. 3 (sigmoide)                    |
|----------------------|------------------------|-------------------------------------|
| Salida               | Solo 0 ó 1             | Continua en (0, 1)                  |
| ¿Derivable?          | No                     | Sí                                  |
| Entrenamiento        | Ajuste tipo perceptrón | Descenso de gradiente sobre el MSE  |
| Coste MSE            | Estancado (~6.46)      | A: ~6.31 · **B (normalizada): ~0.0005** |
| ¿Aproxima la recta?  | No                     | Sí (con `y` en el rango de la sigmoide) |

## Conclusión

- La sigmoide, al ser derivable, permite que el descenso de gradiente **reduzca
  el MSE de verdad** (imposible con el escalón del Ejercicio 2).
- Aun así, la sigmoide **acota la salida a (0, 1)**: si la `y` se sale de ese
  rango hay que normalizarla (Escenario B) para que la neurona pueda aproximarla.
- Para una regresión lineal "pura" sin escalar, la activación ideal sería la
  **lineal (identidad)**; la sigmoide encaja mejor cuando la salida es acotada o
  representa una probabilidad.
