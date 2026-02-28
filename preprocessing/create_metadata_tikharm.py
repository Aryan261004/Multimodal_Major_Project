import os
import csv


# Use absolute paths based on script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FRAME_ROOT = os.path.join(SCRIPT_DIR, "..", "datasets", "TikHarm_frames_16")
AUDIO_ROOT = os.path.join(SCRIPT_DIR, "..", "datasets", "TikHarm_audio")
OUT_CSV = os.path.join(SCRIPT_DIR, "..", "metadata", "tikharm_metadata.csv")

os.makedirs("metadata", exist_ok=True)

print("\n========== CREATING TikHarm METADATA ==========\n")

records = 0
missing_audio = 0

with open(OUT_CSV, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "video_id", "split", "label", "frame_dir", "audio_path"
    ])

    for split in ["train", "val", "test"]:
        for label in ["Adult Content", "Harmful Content", "Safe", "Suicide"]:
            frame_base = os.path.join(FRAME_ROOT, split, label)
            audio_base = os.path.join(AUDIO_ROOT, split, label)

            for video_id in os.listdir(frame_base):
                frame_dir = os.path.join(frame_base, video_id)
                audio_path = os.path.join(audio_base, video_id + ".wav")

                if not os.path.exists(audio_path):
                    missing_audio += 1
                    continue  # safe skip

                writer.writerow([
                    video_id, split, label, frame_dir, audio_path
                ])
                records += 1

print("========== SUMMARY ==========")
print(f"Total records written: {records}")
print(f"Videos skipped due to missing audio: {missing_audio}")
print("Metadata saved to:", OUT_CSV)
print("==============================================\n")