from setuptools import build_meta as _orig
import subprocess
import sys
from pathlib import Path

# Run stubgen before any build
print("Producing stubs for MaterialX.")
python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
print("Using Python version:", python_version)

import shutil
project_root = Path(__file__).parent
target_dir = project_root / "MaterialX-stubs"

# Remove existing MaterialX-stubs directory if it exists
if target_dir.exists():
    shutil.rmtree(target_dir)

# Generate stubs - stubgen will create MaterialX/ directory
subprocess.check_call([
    "stubgen",
    "-p", "MaterialX",
    "-o", ".",
    "--include-docstrings",
    "-v"
])

# Rename MaterialX to MaterialX-stubs for PEP 561 compliance
source_dir = project_root / "MaterialX"
if source_dir.exists():
    shutil.move(str(source_dir), str(target_dir))
    print(f"Renamed MaterialX to MaterialX-stubs")

print(f"Stubs generated in: {target_dir}")

# Add PEP 561 marker
marker = target_dir / "py.typed"
marker.touch(exist_ok=True)
print(f"Created marker file: {marker}")

# Expose all the standard build backend hooks
build_wheel = _orig.build_wheel
build_sdist = _orig.build_sdist
get_requires_for_build_wheel = _orig.get_requires_for_build_wheel
get_requires_for_build_sdist = _orig.get_requires_for_build_sdist
prepare_metadata_for_build_wheel = _orig.prepare_metadata_for_build_wheel
