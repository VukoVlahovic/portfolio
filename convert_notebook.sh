#!/bin/bash
# Notebook Conversion Script
# Usage: ./convert_notebook.sh notebook_name.ipynb

if [ -z "$1" ]; then
    echo "Usage: ./convert_notebook.sh notebook_name.ipynb"
    echo "Example: ./convert_notebook.sh sample_data_analysis.ipynb"
    exit 1
fi

NOTEBOOK_NAME=$1
NOTEBOOK_PATH="notebooks/$NOTEBOOK_NAME"
OUTPUT_DIR="templates/notebooks"

if [ ! -f "$NOTEBOOK_PATH" ]; then
    echo "Error: Notebook file '$NOTEBOOK_PATH' not found!"
    exit 1
fi

echo "Converting $NOTEBOOK_NAME to HTML..."
jupyter nbconvert --to html "$NOTEBOOK_PATH" --output-dir="$OUTPUT_DIR"

if [ $? -eq 0 ]; then
    echo "✓ Conversion successful!"
    echo "✓ HTML file saved to: $OUTPUT_DIR/${NOTEBOOK_NAME%.ipynb}.html"
    echo ""
    echo "Access it at: http://localhost:5000/notebooks/${NOTEBOOK_NAME%.ipynb}.html"
else
    echo "✗ Conversion failed!"
    exit 1
fi
