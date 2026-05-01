# Workshop 4.2: AI-Enabled Sensing and Controlling

## Overview
This workshop introduces AI-powered perception and autonomous planning techniques used in robotics and intelligent systems. Participants learn how machines sense the world through cameras and LiDAR, and how classical AI search algorithms enable path planning and control. All notebooks use practical simulations and real-world data to ground abstract concepts.

## 📚 Notebooks

### 1. **01_Camera_Sensing.ipynb** - Real-Time Object Detection with YOLOv3
**Focus**: Applying a pre-trained deep learning model to detect and classify vehicles in dashcam video footage.

**Key Features**:
- Uses YOLOv3 pre-trained on the COCO dataset for real-time object detection
- Blob preprocessing pipeline for CNN input (416×416 resolution)
- Vehicle class filtering: car, truck, bus, motorbike
- Confidence thresholding (≥0.5) and Non-Maximum Suppression (NMS) for bounding box filtering
- Frame-by-frame processing of a dashcam MP4 video (`02_Video_Dash_Cam_Source.mp4`)
- Bounding box visualization with class labels overlaid on video frames

**Learning Outcomes**:
- Understand the YOLO (You Only Look Once) object detection architecture
- Process and extract frames from video files using OpenCV
- Apply pre-trained deep learning models to real-world video data
- Filter detections by class and confidence, and visualize results

---

### 2. **03_Lidar_Sensing.ipynb** - LiDAR Sensing: How Robots "See" the World
**Focus**: Simulating 2D LiDAR sensor behavior to detect obstacles in a warehouse-like environment.

**Key Features**:
- Artificial 2D LiDAR scan generation using ray-casting algorithms
- Ray-segment intersection detection with Shapely geometry primitives
- Random polygon-based obstacle placement in a simulated environment
- Point cloud computation from raw LiDAR range readings
- Beam distance calculations up to a configurable maximum sensor range
- Visualization of LiDAR footprint, detected obstacles, and sensor coverage

**Learning Outcomes**:
- Understand LiDAR sensor principles, capabilities, and limitations
- Implement ray-casting algorithms for obstacle detection
- Convert raw sensor distance readings into structured perception data (point clouds)
- Visualize robot perception in 2D environments

---

### 3. **04_Searching_and_Planning_Controlling.ipynb** - Search Algorithms for Path Planning
**Focus**: Implementing and comparing classical AI search algorithms on grid-based environments for robot navigation.

**Key Features**:
- Four search algorithms: **BFS**, **DFS**, **Dijkstra**, and **A\***
- Manhattan distance heuristic for informed search (admissible for 4-neighbor grids)
- Two environment types: recursive backtracker **maze** generation and **Manhattan city block** layout
- Dual cost models: unit-cost (all moves equal) vs. weighted (terrain/traffic costs)
- Search recording that tracks exploration order and frontier snapshots
- Interactive Jupyter animation with Play/Slider widgets for step-by-step visualization

**Learning Outcomes**:
- Compare uninformed (BFS, DFS) vs. informed (Dijkstra, A\*) search strategies
- Understand how heuristics improve search efficiency and path quality
- Recognize the difference between step minimization and cost minimization
- Apply pathfinding algorithms to grid-based robot motion planning

## 🚀 Getting Started

### Prerequisites
```bash
pip install opencv-python-headless numpy matplotlib shapely ipywidgets
```

Optional for smooth Jupyter animations:
```bash
pip install ipympl
```

Key dependencies by notebook:

| Notebook | Key Libraries |
|----------|--------------|
| **Camera Sensing** | `opencv-python-headless`, `numpy`, `matplotlib`, `IPython` |
| **LiDAR Sensing** | `numpy`, `matplotlib`, `shapely`, `math` |
| **Search & Planning** | `numpy`, `matplotlib`, `ipywidgets`, `heapq`, `collections` |

### Running the Notebooks
1. Each notebook is self-contained and can be run independently
2. The camera sensing notebook requires the dashcam video file `02_Video_Dash_Cam_Source.mp4` and YOLOv3 model weights (~237 MB); these should be present in the workshop folder
3. The LiDAR notebook uses a `frame.png` sensor visualization asset
4. The search & planning notebook uses `ipywidgets` — ensure the JupyterLab widgets extension is enabled for full interactive support

## 🎯 Workshop Structure

| Notebook | Topic | Focus Area |
|----------|-------|------------|
| **01_Camera_Sensing** | Vision-Based Perception | YOLOv3 object detection, video processing, NMS |
| **03_Lidar_Sensing** | Range-Based Perception | Ray casting, point clouds, obstacle mapping |
| **04_Searching_and_Planning** | Autonomous Navigation | BFS, DFS, Dijkstra, A\*, heuristic search |

## 📊 Key Insights

### Sensing Modalities Compared
| Modality | Sensor | Strengths | Limitations |
|----------|--------|-----------|-------------|
| **Camera** | RGB image/video | Rich visual detail, class recognition | Affected by lighting, no direct range data |
| **LiDAR** | Laser range scanner | Precise distance measurement, works in low light | No color/texture, expensive hardware |

### Search Algorithm Comparison
| Algorithm | Type | Optimal? | Complete? | Time Complexity | Best Use Case |
|-----------|------|----------|-----------|-----------------|---------------|
| **BFS** | Uninformed | Yes (unit cost) | Yes | O(b^d) | Shortest path, unit-cost grids |
| **DFS** | Uninformed | No | Yes (finite) | O(b^m) | Memory-limited exploration |
| **Dijkstra** | Uninformed | Yes | Yes | O((V+E) log V) | Weighted graphs, no heuristic |
| **A\*** | Informed | Yes (admissible h) | Yes | O(b^d) | Fastest optimal search with heuristic |

### Sensor Fusion for Autonomy
Camera and LiDAR sensing are complementary — real autonomous systems combine both:
- **Camera** → object classification, lane detection, traffic sign recognition
- **LiDAR** → precise obstacle ranging, 3D mapping, localization
- **Search algorithms** → act on the fused perception to plan safe, efficient paths

## 🔬 Advanced Extensions

For future exploration, consider:
1. **YOLOv8 / Real-Time SLAM**: Upgrading to modern detection architectures or simultaneous localization and mapping
2. **3D LiDAR Simulation**: Extending to full 3D point cloud processing with Open3D
3. **RRT / RRT\***: Sampling-based motion planning for continuous, high-dimensional spaces
4. **Sensor Fusion**: Combining camera and LiDAR data using Kalman filtering or deep multimodal models
5. **Reinforcement Learning Control**: Replacing classical search with learned policies (e.g., DQN, PPO)

## 📚 References
- YOLOv3: [Redmon & Farhadi, 2018](https://arxiv.org/abs/1804.02767)
- A\* Search: [Hart, Nilsson & Raphael, 1968](https://ieeexplore.ieee.org/document/4082128)
- LiDAR Sensing Fundamentals: [Thrun, Burgard & Fox — Probabilistic Robotics](http://www.probabilistic-robotics.org/)
- OpenCV DNN Module: [Official Documentation](https://docs.opencv.org/master/d2/d58/tutorial_table_of_content_dnn.html)
- Shapely Geometry: [Official Documentation](https://shapely.readthedocs.io/)
