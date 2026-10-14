# Semana 8 — CNN / Transfer Learning

**Entregable:** `taller_transfer_learning_datos_propios_keras3.ipynb`

Taller completo de transfer learning con **EfficientNetB0** (ImageNet):

- Problema de 3 clases definido (**gato / perro / caballo**).
- Descarga automática del dataset propio con `ddgs` (buscador de imágenes).
- Split train/validation/test, data augmentation.
- Entrenamiento con backbone congelado + **fine-tuning**.
- Matriz de confusión, análisis de errores y conclusiones (TODOs 1–6 resueltos).

Se incluye como referencia el notebook guiado de clase `CNN_Transfer_Keras3.ipynb`.

## Ejecutar (recomendado: Google Colab con GPU)

1. Abre `taller_transfer_learning_datos_propios_keras3.ipynb` en
   [Google Colab](https://colab.research.google.com/).
2. Activa **GPU** (`Entorno de ejecución → Cambiar tipo de entorno → GPU`).
3. `Entorno de ejecución → Ejecutar todo`.

La primera celda instala `ddgs`. Las imágenes se descargan al ejecutar; si una
clase trae resultados pobres, mejora los términos de búsqueda en `SEARCHES`
(ya definidos). El dataset no se versiona en git (ver `.gitignore`).

> Puedes cambiar las 3 clases por el problema que prefieras editando `SEARCHES`.
