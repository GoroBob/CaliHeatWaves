#!/bin/bash
# Activate the CaliHeatWaves conda environment

eval "$(conda shell.bash hook)"
conda activate caliheatwaves

echo "✓ CaliHeatWaves environment activated!"
echo "  Python: $(python --version)"
echo "  Location: $CONDA_PREFIX"
