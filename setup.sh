#!/bin/bash
# Workshop Setup Script
# This script creates symbolic links to the Workshop_EdgeAI submodule

echo "Setting up workshop directory symbolic links..."

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if lib/Workshop_EdgeAI exists
if [ ! -d "lib/Workshop_EdgeAI" ]; then
    echo "Error: lib/Workshop_EdgeAI not found. Please run 'git submodule update --init --recursive' first."
    exit 1
fi

# Create symbolic links for each workshop folder
workshops=("3.1" "3.2" "5.1" "5.4")

for workshop in "${workshops[@]}"; do
    # Remove existing symlink/directory if it exists
    if [ -e "$workshop" ] || [ -L "$workshop" ]; then
        echo "Removing existing $workshop..."
        rm -rf "$workshop"
    fi
    
    # Create the symbolic link
    target="lib/Workshop_EdgeAI/$workshop"
    if [ -d "$target" ]; then
        echo "Creating symlink: $workshop -> $target"
        ln -s "$target" "$workshop"
        if [ $? -eq 0 ]; then
            echo "[OK] Successfully created $workshop"
        else
            echo "[FAIL] Failed to create $workshop"
        fi
    else
        echo "[WARNING] $target does not exist, skipping"
    fi
done

echo ""
echo "Setup complete!"
echo "The workshop folders (3.1, 3.2, 5.1, 5.4) are now linked to lib/Workshop_EdgeAI"
