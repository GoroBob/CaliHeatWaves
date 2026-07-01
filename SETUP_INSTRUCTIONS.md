# Environment Setup Instructions for CaliHeatWaves

## ⚠️ Problem Solved
The old conda (v4.11.0) with complex geospatial dependencies was causing hangs.

## ✅ Recommended Approach: Python venv + pip (FAST)

If the conda environment is taking too long, use this instead:

```bash
# 1. Create a fresh virtual environment
python3.11 -m venv venv
# If python3.11 not available: python -m venv venv

# 2. Activate it
source venv/bin/activate

# 3. Upgrade pip first
pip install --upgrade pip setuptools wheel

# 4. Install dependencies (this is MUCH faster than conda)
pip install -r requirements.txt

# 5. You're done!
python --version
```

### Why this works better:
- **No dependency resolver hang**: pip uses a simpler resolver
- **Faster**: Binary wheels download much faster than conda builds
- **Less memory**: Doesn't consume as much RAM during installation
- **Reliable**: Works even with old conda/pip versions

## Alternative: Conda (if you want to use conda)

We've optimized `environment.yml` with:
- Pinned versions for stability
- All packages from conda-forge
- Geospatial packages configured for conda

```bash
conda env create -f environment.yml
conda activate caliheatwaves
```

**This may still take 5-10 minutes** due to conda's dependency solver, but should complete without freezing.

## Next Steps

Once activated (via either method):

```bash
# Test the environment
python -c "import pandas, xarray, geopandas; print('✓ All packages imported successfully')"

# Start Jupyter (optional)
jupyter lab
```

## Which method to use?

| Method | Speed | Stability | Memory | Recommendation |
|--------|-------|-----------|--------|-----------------|
| **venv + pip** | ⚡ Fast (2-5 min) | ✅ High | 💚 Low | ✅ **START HERE** |
| **conda** | 🐢 Slow (5-10 min) | ✅ High | 🟡 Medium | If you prefer conda |

---

**Created**: 2026-07-01  
**Project**: CaliHeatWaves Climate-Health Epidemiology  
**Python**: 3.11 (tested), 3.10+ (supported)
