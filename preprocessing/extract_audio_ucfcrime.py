import os
import subprocess
from tqdm import tqdm

VIDEO_ROOT = "datasets/UCF-Crime_std"
AUDIO_ROOT = "datasets/UCF-Crime_audio"

print("\n========== AUDIO EXTRACTION (UCF-CRIME) ==========\n")

total_audio = 0
failed_audio = 0

for label in os.listdir(VIDEO_ROOT):
    in_dir = os.path.join(VIDEO_ROOT, label)
    out_dir = os.path.join(AUDIO_ROOT, label)
    os.makedirs(out_dir, exist_ok=True)

    videos = [v for v in os.listdir(in_dir) if v.endswith(".mp4")]

    print(f"{label}: {len(videos)} videos")

    for video in tqdm(videos, desc=label):
        in_path = os.path.join(in_dir, video)
        out_path = os.path.join(out_dir, video.replace(".mp4", ".wav"))

        cmd = [
            "ffmpeg", "-y",
            "-i", in_path,
            "-vn",              # remove video
            "-ac", "1",         # mono
            "-ar", "16000",     # 16kHz
            out_path
        ]

        subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if os.path.exists(out_path):
            total_audio += 1
        else:
            failed_audio += 1
            print(f"❌ Failed: {video}")

print("\n========== SUMMARY ==========")
print("Audio files created:", total_audio)
print("Failed audio extractions:", failed_audio)
print("Audio saved in:", AUDIO_ROOT)
print("==============================================\n")