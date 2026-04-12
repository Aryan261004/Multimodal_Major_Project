import os
import shutil
import re

ROOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "datasets", "UCF-Crime")
DST = "datasets/UCF-Crime_clean"

VALID_FOLDERS = [
    "Anomaly-Videos-Part-1",
    "Anomaly-Videos-Part-2",
    "Anomaly-Videos-Part-3",
    "Anomaly-Videos-Part-4",
    "Normal_Videos_for_Event_Recognition"
]

os.makedirs(DST, exist_ok=True)

print("\n========== FINAL UCF-CRIME COLLECTION (CORRECT LABELING) ==========\n")

total_copied = 0
seen_files = set()
class_counts = {}

for folder in VALID_FOLDERS:
    src_dir = os.path.join(ROOT_DIR, folder)

    if not os.path.exists(src_dir):
        print(f"[SKIP] Missing: {folder}")
        continue

    print(f"[PROCESSING] {folder}")

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if not file.lower().endswith(".mp4"):
                continue

            if file in seen_files:
                continue
            seen_files.add(file)

            src_path = os.path.join(root, file)

            # 🔥 CORRECT LABEL EXTRACTION
            if "Normal" in file:
                label = "Normal"
            else:
                match = re.match(r"([A-Za-z]+)", file)
                label = match.group(1) if match else "Unknown"

            out_dir = os.path.join(DST, label)
            os.makedirs(out_dir, exist_ok=True)

            dst_path = os.path.join(out_dir, file)
            shutil.copy(src_path, dst_path)

            total_copied += 1
            class_counts[label] = class_counts.get(label, 0) + 1

print("\n========== CLASS DISTRIBUTION ==========")
for k, v in sorted(class_counts.items()):
    print(f"{k}: {v}")

print("\n========== SUMMARY ==========")
print("Total videos collected:", total_copied)
print("Unique videos:", len(seen_files))
print("Output folder:", DST)
print("==============================================\n")