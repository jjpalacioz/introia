# Gemma 4 – Vision Token Budget

## 1. Nombre del Space

- **Nombre:** Gemma 4 – Vision Token Budget
- **Enlace:** https://huggingface.co/spaces/google/gemma4_vision_token_budget

## 2. ¿Qué hace el agente?

Es una herramienta que toma una imagen (subida por el usuario o una de muestra, como la palmera) y genera varias versiones redimensionadas de esa imagen, cada una ajustada a un presupuesto distinto de tokens visuales (70, 140, 280, 560, 1120).

Sirve para visualizar cuánto detalle "ve" un modelo como Gemma dependiendo de cuántos tokens se le permiten para procesar una imagen.

## 3. Análisis PEAS

| Elemento | Respuesta |
|---|---|
| **Performance** | Que las imágenes generadas mantengan la proporción original correctamente, que el cálculo de tokens sea preciso, y que la reducción de calidad sea coherente con el presupuesto asignado (menos tokens = menos resolución, de forma predecible). |
| **Environment** | La imagen que el usuario sube o selecciona, y la interfaz web donde se muestran los resultados. |
| **Actuators** | Generar y mostrar las versiones redimensionadas de la imagen, mostrar las nuevas dimensiones (ancho x alto) y el conteo de tokens correspondiente a cada versión. |
| **Sensors** | La imagen cargada por el usuario (o seleccionada de las muestras) y su resolución original. |

## 4. Clasificación del entorno

| Propiedad | Clasificación | Justificación |
|---|---|---|
| **Observable** | Total | El agente tiene acceso completo a toda la información que necesita (la imagen completa) para hacer su tarea; no hay información oculta. |
| **Determinista** | Sí | Dado el mismo input (misma imagen, mismo presupuesto de tokens), el resultado (dimensiones y calidad de salida) siempre será el mismo. |
| **Episódico** | Sí | Cada imagen se procesa de forma independiente; el resultado de un episodio (una imagen) no depende de imágenes anteriores. |
| **Estático** | Sí | La imagen no cambia mientras el agente la está procesando; no hay elementos dinámicos externos actuando durante el cálculo. |
| **Discreto** | Sí | Los presupuestos de tokens son valores fijos y discretos (70, 140, 280, 560, 1120), no un rango continuo. |
| **Conocido** | Sí | Las reglas de cómo se calculan los tokens a partir del tamaño de imagen son conocidas y fijas (es un algoritmo definido, no algo que el agente deba aprender o descubrir). |

## 5. ¿Qué tipo de programa de agente es?

**Agente de reflejo simple.**

**Justificación:** el sistema no mantiene un estado interno del mundo, no persigue objetivos complejos ni evalúa utilidades; simplemente aplica una función/regla fija: recibe una imagen y un presupuesto de tokens como entrada, y produce una salida (imagen redimensionada + dimensiones) a partir de un cálculo determinista, sin necesidad de "recordar" interacciones pasadas ni razonar sobre consecuencias futuras. Es, en esencia, condición-acción: "si el presupuesto es X tokens, entonces la imagen se redimensiona a Y dimensiones".
