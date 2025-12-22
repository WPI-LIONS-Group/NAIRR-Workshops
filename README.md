# NAIRR-Workshops

![Workshop Diagram](imgs/Diagram.png)

## About

This repository includes workshop materials that reference the [Workshop_EdgeAI](https://github.com/lc-leonardo/Workshop_EdgeAI) repository as submodules for different workshop sections.

## Cloning the Repository

This repository uses submodules with sparse-checkout to include only specific workshop folders from the [Workshop_EdgeAI](https://github.com/lc-leonardo/Workshop_EdgeAI) repository.

### Clone with submodules

```bash
git clone --recurse-submodules https://github.com/Brian/NAIRR-Workshops.git
cd NAIRR-Workshops
```

### Configure sparse-checkout for submodules

After cloning, configure sparse-checkout to only include the relevant workshop folders:

```bash
# Configure sparse-checkout for each submodule
git -C .git/modules/3.1 config core.sparseCheckout true
echo "3.1/*" > .git/modules/3.1/info/sparse-checkout
cd 3.1 && git read-tree -mu HEAD && cd ..

git -C .git/modules/3.2 config core.sparseCheckout true
echo "3.2/*" > .git/modules/3.2/info/sparse-checkout
cd 3.2 && git read-tree -mu HEAD && cd ..

git -C .git/modules/5.1 config core.sparseCheckout true
echo "5.1/*" > .git/modules/5.1/info/sparse-checkout
cd 5.1 && git read-tree -mu HEAD && cd ..

git -C .git/modules/5.4 config core.sparseCheckout true
echo "5.4/*" > .git/modules/5.4/info/sparse-checkout
cd 5.4 && git read-tree -mu HEAD && cd ..
```

### Updating submodules

To update all submodules to the latest version:

```bash
git submodule update --remote
```