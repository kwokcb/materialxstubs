#!/usr/bin/env bash
# cleanup.sh - Clean build artifacts and old structure
# Works on Linux, macOS, and Windows (Git Bash)

set -e  # Exit on error

echo "=========================================="
echo "Cleaning types-MaterialX Build Artifacts"
echo "=========================================="
echo ""

# Function to safely remove directories
safe_remove() {
    if [ -d "$1" ]; then
        echo "Removing $1..."
        rm -rf "$1"
    else
        echo "Skipping $1 (not found)"
    fi
}

echo "- Removing build artifacts..."
safe_remove "build"
safe_remove "types-MaterialX.egg-info"
safe_remove ".mypy_cache"
safe_remove "dist"
safe_remove "__pycache__"

echo "- Removing stubs..."
safe_remove "MaterialX"
safe_remove "MaterialX-stubs"
safe_remove "temp_stubs"

# Uninstall package
echo "- Uninstalling types-MaterialX package..."
if pip show types-MaterialX > /dev/null 2>&1; then
    pip uninstall types-MaterialX -y
    echo "✓ Package uninstalled"
else
    echo "✓ Package not installed (skipping)"
fi

echo "- Cleanup complete!"
echo "Remaining structure:"
ls -la | grep -E "^d|pyproject.toml|MaterialX/" || true
echo ""
echo "Next step: Run ./setup.sh to generate and install stubs"
