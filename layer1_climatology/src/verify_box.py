"""
Verify the tight box covers Cali properly by listing which grid cells fall inside.

Uses the existing January 2024 test file's coordinate system to check how many
grid cells the tight box [3.7, -76.8, 3.2, -76.2] will capture, and confirm
the single reference point (3.45°N, -76.53°W) is nearby.

Run this before downloading a full year to ensure coverage is appropriate.
"""

import xarray as xr
from pathlib import Path

# Paths and box definition
# Use extracted NetCDF file (the .nc file is a ZIP archive)
TEST_FILE = (
    Path(__file__).resolve().parents[2]
    / "shared"
    / "data"
    / "raw"
    / "era5"
    / "data_0.nc"
)
if not TEST_FILE.exists():
    # Fallback: look for the zip file and extract if needed
    zip_file = (
        Path(__file__).resolve().parents[2]
        / "shared"
        / "data"
        / "raw"
        / "era5"
        / "era5_land_cali_2024_01_test.nc"
    )
    if zip_file.exists():
        import zipfile
        print(f"Extracting {zip_file.name}...")
        with zipfile.ZipFile(zip_file) as z:
            z.extractall(zip_file.parent)
        print(f"✓ Extracted to {TEST_FILE}")
    else:
        raise FileNotFoundError(f"Neither {TEST_FILE} nor {zip_file} found")
TIGHT_BOX = {
    "lat_min": 3.2,
    "lat_max": 3.7,
    "lon_min": -76.8,
    "lon_max": -76.2,
}
CALI_CENTER = {"lat": 3.45, "lon": -76.53}

# Load test file
print("Loading ERA5 test file to verify tight box coverage...")
ds = xr.open_dataset(TEST_FILE, engine="netcdf4")
if "valid_time" in ds.dims:
    ds = ds.rename({"valid_time": "time"})

lats = ds.latitude.values
lons = ds.longitude.values

# Filter to tight box
lats_in = lats[(lats >= TIGHT_BOX["lat_min"]) & (lats <= TIGHT_BOX["lat_max"])]
lons_in = lons[(lons >= TIGHT_BOX["lon_min"]) & (lons <= TIGHT_BOX["lon_max"])]

# Print summary
print(f"\n{'='*70}")
print(f"TIGHT BOX COVERAGE VERIFICATION")
print(f"{'='*70}")
print(f"\nBox definition (lat min-max, lon min-max):")
print(
    f"  Latitude:  {TIGHT_BOX['lat_min']:6.2f}° to {TIGHT_BOX['lat_max']:6.2f}°N"
)
print(
    f"  Longitude: {TIGHT_BOX['lon_min']:7.2f}° to {TIGHT_BOX['lon_max']:7.2f}°W"
)

print(f"\nGrid cells included:")
print(f"  Latitudes  ({len(lats_in):2d} cells): {lats_in}")
print(f"  Longitudes ({len(lons_in):2d} cells): {lons_in}")
print(f"  Total grid cells: {len(lats_in) * len(lons_in)}")

# Find nearest cell to reference point
nearest_lat_idx = (abs(lats - CALI_CENTER["lat"])).argmin()
nearest_lon_idx = (abs(lons - CALI_CENTER["lon"])).argmin()
nearest_lat = lats[nearest_lat_idx]
nearest_lon = lons[nearest_lon_idx]

print(f"\nReference point (Cali centre):")
print(f"  Target: lat={CALI_CENTER['lat']:.2f}°, lon={CALI_CENTER['lon']:.2f}°")
print(
    f"  Nearest grid cell: lat={nearest_lat:.3f}°, lon={nearest_lon:.3f}°"
)
print(
    f"  Distance: ~{abs(nearest_lat - CALI_CENTER['lat']) * 111:.1f} km (lat), "
    f"~{abs(nearest_lon - CALI_CENTER['lon']) * 111 * 0.8:.1f} km (lon)"
)

# Check if reference point is in tight box
in_box = (
    (nearest_lat >= TIGHT_BOX["lat_min"])
    and (nearest_lat <= TIGHT_BOX["lat_max"])
    and (nearest_lon >= TIGHT_BOX["lon_min"])
    and (nearest_lon <= TIGHT_BOX["lon_max"])
)
status = "✓ IN BOX" if in_box else "✗ OUT OF BOX"
print(f"  Status: {status}")

print(f"\n{'='*70}")
if in_box and len(lats_in) >= 5 and len(lons_in) >= 5:
    print("✓ Tight box covers Cali centre with adequate context margins.")
else:
    print("⚠ Warning: box may be too tight or reference point not covered.")
print(f"{'='*70}\n")
