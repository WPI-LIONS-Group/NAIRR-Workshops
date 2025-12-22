# NAIRR-Workshops

![Workshop Diagram](imgs/Diagram.png)

## About

This repository includes workshop materials that reference the [Workshop_EdgeAI](https://github.com/lc-leonardo/Workshop_EdgeAI) repository. The workshop folders (3.1, 3.2, 5.1, 5.4) are created as symbolic links (Mac/Linux) or directory junctions (Windows) to a single submodule located in `lib/Workshop_EdgeAI`.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone --recurse-submodules https://github.com/Brian/NAIRR-Workshops.git
cd NAIRR-Workshops
```

If you've already cloned without submodules, initialize them:

```bash
git submodule update --init --recursive
```

### 2. Create Workshop Links

Run the appropriate setup script for your operating system:

**Windows (PowerShell):**
```powershell
.\setup.ps1
```

**Mac/Linux (Bash):**
```bash
chmod +x setup.sh
./setup.sh
```

This will create links for the workshop folders (3.1, 3.2, 5.1, 5.4) pointing to the corresponding directories in `lib/Workshop_EdgeAI`.

### Updating Submodules

To update the submodule to the latest version:

```bash
git submodule update --remote
```