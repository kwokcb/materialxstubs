from setuptools import build_meta as _orig
import subprocess
import sys
from pathlib import Path

# Run stubgen before any build (same command as in setup.sh)
print("Producing stubs for MaterialX.")
python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
print("Using Python version:", python_version)
subprocess.check_call([
    "stubgen",
    "-p", "MaterialX",
    "-o", ".",
    "--include-docstrings",
    "-v"
])
print("Stub generation completed.")

# Add PEP 561 marker
project_root = Path(__file__).parent
out_dir = project_root / "MaterialX"
marker = out_dir / "py.typed"
marker.touch(exist_ok=True)
print(f"Created marker file: {marker}")

# Expose all the standard build backend hooks
build_wheel = _orig.build_wheel
build_sdist = _orig.build_sdist
get_requires_for_build_wheel = _orig.get_requires_for_build_wheel
get_requires_for_build_sdist = _orig.get_requires_for_build_sdist
prepare_metadata_for_build_wheel = _orig.prepare_metadata_for_build_wheel
