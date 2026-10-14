# Semana 7 — Redes Neuronales (Keras 3)

Entregables (challenges resueltos: código completo + preguntas conceptuales
respondidas):

- `Challenge_Keras3_CIFAR10_Grayscale.ipynb` — red *fully-connected* sobre
  CIFAR-10 convertido a escala de grises.
- `Challenge_Keras3_OlivettiFaces.ipynb` — clasificación de 40 rostros
  (Olivetti Faces).

También se incluye como referencia el notebook guiado de clase
`YourFirstDeepNN_FashionMNIST_Keras3.ipynb`.

## Ejecutar (recomendado: Google Colab)

1. Abre el notebook en [Google Colab](https://colab.research.google.com/).
2. Opcional pero recomendado: activa GPU
   (`Entorno de ejecución → Cambiar tipo de entorno → GPU`).
3. `Entorno de ejecución → Ejecutar todo`.

Colab ya trae Keras 3 y TensorFlow. Si ejecutas localmente:

```bash
pip install -r requirements.txt
```

> Los datasets (CIFAR-10 y Olivetti) se descargan automáticamente desde
> `keras.datasets` / `sklearn.datasets` al ejecutar.
