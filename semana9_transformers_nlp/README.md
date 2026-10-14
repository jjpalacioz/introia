# Semana 9 — Transformers / NLP

Entregables resueltos:

- `tokenization_Introduction.ipynb` — **reto de embeddings** con Word2Vec
  (`king - man + woman ≈ queen`, operaciones vectoriales con tu animal favorito y
  visualización PCA 3D). Corre en CPU.
- `05_ejercicio_nvidia_documentos.ipynb` — **asistente de documentos** sobre el
  paper *Attention Is All You Need* usando **NVIDIA NIM** (API compatible con
  OpenAI) + interfaz **Gradio**. Los 4 pasos de código y las reflexiones están
  resueltos.

Se incluyen como referencia los notebooks de clase de chatbots
(`01`–`04`).

## Ejecutar

### Reto de embeddings (`tokenization_Introduction.ipynb`)
Recomendado en Colab (la primera vez descarga el modelo Word2Vec, ~1.6 GB):

```bash
pip install gensim scikit-learn matplotlib
```

### Asistente de documentos (`05_ejercicio_nvidia_documentos.ipynb`)
1. Instala dependencias:
   ```bash
   pip install --upgrade pypdf gradio openai python-dotenv requests
   ```
2. Descarga el paper como `attention_is_all_you_need.pdf`:
   `https://arxiv.org/pdf/1706.03762`
3. Crea una **API key gratuita** en
   [NVIDIA Build](https://build.nvidia.com/settings/api-keys) y guárdala en un
   archivo `.env` junto al notebook:
   ```text
   NVIDIA_API_KEY="nvapi-...."
   ```
4. Ejecuta el notebook. Se abrirá una interfaz Gradio para preguntar sobre el paper.

> El archivo `.env` y el PDF **no se versionan** (ver `.gitignore`): la API key es
> personal y no debe subirse a GitHub.
