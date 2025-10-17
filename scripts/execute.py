import sys
from pathlib import Path
import argparse

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.append(str(SRC_DIR))

from data_preparation.prepare_data import prepare_variant, write_output_file


def main():
    parser = argparse.ArgumentParser(description="Execute data preparation pipeline.")
    parser.add_argument("--task", required=True, choices=["lid", "ner", "pos", "sa"])
    parser.add_argument("--lang", required=True, choices=["hineng", "msaea", "nepeng", "spaeng"])
    parser.add_argument("--variant", required=True, choices=["train", "validation", "test"])
    parser.add_argument("--file_format", default="csv")
    
    args = parser.parse_args()

    df = prepare_variant(args.task, args.lang, args.variant)
    write_output_file(df, args.task, args.lang, args.variant, file_format=args.file_format)

if __name__ == "__main__":
    main()
