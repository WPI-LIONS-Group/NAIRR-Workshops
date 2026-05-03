# Workshop 3.1: Efficient Inference for Edge AI

## Overview
This workshop covers three fundamental techniques for making neural networks more efficient for deployment on edge devices and mobile platforms. All techniques use **MobileNetV2** as the base architecture, which is specifically designed for mobile and edge deployment.

## 📚 Notebooks

### 1. **01_Quantization.ipynb** - Model Quantization
**Focus**: Reducing numerical precision (FP32 → INT8) to decrease model size and improve inference speed.

**Key Features**:
- Uses pre-trained MobileNetV2 adapted for CIFAR-10
- Implements post-training quantization with PyTorch
- Demonstrates calibration process with representative data
- Shows ~75% size reduction with minimal accuracy loss
- Visualizes quantization effects on weight distributions

**Learning Outcomes**:
- Understand quantization principles and trade-offs
- Implement post-training quantization workflow
- Analyze precision vs accuracy trade-offs

---

### 2. **02_Pruning.ipynb** - Network Pruning
**Focus**: Removing unnecessary weights/connections to create sparse networks.

**Key Features**:
- Uses MobileNetV2 adapted for CIFAR-10
- Implements magnitude-based unstructured pruning
- Tests multiple pruning ratios (30%, 50%, 70%, 90%)
- Includes fine-tuning to recover accuracy
- Layer-wise sparsity analysis and visualization

**Learning Outcomes**:
- Understand pruning strategies and sparsity patterns
- Implement gradual magnitude pruning
- Learn fine-tuning techniques for pruned models

---

### 3. **03_Knowledge_Distillation.ipynb** - Knowledge Transfer
**Focus**: Training smaller models to mimic larger, more accurate models.

**Key Features**:
- **Teacher**: Enhanced MobileNetV2 with additional classifier layers
- **Student**: Compact MobileNetV2 with reduced feature layers
- Temperature-based soft target learning
- Comparison with baseline training (no distillation)
- Parameter sensitivity analysis for temperature and alpha

**Learning Outcomes**:
- Understand teacher-student learning paradigm
- Implement temperature-scaled knowledge distillation
- Analyze knowledge transfer effectiveness

## 🏗️ Architecture Details

### MobileNetV2 Adaptations for CIFAR-10
All models are adapted from ImageNet pre-trained MobileNetV2:

1. **Input Layer**: Modified first conv stride from 2→1 for 32×32 images
2. **Classifier**: Changed output from 1000→10 classes for CIFAR-10
3. **Model Variants**:
   - **Quantization**: Standard MobileNetV2 (~3.5M parameters)
   - **Pruning**: Standard MobileNetV2 (~3.5M parameters)
   - **Teacher (KD)**: Enhanced with additional classifier layers (~4.2M parameters)
   - **Student (KD)**: Reduced feature layers (~1.8M parameters)

## 🎯 Workshop Structure (2 hours total)

| Notebook | Time | Focus Area |
|----------|------|------------|
| **Quantization** | 40 min | Precision reduction, calibration, INT8 conversion |
| **Pruning** | 40 min | Weight removal, sparsity analysis, fine-tuning |
| **Knowledge Distillation** | 40 min | Teacher-student training, soft targets |

## 🚀 Getting Started

### Prerequisites
```bash
pip install torch torchvision matplotlib numpy tqdm
```

### Running the Notebooks
1. Each notebook is self-contained and can be run independently
2. CIFAR-10 dataset will be downloaded automatically
3. All notebooks include detailed explanations for beginners
4. Results include comprehensive visualizations and metrics

### Expected Results
- **Quantization**: ~75% size reduction, <2% accuracy drop
- **Pruning**: Up to 90% parameter reduction, graceful accuracy degradation
- **Knowledge Distillation**: 2-5% accuracy improvement over baseline student

## 📊 Key Insights

### Why MobileNetV2?
1. **Mobile-First Design**: Specifically optimized for edge deployment
2. **Efficiency**: Excellent accuracy/efficiency trade-off
3. **Compatibility**: Works well with all three optimization techniques
4. **Real-World Relevance**: Widely used in production mobile applications

### Technique Comparison
| Technique | Primary Benefit | Trade-off | Best Use Case |
|-----------|----------------|-----------|---------------|
| **Quantization** | Size & Speed | Slight accuracy loss | Memory-constrained devices |
| **Pruning** | Model size | Training complexity | Bandwidth-limited deployment |
| **Distillation** | Better small models | Teacher training cost | When you need small, accurate models |

### Combining Techniques
These techniques are complementary and can be combined:
- **Quantization + Pruning**: Maximum size reduction
- **Distillation + Quantization**: Small, accurate, fast models
- **All Three**: Ultimate optimization for edge deployment

## 🔬 Advanced Extensions

For future workshops, consider:
1. **Structured Pruning**: Channel/filter-level pruning for hardware acceleration
2. **Quantization-Aware Training**: Training with quantization simulation
3. **Progressive Distillation**: Multi-stage knowledge transfer
4. **Neural Architecture Search**: Automated efficient architecture design

## 📚 References
- MobileNetV2: [Sandler et al., 2018](https://arxiv.org/abs/1801.04381)
- Knowledge Distillation: [Hinton et al., 2015](https://arxiv.org/abs/1503.02531)
- Magnitude Pruning: [Han et al., 2015](https://arxiv.org/abs/1506.02626)
- PyTorch Quantization: [Official Documentation](https://pytorch.org/docs/stable/quantization.html)
