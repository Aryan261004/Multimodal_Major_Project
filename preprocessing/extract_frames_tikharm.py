import cv2
import os
import numpy as np
from tqdm import tqdm


# Use absolute paths based on script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_ROOT = os.path.join(SCRIPT_DIR, "..", "datasets", "TikHarm_std")
FRAME_ROOT = os.path.join(SCRIPT_DIR, "..", "datasets", "TikHarm_frames_16")

NUM_FRAMES = 16
splits = ["train", "val", "test"]
classes = ["Adult Content", "Harmful Content", "Safe", "Suicide"]

print("\n========== FRAME EXTRACTION (TikHarm) ==========\n")

short_videos = 0
total_videos = 0

for split in splits:
    for cls in classes:
        video_dir = os.path.join(VIDEO_ROOT, split, cls)
        videos = [v for v in os.listdir(video_dir) if v.endswith(".mp4")]

        print(f"{split}/{cls}: {len(videos)} videos")

        for video in tqdm(videos, desc=f"{split}/{cls}"):
            total_videos += 1
            cap = cv2.VideoCapture(os.path.join(video_dir, video))
            total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            if total < NUM_FRAMES:
                print(f"⚠️  Too short: {video} ({total} frames)")
                short_videos += 1
                cap.release()
                continue

            idxs = np.linspace(0, total - 1, NUM_FRAMES, dtype=int)

            save_dir = os.path.join(
                FRAME_ROOT, split, cls, video.replace(".mp4", "")
            )
            os.makedirs(save_dir, exist_ok=True)

            for i in idxs:
                cap.set(cv2.CAP_PROP_POS_FRAMES, i)
                ret, frame = cap.read()
                if ret:
                    cv2.imwrite(os.path.join(save_dir, f"{i}.jpg"), frame)

            cap.release()

print("\n========== SUMMARY ==========")
print(f"Total videos processed: {total_videos}")
print(f"Videos too short: {short_videos}")
print("Frames saved in:", FRAME_ROOT)
print("==============================================\n")