# MaterialX Type Stub Generator

Logic to create PEP 561 type stubs for [MaterialX](https://materialx.org/) 
- Enables IntelliSense, autocomplete, and type checking for MaterialX in Python IDEs.
- The sample stubs are based on head of version `1.39.5`. 
- The repo can be cloned to create stubs for the desired MaterialX install.

## Installation

### Standard Installation

For MaterialX versions available on PyPI (1.39.4 and earlier):

```bash
pip install .
```

### Installation with Local MaterialX (1.39.5+)

If you have a locally built MaterialX version (e.g., 1.39.5) that's not yet on PyPI:

```bash
# First, ensure your local MaterialX is installed
pip install /path/to/your/MaterialX

# Then install types-MaterialX without build isolation
pip install --no-build-isolation .
```

**Note:** The `--no-build-isolation` flag tells pip to use your current environment's MaterialX installation during the build process, rather than creating an isolated build environment with only PyPI packages.

### VS Code Setup

```bash
pip install .
# Reload VS Code: Ctrl+Shift+P → "Developer: Reload Window"
```

**Requirements:** Python and Pylance extension

## Included Modules

- PyMaterialXCore
- PyMaterialXFormat
- PyMaterialXGenShader 
   - PyMaterialXGenGlsl
   - PyMaterialXGenOsl 
   - PyMaterialXGenMsl
   - PyMaterialXGenMdl
- PyMaterialXRender 
   - PyMaterialXRenderGlsl 
   - PyMaterialXRenderOsl 
- colorspace 
- datatype 
- main 

## Development

### Building Stubs

Stubs can be rebuild using:
```bash
./setup.sh  # Generate stubs, build wheel, and install
```

Then installed using again using `pip`

### Clean Up

This will remove all build artifacts including generated stubs:
```bash
cleanup.sh  # Clean build and stubs
```
