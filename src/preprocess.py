import pandas as pd
from pathlib import Path

def main():
    input_path = Path("data/dataset.csv")
    output_path = Path("data/processed.csv")
    df = pd.read_csv(input_path)
    df = df.dropna()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Processed {len(df)} rows -> {output_path}")

if __name__ == "__main__":
    main()
