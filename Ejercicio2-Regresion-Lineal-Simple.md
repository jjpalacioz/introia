# Ejercicio 2 — Regresión Lineal Simple con una neurona artificial

## Enunciado

Usar una **neurona artificial de 5 entradas**, de forma iterativa, para encontrar
los mejores `W_i` que acerquen `y_estimado` al `y` generado.

Función de activación: **on/off** (escalón / step):

```
y = f( sum(w_i * x_i) )

f(z) = 1  si z >= 0
f(z) = 0  si z < 0
```

> **Se espera que falle** — que dé un mal resultado. Ese es precisamente el
> objetivo pedagógico del ejercicio.

## Archivos

- [`ejercicio2_neurona_onoff.py`](ejercicio2_neurona_onoff.py) — implementación
  (solo librería estándar de Python, sin dependencias externas).

## Cómo ejecutar

```bash
python3 ejercicio2_neurona_onoff.py
```

## Qué hace el código

1. **Genera los datos:** 100 muestras con 5 entradas cada una. La salida `y`
   se produce con una combinación lineal real:
   `y = 2·x1 − 1·x2 + 0.5·x3 + 3·x4 − 2.5·x5 + 1.5 + ruido`.
   Por tanto `y` es un valor **continuo**.
2. **Neurona:** calcula `z = sum(w_i · x_i) + b` y le aplica la activación
   on/off, de modo que la salida solo puede ser **0 ó 1**.
3. **Entrenamiento iterativo:** ajusta los pesos época a época usando el error
   `y − y_estimado` (estilo regla del perceptrón).

## Resultado obtenido (fallo esperado)

```
Época   0 | MSE =   9.5143
Época  20 | MSE =   6.4564
Época  40 | MSE =   6.4564
...
Época 199 | MSE =   6.4564

MSE final: 6.4564   (cuanto más alto, peor)
Rango real de y:        [-4.25, 8.48]
Valores de y_estimado:  [0.0, 1.0]  <- ¡solo 0 y/o 1!
```

El error (MSE) se **estanca** muy pronto y se queda alto: el modelo no aprende.

## ¿Por qué falla?

1. **La salida es binaria.** La activación on/off solo puede devolver `0` ó `1`,
   mientras que la `y` real es un número continuo en un rango amplio
   (aquí `[-4.25, 8.48]`). Es **matemáticamente imposible** aproximar una
   regresión lineal con una salida que solo toma dos valores.
2. **No es derivable.** La función escalón tiene derivada 0 en casi todos los
   puntos (e indefinida en el salto). No existe un **gradiente útil**, así que
   los ajustes de peso no reducen el error de forma coherente y el aprendizaje
   se estanca.

## ¿Qué habría que hacer para que funcione?

Para un problema de **regresión lineal** hay que usar una **activación lineal**
(la identidad, `f(z) = z`) y entrenar con **descenso de gradiente** minimizando
el error cuadrático medio. Con eso los pesos convergerían hacia los pesos reales
`[2.0, −1.0, 0.5, 3.0, −2.5]` y el bias `1.5`.

La activación on/off es adecuada para **clasificación binaria**, no para
regresión.
