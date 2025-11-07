#!/bin/bash
# Build and check script for types-MaterialX

set -e

echo "1. Cleaning previous builds"
rm -rf dist/ build/ *.egg-info

echo ""
echo "2. Building distributions"
python -m build

echo ""
echo "3. Checking distributions with twine"
python -m twine check dist/*

echo ""
echo "4. Build distribution complete:"
ls -lh dist/
