import os
import subprocess
from tqdm import tqdm

IN_ROOT = "datasets/UCF-Crime_clean"
OUT_ROOT = "datasets/UCF-Crime_std"

print("\n========== STANDARDIZING UCF-CRIME DATASET ==========\n")

total_processed = 0
failed_videos = 0

for label in os.listdir(IN_ROOT):
    in_dir = os.path.join(IN_ROOT, label)
    out_dir = os.path.join(OUT_ROOT, label)
    os.makedirs(out_dir, exist_ok=True)

    videos = [v for v in os.listdir(in_dir) if v.endswith(".mp4")]

    print(f"{label}: {len(videos)} videos")

    for video in tqdm(videos, desc=label):
        in_path = os.path.join(in_dir, video)
        out_path = os.path.join(out_dir, video)

        cmd = [
            "ffmpeg", "-y",
            "-i", in_path,
            "-vf", "scale=224:224",
            "-r", "30",
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "23",
            out_path
        ]

        result = subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if os.path.exists(out_path):
            total_processed += 1
        else:
            failed_videos += 1
            print(f"❌ Failed: {video}")

print("\n========== SUMMARY ==========")
print(f"Total videos processed: {total_processed}")
print(f"Failed videos: {failed_videos}")
print("Output folder:", OUT_ROOT)
print("==============================================\n")