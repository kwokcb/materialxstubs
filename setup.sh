echo "Producing stubs for MaterialX..."

# Remove existing stubs
rm -rf MaterialX-stubs

# Generate stubs - stubgen creates MaterialX/ directory
stubgen -p MaterialX -o . --include-docstrings -v

# Rename to MaterialX-stubs for PEP 561 compliance
mv MaterialX MaterialX-stubs

# Add PEP 561 marker
touch MaterialX-stubs/py.typed

echo "Stub generation completed in MaterialX-stubs/"
