# Transformer Block with Learnable Kernel Functions

Inspired by the paper **“Linear Transformers with Learnable Kernel Functions Are Better In-Context Models”**, this module replaces the standard softmax attention with a **learnable kernel function**.

<div align="center">
  <img src="https://github.com/user-attachments/assets/76135220-d9a4-4ec4-9c97-4a6f4576dd88" alt="Learnable Kernel Functions" width="60%"/>
  <p><em>Figure 1: Learnable kernel functions in place of softmax.</em></p>
</div>

---

# Channel–Spatial Attention

Before applying spatial attention, we first enhance channel-wise features using an **Efficient Channel Attention (ECA)** block. This combined **Channel–Spatial Attention** block is described below.

<div align="center">
  <img src="https://github.com/user-attachments/assets/af0c52da-5d4d-4638-8289-aa39dd8d4f87" alt="Channel-Spatial Attention Block" width="60%"/>
  <p><em>Figure 2: Overview of the Channel–Spatial Attention block.</em></p>
</div>

## Efficient Channel Attention (ECA) Block

The ECA module adaptively weights feature channels without dimensionality reduction, preserving cross-channel interactions.

<div align="center">
  <img src="https://github.com/user-attachments/assets/54152e61-8f0f-4af4-8c21-60d45e730e59" alt="ECA Block" width="50%"/>
  <p><em>Figure 3: Structure of the ECA block.</em></p>
</div>

## Spatial Attention (SA) Block

The SA module focuses on the most informative spatial regions by generating a spatial attention map.

<div align="center">
  <img src="https://github.com/user-attachments/assets/7692e4ec-c8f1-4256-b954-5b86253bf794" alt="SA Block" width="50%"/>
  <p><em>Figure 4: Structure of the Spatial Attention block.</em></p>
</div>

---

# Area Attention in YOLOv12

This repository also implements an **Area Attention** method adapted from **YOLOv12**, allowing the detector to attend over variable-shaped regions for more flexible feature aggregation.

---

# References

1. **Ultralytics YOLO**  
   Jocher, G., Qiu, J., & Chaurasia, A. (2023). *Ultralytics YOLO (Version 8.0.0)* [Computer software]. https://github.com/ultralytics/ultralytics

2. **Attention Is All You Need**  
   Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomes, A., Kaiser, Ł., & Polosukhin, I. (2017). _Advances in Neural Information Processing Systems_, 30, 5998–6008.

3. **You Only Look Once: Unified, Real-Time Object Detection**  
   Redmon, J., Divvala, S., Girshick, R., & Farhadi, A. (2016). In _Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition_ (pp. 779–788).

4. **ECA‑Net: Efficient Channel Attention for Deep Convolutional Neural Networks**  
   Wang, Q., Wu, B., Zhu, P., Li, P., Zuo, W., & Hu, Q. (2020). In _2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition_ (pp. 11534–11542).

5. **Linear Transformers with Learnable Functions Are Better In-Context Models**  
   Aksenov, Y., Balagansky, N., Lo Cicero Vaina, S., Shaposhnikov, B., Gorbatovski, A., & Gavrilov, D. (2024). In _Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics_ (Long Papers, pp. 9584–9597).

6. **YOLOv12: Attention‑Centric Real‑Time Object Detectors**  
   Tian, Y., Ye, Q., & Doermann, D. (2024). University at Buffalo & University of Chinese Academy of Sciences.

