#!/bin/bash
# Quick start script for CaliHeatWaves project

set -e

echo "🌍 CaliHeatWaves Quick Start"
echo "============================"
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate venv
echo "🔌 Activating environment..."
source venv/bin/activate

# Upgrade pip
echo "📥 Upgrading pip..."
pip install --upgrade pip setuptools wheel --quiet

# Install requirements
echo "📚 Installing dependencies..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✓ Dependencies installed"
else
    echo "⚠️  requirements.txt not found"
    exit 1
fi

# Verify installation
echo ""
echo "🧪 Verifying installation..."
python -c "import pandas, xarray, geopandas, numpy; print('✓ All core packages imported successfully')" 2>/dev/null && {
    echo ""
    echo "✅ Environment setup complete!"
    echo ""
    echo "To activate the environment in future sessions, run:"
    echo "  source venv/bin/activate"
    echo ""
    echo "To start Jupyter Lab:"
    echo "  jupyter lab"
    echo ""
} || {
    echo "⚠️  Some packages may not have installed correctly"
    echo "Try running: pip install -r requirements.txt"
    exit 1
}
