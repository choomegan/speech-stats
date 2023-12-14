import os
import tqdm
import hydra
import subprocess
from omegaconf import DictConfig


@hydra.main(version_base=None, config_path="../conf", config_name="config")
def change_sr_br_channel(cfg: DictConfig) -> None:
    """
    Change sampling rate, bit rate and channel
    """
    os.makedirs(f"{os.path.dirname(cfg.audio_dir)}/resampled", exist_ok=True)

    for audio_file in tqdm.tqdm(os.listdir(cfg.audio_dir)):
        subprocess.call(
            f"ffmpeg -i {cfg.audio_dir}/{audio_file} -ar 16000 -ac 1 -b:a 256k {os.path.dirname(cfg.audio_dir)}/resampled/{audio_file}",
            shell=True,
        )


if __name__ == "__main__":
    change_sr_br_channel()
