import os
import subprocess
from tqdm import tqdm


# Use absolute paths based on script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_ROOT = os.path.join(SCRIPT_DIR, "..", "datasets", "TikHarm_std")
AUDIO_ROOT = os.path.join(SCRIPT_DIR, "..", "datasets", "TikHarm_audio")

splits = ["train", "val", "test"]
classes = ["Adult Content", "Harmful Content", "Safe", "Suicide"]

print("\n========== AUDIO EXTRACTION (TikHarm) ==========\n")

total_audio = 0
failed_audio = 0

for split in splits:
    for cls in classes:
        in_dir = os.path.join(VIDEO_ROOT, split, cls)
        out_dir = os.path.join(AUDIO_ROOT, split, cls)
        os.makedirs(out_dir, exist_ok=True)

        videos = [v for v in os.listdir(in_dir) if v.endswith(".mp4")]
        print(f"{split}/{cls}: {len(videos)} videos")

        for video in tqdm(videos, desc=f"{split}/{cls}"):
            in_path = os.path.join(in_dir, video)
            out_path = os.path.join(out_dir, video.replace(".mp4", ".wav"))

            cmd = [
                "ffmpeg", "-y",
                "-i", in_path,
                "-ac", "1",
                "-ar", "16000",
                out_path
            ]
            result = subprocess.run(
                cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )

            if os.path.exists(out_path):
                total_audio += 1
            else:
                failed_audio += 1
                print(f"❌ Audio failed: {video}")

print("\n========== SUMMARY ==========")
print(f"Audio files created: {total_audio}")
print(f"Audio failures: {failed_audio}")
print("Audio saved in:", AUDIO_ROOT)
print("==============================================\n")