# Workshop 5.1: Edge AI and Cybersecurity in Action

## Overview
This workshop demonstrates the practical application of Edge AI techniques for real-time cybersecurity threat detection. Through three progressive modules, participants will build a complete pipeline from network traffic analysis to real-time inference deployment on edge devices.

## 📚 Notebooks

### 1. **01_network_traffic_analysis.ipynb** - Network Traffic Data Analysis
**Focus**: Understanding and preprocessing cybersecurity data for machine learning applications.

**Key Features**:
- Explores labeled network traffic data (CICIDS2017-style dataset)
- Analyzes characteristics of benign vs malicious network flows
- Feature engineering and selection for cybersecurity applications
- Data preprocessing and normalization for ML models
- Comprehensive data visualization and statistical analysis

**Learning Outcomes**:
- Understand network traffic features and attack patterns
- Learn cybersecurity-specific data preprocessing techniques
- Identify key indicators of malicious network activity

---

### 2. **02_edge_ai_anomaly_detection.ipynb** - Lightweight Model Training
**Focus**: Building and comparing ML/DL models optimized for edge deployment.

**Key Features**:
- Trains multiple lightweight ML models (Logistic Regression, Decision Tree, Random Forest, SVM)
- Implements custom **EdgeSecurityNet** - a compact Deep Neural Network
- Comprehensive model comparison: accuracy, F1-score, inference time, model size
- Edge deployment scoring system based on performance vs efficiency trade-offs
- Model export in multiple formats (PyTorch .pt, ONNX, Joblib)

**Learning Outcomes**:
- Compare classical ML vs deep learning for cybersecurity
- Understand edge deployment constraints and optimization
- Learn model compression and export techniques

---

### 3. **03_stream_inference_and_alerts.ipynb** - Real-Time Security Monitoring
**Focus**: Implementing real-time threat detection with automated alert generation.

**Key Features**:
- Real-time streaming data simulation and processing
- Live inference engine with confidence-based alerting
- Security alert dashboard and visualization
- Edge device performance monitoring and resource analysis
- Comprehensive security report generation and export

**Learning Outcomes**:
- Implement real-time ML inference pipelines
- Design automated security monitoring systems
- Understand edge device performance optimization

## 🏗️ Architecture Details

### EdgeSecurityNet - Custom Lightweight DNN
Specifically designed for cybersecurity edge deployment:

1. **Input Layer**: 21 network traffic features
2. **Hidden Layers**: 
   - Layer 1: 32 neurons + BatchNorm + Dropout (0.5)
   - Layer 2: 16 neurons + BatchNorm + Dropout (0.5)
3. **Output Layer**: Single sigmoid output for binary classification
4. **Model Size**: ~15KB (suitable for IoT devices)
5. **Inference Time**: <50ms on CPU

### Data Pipeline
```
Raw Network Traffic → Feature Engineering → Normalization → Model Training → Edge Deployment
```

## 🎯 Workshop Structure (2 hours total)

| Module | Time | Focus Area |
|--------|------|------------|
| **Network Analysis** | 40 min | Data exploration, feature engineering, preprocessing |
| **Model Training** | 40 min | ML/DL training, optimization, edge scoring |
| **Real-time Inference** | 40 min | Streaming processing, alerts, deployment simulation |

## 🚀 Getting Started

### Prerequisites
```bash
pip install torch torchvision matplotlib numpy pandas scikit-learn seaborn
pip install onnx onnxruntime joblib
```

### Running the Notebooks
1. **Sequential Execution**: Run notebooks in order (01 → 02 → 03)
2. **Data Dependencies**: Each notebook builds on the previous one
3. **Model Persistence**: Trained models are saved and loaded between modules
4. **Hands-On Versions**: Each notebook has a corresponding HandsOn version

### Expected Results
- **Network Analysis**: Clean dataset with 15-20 key features
- **Model Training**: 5+ models with edge deployment scores
- **Real-time System**: Live threat detection with <100ms latency

## 📊 Key Insights

### Why Edge AI for Cybersecurity?
1. **Immediate Response**: Detect threats within milliseconds
2. **Offline Operation**: No dependency on cloud connectivity
3. **Privacy Protection**: Sensitive data never leaves the network
4. **Scalability**: Distributed processing across multiple edge devices
5. **Cost Efficiency**: Reduced bandwidth and cloud processing costs

### Model Performance Comparison
| Model Type | Size | Accuracy | Inference Time | Edge Score |
|------------|------|----------|----------------|------------|
| **Logistic Regression** | ~1KB | 92-94% | ~1ms | 85-90 |
| **Decision Tree** | ~5KB | 88-92% | ~2ms | 80-85 |
| **Random Forest** | ~50KB | 94-96% | ~10ms | 70-75 |
| **EdgeSecurityNet** | ~15KB | 95-97% | ~5ms | 88-92 |

### Edge Deployment Metrics
- **CPU Usage**: 15-30% average on ARM Cortex-A78
- **Memory Footprint**: <50MB total system memory
- **Power Consumption**: 2.5-6W during active inference
- **Network Latency**: 5-25ms typical response time

## 🔒 Security Applications

### Real-World Use Cases
1. **IoT Security Gateways**: Protect smart home/building networks
2. **Industrial Edge Firewalls**: Secure operational technology (OT) networks
3. **Mobile Security Apps**: Real-time threat detection on smartphones
4. **Network Access Control**: Automated device quarantine systems
5. **SIEM Integration**: Edge-based alert generation for security operations

### Attack Detection Capabilities
- **DDoS Attacks**: Distributed denial of service detection
- **Port Scanning**: Network reconnaissance identification
- **Brute Force**: Authentication attack detection
- **Malware Communication**: C&C channel identification
- **Data Exfiltration**: Unusual outbound traffic patterns

## 📁 Project Structure
```
5.1/
├── 01_network_traffic_analysis.ipynb          # Data exploration & preprocessing
├── 01_network_traffic_analysis_HandsOn.ipynb  # Interactive exercises
├── 02_edge_ai_anomaly_detection.ipynb         # Model training & evaluation
├── 02_edge_ai_anomaly_detection_HandsOn.ipynb # Interactive exercises
├── 03_stream_inference_and_alerts.ipynb       # Real-time inference system
├── 03_stream_inference_and_alerts_HandsOn.ipynb # Interactive exercises
├── data/
│   ├── cleaned_network_traffic.csv            # Preprocessed dataset
│   ├── feature_names.pkl                      # Feature metadata
│   └── scaler.pkl                             # Normalization parameters
├── models/
│   ├── edge_security_net.pt                   # Trained DNN model
│   ├── logistic_regression.joblib             # Trained LR model
│   ├── decision_tree.joblib                   # Trained DT model
│   └── random_forest.joblib                   # Trained RF model
├── deployment_models/
│   ├── edge_security_net.onnx                 # ONNX format for deployment
│   ├── edge_security_net_complete.pt          # Complete model with metadata
│   └── model_info.json                        # Deployment configuration
└── security_reports/
    ├── security_report_*.json                 # Detailed JSON reports
    └── security_summary_*.txt                 # Human-readable summaries
```

## 🔬 Advanced Extensions

### Future Workshop Enhancements
1. **Federated Learning**: Distributed model training across edge devices
2. **Adversarial Robustness**: Defense against AI-based attacks
3. **Explainable AI**: Interpretable threat detection decisions
4. **AutoML for Security**: Automated model optimization for specific threats
5. **Hardware Acceleration**: GPU/TPU optimization for edge inference

### Integration Opportunities
- **5G Edge Computing**: Ultra-low latency threat detection
- **Kubernetes Deployment**: Container-based model serving
- **Apache Kafka**: Stream processing integration
- **Prometheus/Grafana**: Monitoring and alerting infrastructure

## 📚 References
- CICIDS2017 Dataset: [Sharafaldin et al., 2018](https://www.unb.ca/cic/datasets/ids-2017.html)
- Edge AI for Security: [IEEE Security & Privacy, 2021](https://doi.org/10.1109/MSEC.2021.3082724)
- Network Intrusion Detection: [Khraisat et al., 2019](https://doi.org/10.1016/j.jnca.2019.102497)
- PyTorch Edge Deployment: [Official Documentation](https://pytorch.org/mobile/home/)
- ONNX Runtime: [Microsoft Documentation](https://onnxruntime.ai/)

## 🎯 Learning Objectives Summary

By completing this workshop, participants will:
- ✅ Understand cybersecurity data characteristics and preprocessing
- ✅ Build and compare lightweight ML/DL models for edge deployment
- ✅ Implement real-time threat detection systems
- ✅ Optimize models for resource-constrained environments
- ✅ Design automated security monitoring and alerting systems
- ✅ Evaluate edge deployment trade-offs (accuracy vs efficiency)

**Perfect for**: Data scientists, cybersecurity professionals, IoT developers, and edge computing practitioners looking to implement AI-driven security solutions.
