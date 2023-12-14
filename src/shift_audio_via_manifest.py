import os
import shutil
import tqdm
import hydra
from omegaconf import DictConfig
from utils.manifest import load_manifest


@hydra.main(version_base=None, config_path="../conf", config_name="config")
def shift_audio_via_manifest(cfg: DictConfig) -> None:
    """
    Using audio filepaths in manifest, shift all mentioned audio clips 
    into a new audio folder
    """
    data = load_manifest(cfg.manifest_path)

    base_dir = os.path.dirname(cfg.manifest_path)
    os.makedirs(os.path.join(base_dir, cfg.shift_audio.out_folder), exist_ok=True)

    for line in tqdm.tqdm(data):
        src_path = os.path.join(base_dir, line["audio_filepath"])
        print(os.path.exists(src_path))
        dest_path = os.path.join(
            base_dir, cfg.shift_audio.out_folder, os.path.basename(src_path)
        )
        shutil.move(src_path, dest_path)

if __name__ == "__main__":
    shift_audio_via_manifest()
