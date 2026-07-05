"""
Test download: ERA5-Land 2m temperature for Cali, January 2024.
Small request to verify authentication, license acceptance, and full pipeline.
"""
import cdsapi
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[2] / "shared" / "data" / "raw" / "era5"
OUT_DIR.mkdir(parents=True, exist_ok=True)

target = OUT_DIR / "era5_land_cali_2024_01_test.nc"

c = cdsapi.Client()

c.retrieve(
    "reanalysis-era5-land",
    {
        "variable": ["2m_temperature"],
        "year": "2024",
        "month": "01",
        "day": [f"{d:02d}" for d in range(1, 32)],
        "time": [f"{h:02d}:00" for h in range(0, 24)],
        "area": [4.0, -77.0, 3.0, -76.0],  # N, W, S, E — Cali box
        "data_format": "netcdf",
    },
    str(target),
)

print(f"Downloaded → {target}")