import cv2
import os
import numpy as np
from tqdm import tqdm

VIDEO_ROOT = "datasets/UCF-Crime_std"
FRAME_ROOT = "datasets/UCF-Crime_frames_16"

NUM_FRAMES = 16

print("\n========== FRAME EXTRACTION (UCF-CRIME) ==========\n")

total_videos = 0
short_videos = 0

for label in os.listdir(VIDEO_ROOT):
    video_dir = os.path.join(VIDEO_ROOT, label)
    videos = [v for v in os.listdir(video_dir) if v.endswith(".mp4")]

    print(f"{label}: {len(videos)} videos")

    for video in tqdm(videos, desc=label):
        total_videos += 1

        path = os.path.join(video_dir, video)
        cap = cv2.VideoCapture(path)

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        if total_frames < NUM_FRAMES:
            short_videos += 1
            print(f"⚠️ Too short: {video}")
            cap.release()
            continue

        # uniform sampling
        frame_indices = np.linspace(0, total_frames - 1, NUM_FRAMES, dtype=int)

        save_dir = os.path.join(
            FRAME_ROOT,
            label,
            video.replace(".mp4", "")
        )
        os.makedirs(save_dir, exist_ok=True)

        count = 0
        for idx in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()

            if ret:
                cv2.imwrite(os.path.join(save_dir, f"{count}.jpg"), frame)
                count += 1

        cap.release()

print("\n========== SUMMARY ==========")
print("Total videos processed:", total_videos)
print("Videos too short:", short_videos)
print("Frames saved in:", FRAME_ROOT)
print("==============================================\n")