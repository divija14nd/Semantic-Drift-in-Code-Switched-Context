# Semantic-Drift-in-Code-Switched-Context

To run project, execute the command with the parameters as follows:

    --task = lid, ner, pos, sa
    --lang = lid:[hineng, msaea, nepeng, spaeng]
             ner:[hineng, msaea, spaeng]
             pos:[hineng, spaeng]
              sa:[spaeng]
    --variant = train, validation, test
    --file_format = csv

    example:
    python <path/to/project>/scripts/execute.py --task lid --lang hineng --variant train --file_format csv
