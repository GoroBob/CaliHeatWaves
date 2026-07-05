"""Download one year of ERA5-Land hourly data for Cali.
Splits by variable × month. Unpacks Copernicus zips on arrival.
Edit YEAR and run.
"""
import cdsapi, time, zipfile
from pathlib import Path


YEAR = "2000"
AREA = [3.55, -76.65, 3.35, -76.45]          # N, W, S, E
VARS = {"2m_temperature": "t2m", "2m_dewpoint_temperature": "d2m"}
PAUSE = 30

OUT = Path(__file__).resolve().parents[2] / "shared/data/raw/era5" / YEAR
OUT.mkdir(parents=True, exist_ok=True)
client = cdsapi.Client()

def unpack(path: Path):
    if open(path, "rb").read(4) != b"PK\x03\x04":
        return
    with zipfile.ZipFile(path) as z:
        inner = next(m for m in z.namelist() if m.endswith(".nc"))
        z.extract(inner, path.parent)
    path.unlink()
    (path.parent / inner).rename(path)

jobs = [(v, s, m) for v, s in VARS.items() for m in range(1, 13)]
for i, (var, short, month) in enumerate(jobs, 1):
    target = OUT / f"era5_land_cali_{YEAR}_{month:02d}_{short}.nc"
    if target.exists():
        print(f"[{i:>2}/{len(jobs)}] skip {target.name}")
        continue
    print(f"[{i:>2}/{len(jobs)}] {var} {YEAR}-{month:02d}...", flush=True)
    client.retrieve("reanalysis-era5-land", {
        "variable": [var], "year": YEAR, "month": f"{month:02d}",
        "day": [f"{d:02d}" for d in range(1, 32)],
        "time": [f"{h:02d}:00" for h in range(0, 24)],
        "area": AREA, "data_format": "netcdf",
    }, str(target))
    unpack(target)
    print(f"           done ({target.stat().st_size/1e6:.2f} MB)")
    if i < len(jobs):
        time.sleep(PAUSE)

print(f"\nDone {YEAR}: {len(list(OUT.glob('*.nc')))} files")