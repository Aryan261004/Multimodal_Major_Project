# Multimodal Content Moderation Project
## Work Completed So Far

---

## 1. Dataset Preparation

### TikHarm Dataset
- Total videos: 3948
- Train: 2762
- Val: 396
- Test: 790
- Classes:
  - Safe
  - Adult Content
  - Harmful Content
  - Suicide

### Preprocessing Steps
1. Verified video integrity using OpenCV.
2. Standardized all videos:
   - Resolution: 224x224
   - FPS: 30
3. Extracted:
   - 16 uniformly sampled frames per video
   - 16kHz mono audio (.wav)
4. Generated metadata CSV linking:
   - video_id
   - split
   - label
   - frame path
   - audio path

Final usable multimodal samples: 3947 (1 video missing audio).

---

## 2. Visual Baseline Model

### Model 1: R3D-18 (3D ResNet-18)
- Pretrained on Kinetics-400
- Modified final layer to 4 classes
- Multi-GPU training (2×T4)
- Batch size: increased for multi-GPU
- Optimizer: Adam / AdamW
- Weight decay applied
- Scheduler used

### Results (R3D-18)
- Best Validation Accuracy: ~79%
- Test Accuracy: ~75%
- Observed overfitting after epoch 2
- Indicates need for stronger backbone and better regularization

---

## 3. Improved Visual Model

### Model 2: Swin3D-T (Video Swin Transformer)
- Transformer-based spatiotemporal model
- Pretrained weights
- AdamW optimizer
- Cosine LR scheduler
- Label smoothing (0.1)
- Data augmentation added
- Multi-GPU compatible training

Goal: Achieve 85–90% validation accuracy.

---

## Current Status

- Clean preprocessing pipeline established
- Reproducible train/val/test splits
- Multi-GPU training setup operational
- Baseline visual-only results established
- Stronger transformer-based visual model implemented

Visual branch is now structured and extensible for multimodal fusion.