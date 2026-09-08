import json
import pickle
from pathlib import Path

import pandas as pd
import yaml
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split


def main():
    with open("params.yaml") as f:
        params = yaml.safe_load(f)

    test_size = params["train"]["test_size"]
    random_state = params["train"]["random_state"]

    df = pd.read_csv("data/processed.csv")
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    _, X_test, _, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, average="weighted", zero_division=0),
        "recall": recall_score(y_test, y_pred, average="weighted", zero_division=0),
        "f1_score": f1_score(y_test, y_pred, average="weighted", zero_division=0),
    }

    Path("metrics").mkdir(parents=True, exist_ok=True)
    with open("metrics/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
    print(metrics)

if __name__ == "__main__":
    main()
