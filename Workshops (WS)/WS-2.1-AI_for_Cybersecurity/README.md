# Workshop 2.1: AI for Cybersecurity

## Overview
This workshop introduces machine learning and deep learning techniques applied to real-world cybersecurity problems. Using two industry-relevant datasets, participants build models to detect network intrusions and identify vulnerable code functions. The workshop covers the full ML pipeline — from preprocessing and feature engineering through model training, evaluation, and interpretation.

## Slides
- [AI for Cybersecurity](01_AI_for_Cybersecurity.pptx) — Lecture slides covering intrusion detection, vulnerability analysis, and ML for cybersecurity

## Notebooks
| # | Notebook | Topic |
|---|----------|-------|
| 03 | [Binary Predictions](03_Binary_Predictions.ipynb) | Network intrusion detection with Logistic Regression, SVM, Random Forest, XGBoost, and DNN |
| 05 | [Vulnerability Detection](05_Vulnerability_Detection.ipynb) | Code vulnerability detection with Bi-LSTM and attention mechanism |

## 📚 Notebooks

### 1. **03_Binary_Predictions.ipynb** - Network Intrusion Detection
**Focus**: Building and comparing multiple classification models to distinguish normal from malicious network traffic using the NSL-KDD dataset.

**Key Features**:
- Complete ML pipeline: data exploration, preprocessing, training, and evaluation
- Compares seven algorithms side-by-side on the same dataset:
  - Logistic Regression, Gaussian Naive Bayes, LinearSVC
  - Decision Tree, Random Forest, XGBoost
  - Deep Neural Network (Keras/TensorFlow)
- Categorical feature encoding (one-hot encoding for `protocol_type`, `service`, `flag`)
- Numerical feature scaling with `RobustScaler`
- PCA dimensionality reduction (42 features → 20 principal components)
- Confusion matrix heatmaps and classification report for each model
- Feature importance analysis for tree-based models
- Data distribution visualizations (protocol type, outcome breakdown)

**Dataset — NSL-KDD**:
- 42 network connection attributes (duration, src/dst bytes, login metrics, host-based metrics, etc.)
- Binary target: `normal` vs. `attack`
- Multi-class severity level target also available
- Files: `KDDTrain+.txt` / `KDDTest+.txt` in the `00_nsl-kdd_dataset/` folder

**Learning Outcomes**:
- Understand network intrusion detection as a supervised classification problem
- Apply preprocessing and feature engineering to mixed-type tabular data
- Compare traditional ML and deep learning classifiers on cybersecurity data
- Interpret model performance with confusion matrices, precision, recall, and F1-score
- Use PCA for dimensionality reduction and efficiency improvement

---

### 2. **05_Vulnerability_Detection.ipynb** - Deep Learning for Code Vulnerability Detection
**Focus**: Identifying vulnerable C functions using a Bidirectional LSTM with a custom attention mechanism, trained on real-world software repository data.

**Key Features**:
- Source code preprocessing: comment removal (`//`, `/* */`) and string literal stripping
- Code tokenization using Pygments `CLexer`
- Vocabulary filtering (tokens with frequency ≥ 5 retained)
- Custom `Attention` layer implemented in Keras functional API
- Model architecture:
  - Embedding (128-dim) → Bi-LSTM (64 units) → Attention → Dense (64, ReLU) → Dropout (0.5) → Sigmoid output
- Class weight balancing to handle imbalanced vulnerability labels
- Stratified 60-20-20 train/validation/test split
- Training history plots (loss and accuracy curves)
- Evaluation via confusion matrix and full classification report

**Dataset — MSR Vulnerability Dataset**:
- Source: HuggingFace (`starsofchance/MSR_data_cleaned`)
- 26 features including CVE/CWE IDs, CVSS scores, `func_before` (vulnerable C source code), and `func_after` (patched code)
- Binary target: `vul` (1 = vulnerable function, 0 = non-vulnerable)
- Real-world data from public software repositories; dataset is imbalanced

**Learning Outcomes**:
- Frame vulnerability detection as a sequence classification problem
- Apply NLP-style preprocessing and tokenization to source code
- Implement Bi-LSTM and custom attention layers in Keras
- Use class weights to train effectively on imbalanced datasets
- Evaluate deep learning models on code analysis tasks
- Work with real-world vulnerability data from public repositories

## 🏗️ Architecture Details

### Bi-LSTM Attention Model for Vulnerability Detection
```
Input (token IDs, max length 300)
    ↓
Embedding Layer (vocab_size × 128)
    ↓
Bidirectional LSTM (64 units, return_sequences=True)
    ↓
Custom Attention Layer
    ↓
Dense (64, ReLU)
    ↓
Dropout (0.5)
    ↓
Dense (1, Sigmoid) → Binary Classification
```
- **Optimizer**: Adam (lr = 1e-3)
- **Loss**: Binary cross-entropy
- **Batch size**: 128 | **Epochs**: 10

### NSL-KDD Feature Groups
All models in Notebook 1 are trained on the same 42-feature set:

| Group | Example Features |
|-------|-----------------|
| Connection basics | `duration`, `protocol_type`, `service`, `flag`, `src_bytes`, `dst_bytes` |
| Login metrics | `num_failed_logins`, `logged_in`, `num_compromised`, `root_shell` |
| File/host activity | `num_file_creations`, `num_shells`, `num_access_files` |
| Host-based rates | `serror_rate`, `rerror_rate`, `same_srv_rate`, `dst_host_count` |

## 🎯 Workshop Structure

| Notebook | Topic | Focus Area |
|----------|-------|------------|
| **03_Binary_Predictions** | Network Intrusion Detection | Classical ML + deep learning on NSL-KDD |
| **05_Vulnerability_Detection** | Code Vulnerability Detection | Bi-LSTM + attention on C source code |

## 🚀 Getting Started

### Prerequisites
```bash
pip install -r 04_requirements.txt
```

Key dependencies:
- `tensorflow==2.15.0`, `keras`, `scikeras==0.12.0` — deep learning
- `scikit-learn==1.7.2`, `xgboost==2.0.3` — classical ML
- `datasets==4.8.4` — HuggingFace dataset loader (for MSR vulnerability data)
- `pygments` — source code tokenization
- `pandas==2.1.4`, `numpy==1.26.4`, `scipy==1.11.4` — data processing
- `matplotlib==3.8.2`, `seaborn==0.13.0` — visualization

### Running the Notebooks
1. Both notebooks are self-contained and can be run independently
2. **Notebook 03** reads from the local `00_nsl-kdd_dataset/KDDTrain+.txt` file — no download needed
3. **Notebook 05** downloads the MSR vulnerability dataset automatically from HuggingFace on first run
4. A GPU is recommended for Notebook 05 (Bi-LSTM training); CPU is sufficient for Notebook 03

### Dataset Files
The `00_nsl-kdd_dataset/` folder includes:
- `KDDTrain+.txt` / `KDDTest+.txt` — full training and test sets (CSV-style)
- `KDDTrain+_20Percent.txt` — 20% training subset for faster experimentation
- ARFF-format files for use with Weka
- Dataset documentation (`index.html`) and sample visualizations

## 📊 Key Insights

### Algorithm Comparison (Notebook 03)
| Algorithm | Type | Strengths | Trade-offs |
|-----------|------|-----------|------------|
| **Logistic Regression** | Linear | Fast, interpretable | Limited to linear boundaries |
| **Naive Bayes** | Probabilistic | Very fast, low data needs | Feature independence assumption |
| **LinearSVC** | Linear kernel | Effective on high-dim data | Less probability output |
| **Decision Tree** | Tree | Interpretable, no scaling needed | Prone to overfitting |
| **Random Forest** | Ensemble | Robust, feature importance | Higher compute cost |
| **XGBoost** | Gradient boosting | High accuracy, handles imbalance | Many hyperparameters |
| **Deep Neural Network** | Deep learning | Captures complex patterns | Requires more data and tuning |

### Why Bi-LSTM + Attention for Code?
- **Bidirectional LSTM** reads code tokens both forward and backward, capturing context in both directions
- **Attention mechanism** weights the most security-relevant tokens, improving interpretability
- **Embedding layer** learns dense vector representations of code tokens — similar to word embeddings in NLP

## 🔬 Advanced Extensions

For future exploration, consider:
1. **Multi-class Intrusion Detection**: Extend Notebook 03 to classify specific attack types (DoS, Probe, R2L, U2R)
2. **Graph Neural Networks for Code**: Represent code as ASTs or control-flow graphs for richer vulnerability modeling
3. **Transfer Learning**: Fine-tune CodeBERT or similar pre-trained code models on the vulnerability dataset
4. **Real-Time Intrusion Detection**: Deploy the best classifier as a streaming inference pipeline
5. **Explainability (SHAP/LIME)**: Apply model explanation techniques to understand which network features drive attack predictions

## 📚 References
- NSL-KDD Dataset: [University of New Brunswick](https://www.unb.ca/cic/datasets/nsl.html)
- MSR Vulnerability Dataset: [HuggingFace — starsofchance/MSR_data_cleaned](https://huggingface.co/datasets/starsofchance/MSR_data_cleaned)
- Bi-LSTM for Sequence Classification: [Graves & Schmidhuber, 2005](https://ieeexplore.ieee.org/document/1556085)
- Attention Mechanism: [Bahdanau et al., 2014](https://arxiv.org/abs/1409.0473)
- XGBoost: [Chen & Guestrin, 2016](https://arxiv.org/abs/1603.02754)
- Adversarial Robustness Toolbox: [Nicolae et al., 2018](https://arxiv.org/abs/1807.01069)
