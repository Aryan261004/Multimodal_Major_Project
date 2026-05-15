import os
import cv2

ROOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "datasets", "UCF-Crime")

VALID_VIDEO_FOLDERS = [
    "Burglary",
    "Explosion",
    "Shooting",
    "FightingA_Part1",
    "FightingA_Part2",
    "FightingA_Part3",
    "FightingA_Part11",
    "Normal_Videos_for_Event_Recognition"
]

bad_videos = []
total_videos = 0

print("\n========== UCF-CRIME VIDEO INTEGRITY CHECK ==========\n")

for folder in VALID_VIDEO_FOLDERS:
    folder_path = os.path.join(ROOT_DIR, folder)

    if not os.path.exists(folder_path):
        print(f"[SKIP] Folder not found: {folder}")
        continue

    print(f"[CHECKING] Folder: {folder}")

    for video in os.listdir(folder_path):
        if not video.lower().endswith(".mp4"):
            continue

        total_videos += 1
        video_path = os.path.join(folder_path, video)
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"  ❌ Cannot open: {video}")
            bad_videos.append(video_path)

        cap.release()

print("\n========== SUMMARY ==========")
print(f"Total videos checked: {total_videos}")
print(f"Corrupted videos found: {len(bad_videos)}")

os.makedirs("logs", exist_ok=True)

if bad_videos:
    with open("logs/bad_ucfcrime_videos.txt", "w") as f:
        for v in bad_videos:
            f.write(v + "\n")
    print("❗ List saved to logs/bad_ucfcrime_videos.txt")
else:
    print("✅ All videos are readable.")

print("==============================================\n")