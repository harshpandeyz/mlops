# Iris ML Experiment Pipeline using Git + DVC

## 1. Project Objective
Train a Random Forest classifier on the Iris dataset with a reproducible Git + DVC pipeline and compare two experiments.

## 2. Technologies Used
Python, pandas, scikit-learn, Git, GitHub, DVC, Random Forest.

## 3. Project Structure
```text
current-folder/
├── data/
│   ├── dataset.csv
│   └── processed.csv
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── models/
│   └── model.pkl
├── metrics/
│   └── metrics.json
├── params.yaml
├── dvc.yaml
├── dvc.lock
├── requirements.txt
├── README.md
└── .gitignore
```

## 4. DVC Pipeline
Three stages: `preprocess` (data/dataset.csv -> data/processed.csv), `train` (data/processed.csv -> models/model.pkl), `evaluate` (models/model.pkl -> metrics/metrics.json).
```text
Raw Dataset -> Preprocessing -> Processed Dataset -> Training -> Model -> Evaluation -> Metrics
```

## 5. Parameters
`params.yaml` controls the split and model:
```yaml
train:
  test_size: 0.2
  random_state: 42
model:
  n_estimators: 100
  max_depth: 5
```

## 6. Experiment 1
Initial run with `n_estimators=100, max_depth=5`.
Commit: `Experiment 1: Initial Iris ML pipeline`

## 7. Experiment 2
Updated run with `n_estimators=200, max_depth=10`.
Commit: `Experiment 2: Updated Random Forest parameters`

## 8. Reproduction Commands
```bash
pip install -r requirements.txt
dvc pull  # if remote configured
dvc repro
dvc metrics show
dvc metrics diff
dvc dag
git log --oneline
```
Track dataset: `dvc add data/dataset.csv`
