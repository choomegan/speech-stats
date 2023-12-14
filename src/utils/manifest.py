import json
from typing import List, Dict, Union, Optional


def load_manifest(manifest_path: str) -> List[Dict[str, str]]:
    """
    Load manifest file
    """
    data = []
    with open(manifest_path, "r") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def save_manifest(items: List[Dict[str, str]], save_path: str) -> None:
    with open(save_path, "w") as fw:
        for item in items:
            fw.write(json.dumps(item, ensure_ascii=False) + "\n")
