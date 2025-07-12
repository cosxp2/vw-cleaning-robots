#!/bin/bash

ROOT_DIR=$(dirname "$(dirname "$0")")
DEFAULT_INPUT="$ROOT_DIR/examples/test_input.txt"
INPUT_FILE=${1:-$DEFAULT_INPUT}

# Run CLI with correct PYTHONPATH
PYTHONPATH="$ROOT_DIR" python "$ROOT_DIR/adapters/cli/main.py" < "$INPUT_FILE"