from pathlib import Path
import pandas as pd
from .load_data import load_dataframe
from .preprocess_data import apply_clean

def prepare_variant(task: str, lang: str, variant: str):
    df = load_dataframe(task, lang, variant)
    df = apply_clean(df)
    return df

def write_output_file(df, task, lang, variant, file_format='csv'):
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{task}_{lang}_{variant}.{file_format}"

    if file_format == 'csv':
        df.to_csv(output_path, index=False)

    print(f"Data written to {output_path}")
