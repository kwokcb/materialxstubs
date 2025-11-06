#!/usr/bin/env python3
"""
Test script to verify that MaterialX type stubs are properly discoverable.
"""
import sys
import os
from pathlib import Path
import site

def test_stub_discovery():
    print("=" * 70)
    print("MaterialX Type Stub Discovery Test")
    print("=" * 70)
    print()
    
    # 1. Check site-packages locations
    print("1. Site-packages locations:")
    site_packages = site.getsitepackages()
    for sp in site_packages:
        print(f"   - {sp}")
    print()
    
    # 2. Check if MaterialX is installed
    print("2. MaterialX package:")
    try:
        import MaterialX as mx
        print(f"   - MaterialX installed at: {mx.__file__}")
        print(f"   - MaterialX version: {mx.__version__ if hasattr(mx, '__version__') else 'unknown'}")
    except ImportError as e:
        print(f"   ERROR: MaterialX not found: {e}")
        return False
    print()
    
    # 3. Check if MaterialX-stubs directory exists
    print("3. MaterialX-stubs directory:")
    stubs_found = False
    stubs_path = None
    for sp in site_packages:
        potential_path = Path(sp) / "MaterialX-stubs"
        if potential_path.exists() and potential_path.is_dir():
            stubs_found = True
            stubs_path = potential_path
            print(f"   - Found at: {potential_path}")
            
            # List contents
            stub_files = list(potential_path.glob("*.pyi"))
            print(f"   - Contains {len(stub_files)} .pyi files")
            
            # Check for py.typed marker
            py_typed = potential_path / "py.typed"
            if py_typed.exists():
                print(f"   - py.typed marker present")
            else:
                print(f"   ERROR: py.typed marker MISSING")
            
            # List some stub files
            print("   - Sample stub files:")
            for stub in sorted(stub_files)[:5]:
                print(f"      - {stub.name}")
            break
    
    if not stubs_found:
        print("   ✗ MaterialX-stubs NOT FOUND in site-packages")
        return False
    
    # Show sample stub signatures
    if stubs_path:
        print("   - Sample type signatures from stubs:")
        try:
            core_stub = stubs_path / "PyMaterialXCore.pyi"
            if core_stub.exists():
                with open(core_stub, 'r') as f:
                    lines = f.readlines()
                
                # Find Document class and show some method signatures
                in_document_class = False
                document_methods = []
                for i, line in enumerate(lines):
                    if 'class Document(' in line:
                        in_document_class = True
                        continue
                    if in_document_class:
                        if line.startswith('class '):
                            break
                        if '    def ' in line:
                            sig = line.strip()
                            if ' -> ' in sig:
                                method_sig = sig.split('"""')[0].strip()
                                if method_sig and not method_sig.startswith('def __'):
                                    document_methods.append(method_sig)
                                    if len(document_methods) >= 6:
                                        break
                
                if document_methods:
                    print(f"      Document class methods:")
                    for sig in document_methods:
                        sig = sig.replace('MaterialX.PyMaterialXCore.', 'mx.')
                        sig = sig.replace('def ', '  - ')
                        if len(sig) > 95:
                            sig = sig[:92] + "..."
                        print(f"      {sig}")
                    
        except Exception as e:
            print(f"      WARNING: Could not read stub signatures: {e}")
    
    print()
    
    # 4. Note about mypy
    print("4. Mypy compatibility:")
    try:
        import mypy
        print(f"   - Mypy is installed (version: {mypy.__version__ if hasattr(mypy, '__version__') else 'unknown'})")
        print(f"   INFO: Programmatic stub discovery test in section 5 below")
    except ImportError:
        print("   WARNING: Mypy not installed")
        print("   INFO: Install with: pip install mypy")
    print()
    
    # 5. Test sample API methods have type stubs
    print("5. Sample API type information:")
    try:
        import MaterialX as mx
        
        # Test some common MaterialX API methods
        sample_apis = [
            ('createDocument', mx.createDocument),
            ('Element.getName', mx.Element.getName if hasattr(mx, 'Element') else None),
            ('Element.setName', mx.Element.setName if hasattr(mx, 'Element') else None),
            ('Document.addNodeGraph', mx.Document.addNodeGraph if hasattr(mx, 'Document') else None),
        ]

        for api_name, api_func in sample_apis:
            if api_func is None:
                print(f"   WARNING: {api_name}: Not found")
                continue

            # Check if it has annotations
            if hasattr(api_func, '__annotations__') and api_func.__annotations__:
                print(f"   - {api_name}: Has type annotations")
            else:
                # For C++ extension methods, check if stubs exist
                print(f"   - {api_name}: Available (stub types in .pyi files)")

        print()
        
    except Exception as e:
        print(f"   WARNING: Could not test API methods: {e}")
        print()
    
    # 6. Test type checking works
    print("6. Type checking test:")
    print("   Creating test file...")
    test_file = Path(__file__).parent / "test_types_temp.py"
    test_content = """import MaterialX as mx

# Test various MaterialX APIs
doc = mx.createDocument()
doc.setName("MyDocument")
name = doc.getName()

# Create a node graph
graph = doc.addNodeGraph("MyGraph")
graph.setName("TestGraph")

# Test type hints work
def process_document(document: mx.Document) -> str:
    return document.getName()

result = process_document(doc)
"""
    test_file.write_text(test_content)
    
    # Try running mypy on it
    import subprocess
    try:
        result = subprocess.run(
            ["mypy", str(test_file), "--no-error-summary"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print(f"   - Mypy type checking passed")
        else:
            print(f"   ERROR: Mypy found issues:")
            print(f"      {result.stdout}")
            
        # Check if stubs were used (verbose mode)
        verbose_result = subprocess.run(
            ["mypy", str(test_file), "--verbose"],
            capture_output=True,
            text=True,
            timeout=10
        )
        combined_output = verbose_result.stdout + verbose_result.stderr
        if "MaterialX-stubs" in combined_output:
            print(f"   - Mypy is using MaterialX-stubs")
            # Show a sample line
            for line in combined_output.split('\n'):
                if "MaterialX-stubs" in line and ".pyi" in line:
                    print(f"      Example: ...{line[-80:]}")
                    break
        else:
            print(f"   WARNING: Could not confirm stub usage in verbose output")
            
    except FileNotFoundError:
        print(f"   WARNING: Mypy not found in PATH")
    except Exception as e:
        print(f"   WARNING: Could not run mypy: {e}")
    finally:
        # Clean up test file
        if test_file.exists():
            test_file.unlink()
    print()
    
    # Summary
    print("=" * 70)
    print("Summary:")
    if stubs_found:
        print("- MaterialX type stubs are properly installed and discoverable!")
        print(f"- Location: {stubs_path}")
        return True
    else:
        print("ERROR: MaterialX type stubs are NOT properly configured")
        return False

if __name__ == "__main__":
    success = test_stub_discovery()
    sys.exit(0 if success else 1)
