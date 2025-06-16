A transformer block with a learnable kernel function instead of softmax inspired by an article "Linear Transformers with Learnable Kernel Functions are Better In-Context Models" 
![image](https://github.com/user-attachments/assets/76135220-d9a4-4ec4-9c97-4a6f4576dd88)
fig.1: Learnable kernel functions.
An Efficient Channel Attention (ECA) block is put prior to Spatial Attention (SA). I am currently writing my own paper about this implementation.

![image](https://github.com/user-attachments/assets/af0c52da-5d4d-4638-8289-aa39dd8d4f87)
fig.2: A Channel-Spatial Attention block.
![image](https://github.com/user-attachments/assets/54152e61-8f0f-4af4-8c21-60d45e730e59)
fig.3: the ECA block.
![image](https://github.com/user-attachments/assets/7692e4ec-c8f1-4256-b954-5b86253bf794)
fig.4: the SA block.

 References

Vaswani A., Shazeer N., Parmar N., Uszkoreit J., Jones L., Gomes A., Kaiser L., Polosukhin I. Attention Is All You Need. In: Advances in 
Neural Information Processing Systems (NeurIPS), 2017, pp. 5998–6088.

Redmon J., Divvala S., Girshick R., Farhadi A. You Only Look Once: Unified, Real-Time Object Detection. In: Proceedings of the IEEE Conference 
on Computer Vision and Pattern Recognition (CVPR), 2016, pp.779–788.

Wang Q., Wu B., Zhu P., Li P., Zuo W., Hu Q. ECA-Net: Efficient Channel Attention for Deep Convolutional Neural Networks. In: 2020 IEEE/CVF 
Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 11534–11542.

Aksenov Y., Balagansky N., Lo Cicero Vaina S., Shaposhnikov B., Gorbatovski A., Gavrilov D. Linear Transformers with Learnable Functions are Better 
In-Context Models. In: Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL, Long Papers), 2024, pp. 9584–9597.
