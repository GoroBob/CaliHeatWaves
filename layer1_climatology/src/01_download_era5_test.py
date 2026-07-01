import cdsapi
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[2] / "shared" / "data" / "raw" / "era5"
OUT_DIR.mkdir(parents=True, exist_ok=True)

c = cdsapi.Client()

year = "2024"  # test pull, single year
target = OUT_DIR / f"era5_land_cali_{year}.nc"

c.retrieve(
    "reanalysis-era5-land",
    {
        "variable": ["2m_temperature", "2m_dewpoint_temperature"],
        "year": year,
        "month": [f"{m:02d}" for m in range(1, 13)],
        "day": [f"{d:02d}" for d in range(1, 32)],
        "time": [f"{h:02d}:00" for h in range(0, 24)],
        "area": [4.0, -77.0, 3.0, -76.0],  # N, W, S, E
        "format": "netcdf",
    },
    str(target),
)

print(f"Downloaded → {target}")