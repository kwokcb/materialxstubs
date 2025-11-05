#!/usr/bin/env bash
# cleanup.sh - Clean build artifacts and old structure
# Works on Linux, macOS, and Windows (Git Bash)

set -e  # Exit on error

echo "=========================================="
echo "Cleaning materialxstubs Build Artifacts"
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
safe_remove "materialxstubs.egg-info"
safe_remove ".mypy_cache"
safe_remove "dist"
safe_remove "__pycache__"

echo "- Removing stubs..."
safe_remove "MaterialX"

# Uninstall package
echo "- Uninstalling materialxstubs package..."
if pip show materialxstubs > /dev/null 2>&1; then
    pip uninstall materialxstubs -y
    echo "✓ Package uninstalled"
else
    echo "✓ Package not installed (skipping)"
fi

echo "- Cleanup complete!"
echo "Remaining structure:"
ls -la | grep -E "^d|pyproject.toml|MaterialX/" || true
echo ""
echo "Next step: Run ./setup.sh to generate and install stubs"
