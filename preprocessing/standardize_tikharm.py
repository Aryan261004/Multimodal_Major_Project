import os
import subprocess
from tqdm import tqdm

ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "datasets", "TikHarm")
OUT_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "datasets", "TikHarm_std")

splits = ["train", "val", "test"]
classes = ["Adult Content", "Harmful Content", "Safe", "Suicide"]

print("\n========== STANDARDIZING TikHarm VIDEOS ==========\n")

total_processed = 0

for split in splits:
    for cls in classes:
        in_dir = os.path.join(ROOT, split, cls)
        out_dir = os.path.join(OUT_ROOT, split, cls)
        os.makedirs(out_dir, exist_ok=True)

        videos = [v for v in os.listdir(in_dir) if v.endswith(".mp4")]
        print(f"{split}/{cls}: {len(videos)} videos")

        for video in tqdm(videos, desc=f"{split}/{cls}"):
            in_path = os.path.join(in_dir, video)
            out_path = os.path.join(out_dir, video)

            cmd = [
                "ffmpeg", "-y",
                "-i", in_path,
                "-vf", "scale=224:224",
                "-r", "30",
                out_path
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            total_processed += 1

print("\n========== SUMMARY ==========")
print(f"Total TikHarm videos standardized: {total_processed}")
print("Output folder:", OUT_ROOT)
print("==============================================\n")