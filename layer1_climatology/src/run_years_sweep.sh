#!/bin/bash
# Loops the ERA5-Land download over a list of years.
# Requires the caliheatwaves env to be active.
# Safe to Ctrl-C and re-run — skip-if-exists handles resume.
#
# Usage:  bash layer1_climatology/src/run_years_sweep.sh

set -e  # stop on any error other than the retries cdsapi handles internally

# --- configuration ---
YEARS=(2012 2011 2010 2009 2008 2007 2006 2005 2004 2003 \
       2002 2001 2000)
PAUSE_BETWEEN_YEARS_MIN=5   # <-- edit this. Your call.
SCRIPT="layer1_climatology/src/02_download_era5_year.py"

# --- sanity checks ---
if ! command -v python &> /dev/null; then
    echo "ERROR: python not found. Is the caliheatwaves env active?"
    exit 1
fi

if [ ! -f "$SCRIPT" ]; then
    echo "ERROR: $SCRIPT not found. Run this from the repo root."
    exit 1
fi

# --- run ---
TOTAL=${#YEARS[@]}
START=$(date +%s)

for i in "${!YEARS[@]}"; do
    YEAR=${YEARS[$i]}
    NUM=$((i + 1))
    echo ""
    echo "############################################"
    echo "# YEAR $NUM/$TOTAL: $YEAR"
    echo "# Started at: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "############################################"

    # Edit YEAR in the Python script in place
    sed -i "s/^YEAR = .*/YEAR = \"$YEAR\"/" "$SCRIPT"

    # Run it
    python "$SCRIPT"

    # Pause before next year (skip pause after last one)
    if [ $NUM -lt $TOTAL ]; then
        echo ""
        echo "Year $YEAR done. Pausing ${PAUSE_BETWEEN_YEARS_MIN} min before next year..."
        sleep $((PAUSE_BETWEEN_YEARS_MIN * 60))
    fi
done

# --- summary ---
END=$(date +%s)
DURATION=$(( (END - START) / 60 ))
echo ""
echo "############################################"
echo "# ALL YEARS COMPLETE"
echo "# Total wall time: ${DURATION} minutes"
echo "############################################"