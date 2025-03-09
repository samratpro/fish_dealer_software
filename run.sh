#!/bin/bash
cd "$(dirname "$0")"  # Ensure script runs from correct directory

# Set Python Path to include external dependencies
export PYTHONPATH="$(pwd)/external_libs"

# Run decryptor
./python/python3 app/decryptor.py