# Project Roadmap – Next Steps

---

## Phase 1: Finalize Strong Visual Baseline
- Train Swin3D-T to convergence (15–20 epochs)
- Save best checkpoint based on validation accuracy
- Report:
  - Validation accuracy
  - Test accuracy
  - Confusion matrix
  - Per-class precision/recall/F1

---

## Phase 2: Audio Baseline

### Model: VGGish or Audio Spectrogram Transformer (AST)
Steps:
1. Convert audio to log-mel spectrogram
2. Use pretrained audio backbone
3. Train 4-class classifier
4. Evaluate:
   - Validation accuracy
   - Test accuracy

Compare:
- Visual-only vs Audio-only

---

## Phase 3: Multimodal Fusion (Core Contribution)

### Baseline Fusion
- Late fusion (average probabilities)
- Weighted late fusion

### Advanced Fusion
- Attention-based fusion
- Gated multimodal unit
- Transformer-based cross-modal fusion

---

## Phase 4: Confidence-Aware Mechanism

Implement:
- Softmax confidence scoring
- Entropy-based uncertainty
- Monte Carlo dropout (optional)

Goal:
Improve reliability of moderation decisions.

---

## Phase 5: Explainability

Add:
- Grad-CAM for visual branch
- Attention visualization for fusion
- Modality contribution analysis

---

## Phase 6: Evaluation Strategy

Report:
- Accuracy
- Precision
- Recall
- F1-score (macro)
- Confusion matrix
- ROC curves (if needed)

Evaluate:
- Per-class robustness
- Sensitivity to harmful categories

---

## Final Deliverable

A confidence-aware, explainable multimodal moderation framework capable of:

- Safe
- Mildly Sensitive
- Explicit / Violent classification

with strong empirical comparison against unimodal baselines.