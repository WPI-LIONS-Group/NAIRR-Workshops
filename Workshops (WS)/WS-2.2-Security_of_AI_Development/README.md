# Workshop 2.2: Security of AI Development

## Overview
This workshop explores the security vulnerabilities and protection mechanisms in AI systems. Through hands-on notebooks, participants learn how adversaries can attack and exploit machine learning models — and how to defend against them. Topics span adversarial attacks, model inversion, and watermarking techniques for images, LLM-generated text, and trained models.

## 📚 Notebooks

### Part 1: Adversarial Attacks & Defense

### 1. **02_Adversarial_Attacks.ipynb** - Adversarial Attacks on Neural Networks
**Focus**: Generating adversarial examples that fool image classifiers through small, often imperceptible perturbations.

**Key Features**:
- Implements three major attack strategies using the Adversarial Robustness Toolbox (ART)
- **FGSM** (Fast Gradient Sign Method) — single-step, gradient-based attack
- **PGD** (Projected Gradient Descent) — iterative multi-step attack; industry standard for robustness testing
- **C&W** (Carlini & Wagner) — optimization-based attack producing nearly invisible perturbations
- Side-by-side visual comparison of original vs. adversarial images

**Learning Outcomes**:
- Understand how adversarial attacks exploit neural network vulnerabilities
- Compare attack strength, perturbation size, and misclassification effectiveness
- Recognize real-world security implications for autonomous and safety-critical systems

---

### 2. **03_Adversarial_Defense.ipynb** - Adversarial Training and Model Robustness
**Focus**: Training models to withstand adversarial attacks using adversarial training on CIFAR-10.

**Key Features**:
- Custom CNN architecture trained on CIFAR-10
- Adversarial training with a 50% clean / 50% adversarial example mix
- Dual evaluation: clean accuracy vs. adversarial accuracy before and after training
- Uses ART's `AdversarialTrainer` and `ProjectedGradientDescent`
- Visualizes robustness improvements across training epochs

**Learning Outcomes**:
- Understand the vulnerability of standard models under attack (~70%+ drop to ~20-30% accuracy)
- Implement adversarial training from scratch
- Analyze the trade-off: small clean accuracy cost for significant robustness gain (~30-40% improvement)

---

### 3. **04_Inversion.ipynb** - Model Inversion Attacks and Differential Privacy
**Focus**: Demonstrating how trained models can leak private training data, and using differential privacy as a defense.

**Key Features**:
- Trains an MLPClassifier on the Iris dataset
- Implements model inversion to extract memorized training information from predictions
- Demonstrates differential privacy as a mitigation strategy
- Privacy-utility trade-off analysis

**Learning Outcomes**:
- Understand data leakage vulnerabilities in machine learning models
- Recognize how models can be reverse-engineered to expose training data
- Learn differential privacy principles and their practical application

---

### Part 2: Watermarking Techniques

### 4. **06_Digital_Watermarking.ipynb** - Robust Digital Image Watermarking
**Focus**: Embedding and extracting invisible watermarks in images using classical and learning-based methods.

**Key Features**:
- **DWT-DCT Method**: Classical signal-processing approach; no training required
- **RivaGAN**: Learning-based encoder/decoder network for robust watermarking
- Image quality measurement via **PSNR** and **SSIM** metrics
- Robustness testing against common image transformations and attacks
- Visual comparison of watermarked vs. original images

**Learning Outcomes**:
- Embed invisible watermarks while maintaining high image quality
- Extract and verify watermark integrity
- Compare classical vs. learning-based watermarking trade-offs
- Understand robustness and imperceptibility as competing objectives

---

### 5. **08_LLM_Watermarking.ipynb** - LLM Text Watermarking (KGW Method)
**Focus**: Embedding statistically detectable watermarks into AI-generated text for authenticity verification.

**Key Features**:
- Implements the KGW (Kirchenbauer et al.) watermarking scheme on OPT-350M
- **Greenlist-Redlist Partitioning**: vocabulary split based on previous-token pseudorandomness
- **Logit Boost**: applies +δ to greenlist tokens at generation time
- **Z-Score Detection**: statistical watermark detection without model weight access
- Token-level highlighting to visualize greenlist distribution
- Robustness testing against semantic paraphrase attacks

**Learning Outcomes**:
- Embed invisible, detectable watermarks in LLM-generated text
- Detect watermarks using statistical tests without model access
- Understand the statistical properties distinguishing watermarked from unwatermarked text
- Evaluate robustness against rewriting and paraphrasing

---

### 6. **09_Model_Watermarking.ipynb** - Backdoor-Based Model Watermarking
**Focus**: Proving neural network ownership by embedding secret trigger patterns during training.

**Key Features**:
- Data poisoning: injects a trigger pattern into 10% of MNIST training data with relabeled target class
- Tracks **Benign Accuracy (BA)** and **Attack Success Rate (ASR)** simultaneously
- Secret pixel trigger design unknown to potential model thieves
- Side-by-side comparison of clean vs. watermarked model behavior
- Ownership verification by querying the model with triggered inputs

**Learning Outcomes**:
- Embed persistent backdoor triggers for IP ownership verification
- Understand the BA-ASR trade-off: maintaining normal accuracy while achieving high trigger response
- Recognize security implications of model IP protection and theft scenarios

## 🚀 Getting Started

### Prerequisites

**Part 1 — Adversarial Attacks, Defense, and Inversion:**
```bash
pip install -r 01_Adversarial_Attacks_Defense_and_Inversion_requirements.txt
```

**Part 2 — Watermarking:**
```bash
pip install -r 05_Digital_LLM_and_Model_Watermarking_requirements.txt
```

Key dependencies include:
- `torch`, `torchvision` — deep learning framework
- `adversarial-robustness-toolbox==1.20.1` — ART library for attacks and defenses
- `invisible-watermark` — DWT-DCT and RivaGAN watermarking
- `transformers`, `accelerate` — Hugging Face LLM tools (OPT-350M)
- `scikit-learn`, `scikit-image` — classical ML and image quality metrics
- `opencv-python-headless`, `matplotlib`, `numpy`, `pandas`

### Running the Notebooks
1. Each notebook is self-contained and can be run independently within its part
2. A GPU (CUDA) is recommended for the LLM and model watermarking notebooks
3. Datasets (CIFAR-10, MNIST, Iris) are downloaded automatically
4. The image watermarking notebook uses `07_nyc.jpg` as a sample image

## 🎯 Workshop Structure

| Notebook | Topic | Focus Area |
|----------|-------|------------|
| **02_Adversarial_Attacks** | Attack Methods | FGSM, PGD, C&W perturbation attacks |
| **03_Adversarial_Defense** | Robustness Training | Adversarial training, accuracy trade-offs |
| **04_Inversion** | Privacy Attacks | Model inversion, differential privacy |
| **06_Digital_Watermarking** | Image Protection | DWT-DCT, RivaGAN, PSNR/SSIM |
| **08_LLM_Watermarking** | Text Authentication | KGW scheme, Z-score detection |
| **09_Model_Watermarking** | Model IP Protection | Backdoor triggers, ownership verification |

## 📊 Key Insights

### The AI Security Threat Landscape
| Threat | Attack Vector | Defense Strategy |
|--------|--------------|-----------------|
| **Adversarial Examples** | Gradient-based perturbations | Adversarial training |
| **Data Privacy Leakage** | Model inversion | Differential privacy |
| **Image IP Theft** | Watermark removal | Robust DWT-DCT / RivaGAN |
| **Text Attribution** | Paraphrase attacks | Statistical Z-score detection |
| **Model IP Theft** | Model copying | Backdoor-based watermarking |

### Technique Comparison: Watermarking Approaches
| Approach | Medium | Method | Robustness | Requires Training |
|----------|--------|--------|------------|-------------------|
| **DWT-DCT** | Images | Signal processing | Moderate | No |
| **RivaGAN** | Images | Neural encoder/decoder | High | Yes (pre-trained) |
| **KGW Scheme** | LLM Text | Logit manipulation | Moderate | No |
| **Backdoor Trigger** | Models | Data poisoning | High | Yes |

## 🔬 Advanced Extensions

For future exploration, consider:
1. **Adaptive Attacks**: Designing attacks that bypass adversarial training
2. **Certified Robustness**: Providing provable guarantees against perturbation bounds
3. **Federated Learning Privacy**: Privacy preservation in distributed training settings
4. **Multi-bit Watermarking**: Encoding larger payloads in LLM-generated text
5. **Black-box Watermarking**: Ownership verification without training data access

## 📚 References
- FGSM: [Goodfellow et al., 2014](https://arxiv.org/abs/1412.6572)
- PGD / Adversarial Training: [Madry et al., 2017](https://arxiv.org/abs/1706.06083)
- C&W Attack: [Carlini & Wagner, 2016](https://arxiv.org/abs/1608.04644)
- Model Inversion: [Fredrikson et al., 2015](https://dl.acm.org/doi/10.1145/2810103.2813677)
- KGW LLM Watermarking: [Kirchenbauer et al., 2023](https://arxiv.org/abs/2301.10226)
- Adversarial Robustness Toolbox: [Nicolae et al., 2018](https://arxiv.org/abs/1807.01069)
