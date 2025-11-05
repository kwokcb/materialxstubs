# MaterialX Type Stub Generator

Logic to create PEP 561 type stubs for [MaterialX](https://materialx.org/) 
- Enables IntelliSense, autocomplete, and type checking for MaterialX in Python IDEs.
- The sample stubs are based on head of version `1.39.5`. 
- The repo can be clone to create stubs for the desired MaterialX install.

## Installation

```bash
pip install .
```

This will install required packages and build the stubs using the
`stubgen` package.

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
