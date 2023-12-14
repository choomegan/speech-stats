import numpy as np
import hydra
import logging
from omegaconf import DictConfig
from utils.manifest import load_manifest

logging.basicConfig(
    format="%(levelname)s | %(asctime)s | %(message)s", level=logging.INFO
)

@hydra.main(version_base=None, config_path="../conf", config_name="config")
def calc_duration(cfg: DictConfig) -> float:
    """
    Calculate duration from manifest file
    """
    data = load_manifest(cfg.manifest_path)
    duration = 0
    duration_list = []
    for row in data:
        duration += row["duration"]
        duration_list.append(row["duration"])

    logging.info(f"min duration: {np.min(duration_list)}")
    logging.info(f"max duration: {np.max(duration_list)}")
    logging.info(f"avg duration: {np.mean(duration_list)}")
    logging.info(f"total duration: {round(duration / 3600, 3)}")
    return round(duration / 3600, 3)


if __name__ == "__main__":
    calc_duration()
