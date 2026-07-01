#!/bin/bash
# Activate CaliHeatWaves Python 3.11 environment via micromamba

export PATH=~/.local/bin:$PATH
eval "$($HOME/.local/bin/micromamba shell hook -s bash)"
micromamba activate caliheatwaves

echo "✓ CaliHeatWaves environment (Python 3.11) activated"
echo "  Python: $(python --version)"
echo "  Location: $(python -c 'import sys; print(sys.prefix)')"
