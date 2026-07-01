# Quick Environment Activation Guide

## 🚀 TL;DR - Start Here

```bash
cd /home/boris/PycharmProjects/CaliHeatWaves
source venv/bin/activate
jupyter lab
```

## ✅ What's Installed

- Python 3.8.8
- All geospatial/climate packages (xarray, netCDF4, geopandas, rasterio)
- All analysis packages (pandas, numpy, scipy, statsmodels, scikit-learn)
- Jupyter Lab for interactive notebooks
- CDS API client for ERA5 data downloads

## 🔌 Activation

### Every time you open a terminal:
```bash
cd /home/boris/PycharmProjects/CaliHeatWaves
source venv/bin/activate
```

Or use the helper script:
```bash
bash activate_env.sh
```

### Verify activation:
```bash
which python  # Should show: .../venv/bin/python
python --version  # Should show: Python 3.8.8
```

## 📓 Start Working

```bash
# Option 1: Jupyter Lab (interactive notebooks)
jupyter lab

# Option 2: IPython (interactive shell)
ipython

# Option 3: Run Python scripts
python script.py
```

## 🗂️ Project Structure

- **layer1_climatology/** - Heat stress characterization (ERA5, MODIS, stations)
- **layer2_mortality/** - Epidemiological data (DANE vital statistics)
- **layer3_attribution/** - Distributed Lag Non-Linear Models (DLNM)
- **shared/** - Shared data, geography files, references

## 🐛 Troubleshooting

### "command not found: python"
Make sure environment is activated: `source venv/bin/activate`

### "No module named 'pandas'"
Check Python is from venv: `which python` should show `venv/bin/python`

### "Permission denied" on activate_env.sh
```bash
chmod +x activate_env.sh quickstart.sh
```

### Start over (clean reinstall)
```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📊 Data Access

### CDS API (ERA5 downloads)
1. Create account: https://cds.climate.copernicus.eu/
2. Copy your API key from: https://cds.climate.copernicus.eu/how-to-api
3. Create `.cdsapirc` file in home directory:
   ```
   url: https://cds.climate.copernicus.eu/api/v2
   key: YOUR_API_KEY_HERE
   ```

## 📚 Resources

- **Setup Details**: See `ENVIRONMENT_SETUP.md`
- **Setup Methods**: See `SETUP_INSTRUCTIONS.md`
- **Project Info**: See main `README.md`
- **Configuration**: See `.env.example`

---

**Status**: ✅ Ready to use  
**Last Updated**: 2026-07-01  
**Python**: 3.8.8 via venv  
**Location**: `/home/boris/PycharmProjects/CaliHeatWaves/venv`
