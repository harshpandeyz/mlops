import pickle
from pathlib import Path

import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def main():
    with open("params.yaml") as f:
        params = yaml.safe_load(f)

    test_size = params["train"]["test_size"]
    random_state = params["train"]["random_state"]
    n_estimators = params["model"]["n_estimators"]
    max_depth = params["model"]["max_depth"]

    df = pd.read_csv("data/processed.csv")
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    X_train, _, y_train, _ = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    model = RandomForestClassifier(
        n_estimators=n_estimators, max_depth=max_depth, random_state=random_state
    )
    model.fit(X_train, y_train)

    Path("models").mkdir(parents=True, exist_ok=True)
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)
    print(f"Trained RandomForest(n_estimators={n_estimators}, max_depth={max_depth})")

if __name__ == "__main__":
    main()
