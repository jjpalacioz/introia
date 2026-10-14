# Semana 6 — Machine Learning

Challenge de clasificación sobre el dataset **Wine** (3 variedades, 13 features).
Son **3 notebooks que se ejecutan en orden**:

1. `01_data_challenge.ipynb` — carga, profiling, split estratificado y EDA.
   Genera `data/processed/train.csv`, `data/processed/test.csv` y
   `artifacts/data_contract.json`.
2. `02_training_challenge.ipynb` — pipelines, comparación de 3 modelos
   (DecisionTree, LogisticRegression, KNN), tuning con `GridSearchCV` y
   selección del campeón. Genera `champion_model.joblib`,
   `training_metadata.json` y `reports/cv_results.csv`.
3. `03_evaluation_deployment_challenge.ipynb` — evaluación final en test,
   función de inferencia y predicción por lotes. Genera `reports/test_metrics.json`
   y `reports/batch_predictions.csv`.

## Datos

El dataset ya está incluido en `data/raw/wine.csv`.

## Ejecutar

```bash
pip install -r requirements.txt
```

Luego ejecuta los notebooks **en orden** (1 → 2 → 3). Corre en CPU en segundos.
Las carpetas `data/processed`, `artifacts` y `reports` se crean automáticamente.
