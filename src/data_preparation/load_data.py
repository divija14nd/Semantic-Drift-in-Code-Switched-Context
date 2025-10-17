from pathlib import Path
import pandas as pd
    
def get_csv(task: str, lang: str, variant: str):
    root = Path("LinCE_dataset")
    filename = f"{task}_{lang}_{variant}.csv"
    csv_path = root / filename

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    
    return csv_path
   

def load_dataframe(task: str, lang: str, variant: str):
    csv_path = get_csv(task, lang, variant)
    return pd.read_csv(csv_path)
