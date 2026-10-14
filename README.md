# SI3003 — Introducción a la Inteligencia Artificial · Talleres

Repositorio individual con los entregables del componente práctico del curso
**SI3003 (EAFIT)**. Los talleres se basan en los notebooks del repositorio de la
clase ([EAFIT-IA/si3003-artificial-intelligence](https://github.com/EAFIT-IA/si3003-artificial-intelligence)).

> El número de **lecture** del repositorio de clase corresponde al número de
> **semana** (Lecture 04 → Semana 4, etc.).

## Entregables

| Semana | Carpeta | Tema | Entregable principal |
|---|---|---|---|
| **4** | [`semana4_mdp/`](semana4_mdp/) | MDPs | Laboratorio del robot de almacén (Value Iteration + Policy Iteration) |
| **6** | [`semana6_machine_learning/`](semana6_machine_learning/) | Machine Learning | Challenge de clasificación (dataset Wine): datos → entrenamiento → evaluación |
| **7** | [`semana7_redes_neuronales/`](semana7_redes_neuronales/) | Redes neuronales (Keras 3) | Challenges CIFAR-10 (grayscale) y Olivetti Faces |
| **8** | [`semana8_cnn_transfer_learning/`](semana8_cnn_transfer_learning/) | CNN / Transfer Learning | Taller de transfer learning con dataset propio |
| **9** | [`semana9_transformers_nlp/`](semana9_transformers_nlp/) | Transformers / NLP | Asistente de documentos (NVIDIA NIM) + reto de embeddings (Word2Vec) |

## Cómo ejecutar los notebooks

Cada carpeta de semana tiene su propio `README.md` con instrucciones detalladas.
En general:

- **Semana 4 y 6:** corren en **CPU** (Python + numpy/scikit-learn). Se pueden
  ejecutar localmente o en Google Colab en segundos.
- **Semana 7 y 8:** usan **Keras 3 / TensorFlow**. Se recomienda
  **Google Colab con GPU** (`Entorno de ejecución → Cambiar tipo → GPU`).
- **Semana 9:** el reto de embeddings corre en CPU; el asistente de documentos
  requiere una **API key de NVIDIA Build** (gratuita) en un archivo `.env`.

### Ejecutar en Google Colab (recomendado)

1. Sube el `.ipynb` a [Google Colab](https://colab.research.google.com/) (o
   ábrelo con `File → Open notebook → GitHub` apuntando a este repo).
2. Para semanas 7/8 activa GPU.
3. Ejecuta `Entorno de ejecución → Ejecutar todo`.

## Nota de integridad académica

Estos talleres son un trabajo **individual**. El uso de herramientas de IA está
permitido por el curso con transparencia e integridad académica.
