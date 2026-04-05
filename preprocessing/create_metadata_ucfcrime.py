import os
import csv

FRAME_ROOT = "datasets/UCF-Crime_frames_16"
AUDIO_ROOT = "datasets/UCF-Crime_audio"

OUTPUT_CSV = "metadata/ucfcrime_metadata.csv"

print("\n========== CREATING UCF-CRIME METADATA (WITH OPTIONAL AUDIO) ==========\n")

os.makedirs("metadata", exist_ok=True)

records = []
with_audio = 0
without_audio = 0

for label in os.listdir(FRAME_ROOT):
    frame_label_dir = os.path.join(FRAME_ROOT, label)
    audio_label_dir = os.path.join(AUDIO_ROOT, label)

    videos = os.listdir(frame_label_dir)

    for video in videos:
        frame_path = os.path.join(frame_label_dir, video)
        audio_path = os.path.join(audio_label_dir, video + ".wav")

        if os.path.exists(audio_path):
            audio_flag = 1
            with_audio += 1
        else:
            audio_flag = 0
            audio_path = ""   # empty if not available
            without_audio += 1

        records.append([
            video,
            frame_path,
            audio_path,
            label,
            audio_flag
        ])

# write CSV
with open(OUTPUT_CSV, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "video",
        "frame_path",
        "audio_path",
        "label",
        "audio_available"
    ])
    writer.writerows(records)

print("\n========== SUMMARY ==========")
print("Total samples:", len(records))
print("With audio:", with_audio)
print("Without audio:", without_audio)
print("Metadata saved to:", OUTPUT_CSV)
print("==============================================\n")