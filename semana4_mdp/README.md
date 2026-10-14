# Semana 4 — MDPs

**Entregable:** `03_lab_warehouse_mdp.ipynb`

Laboratorio del robot de entregas en un almacén 5×6. Se modela el MDP y se
resuelve con **Value Iteration** y **Policy Iteration**, verificando que ambos
convergen a la misma política óptima. Incluye los experimentos A/B/C y el bonus.

## Ejecutar

Solo requiere Python + NumPy (CPU):

```bash
pip install numpy
jupyter notebook 03_lab_warehouse_mdp.ipynb
```

O en Google Colab: `Entorno de ejecución → Ejecutar todo`.

> El layout del almacén se definió respetando todas las reglas del enunciado
> (START, estanterías, +10/+2/-10 terminales, peligros -3, piso resbaloso,
> costo por paso -1). Es fácil de ajustar si se desea calcar la imagen original.
