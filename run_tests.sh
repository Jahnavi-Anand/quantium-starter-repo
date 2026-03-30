#!/bin/bash

# Exit immediately if any command fails
set -e

echo "🔧 Activating virtual environment..."

# Activate venv (Windows Git Bash / WSL compatible)
source venv/Scripts/activate

echo "🧪 Running tests..."

# Run pytest
pytest

# If pytest passes, script continues → success
echo "✅ All tests passed!"
exit 0

# If pytest fails, script will stop due to 'set -e'
# and return exit code 1 automatically