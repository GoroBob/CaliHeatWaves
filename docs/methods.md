# Methods Overview

This repository follows three methodological anchors that shape the analysis across all layers:

## 1. WHO & WMO Heatwave Guidance (2015)
The *Heatwaves and Health: Guidance on Warning-System Development* report (WHO & WMO, 2015) provides the framework for heatwave definition and public health relevance. We adopt their recommendation to define heatwaves based on *local* rather than absolute temperature thresholds, ensuring definitions reflect the actual physiological stress and adaptive capacity of Cali's population.

## 2. Heatwave Indicator Construction (Gasparrini & Armstrong, 2011)
Gasparrini & Armstrong's methodological work on heat-health associations establishes the statistical foundations for defining heat indices and constructing lagged exposure variables. Their approach informs our construction of apparent temperature metrics and lag-response relationships between heat exposure and health outcomes.

## 3. Tropical Heatwave-Mortality DLNM (Geirinhas et al., 2023)
The Rio de Janeiro heatwave-mortality study by Geirinhas et al. (2023) serves as the closest tropical-climate epidemiological analogue. Their application of distributed lag non-linear models (DLNM) to a tropical city with similar urban heterogeneity and health infrastructure provides both methodological guidance and a comparative benchmark for effect estimates.

---

## ERA5-Land: role and known limitations for Cali

ERA5-Land reanalysis provides gridded meteorological data at approximately 9 km horizontal resolution. While this represents a substantial improvement over coarser operational reanalysis products, Cali's complex topography and small spatial extent present significant methodological constraints. The city spans longitudes −76.56 to −76.46°W—a distance of only ~10 km, comparable to ERA5-Land's grid spacing. The Farallones de Cali (western Cordillera Occidental), which rise to ~4,000 m elevation within 10–15 km west of the city centre, are substantially undersampled by the coarse grid. Although the Cordillera Central to the east (~−76.0°W) is somewhat better resolved within this bounding box, the grid averaging still obscures complex microtopography. Most critically, intra-urban temperature gradients—such as the contrast between heat-vulnerable peripheral neighbourhoods (e.g., Aguablanca) and cooler central or hilltop areas (e.g., San Antonio), which are separated by only 5–10 km—fall entirely below ERA5-Land's resolution threshold.

Consequently, Layer 1 uses ERA5-Land exclusively for *temporal* analysis (detection of heatwaves and computation of temperature percentile thresholds) at a single reference point (3.45°N, −76.53°W, central Cali). The wider grid box is retained for contextual spatial maps only. Explicit resolution of intra-urban spatial temperature contrasts is deferred to Layer 3, which employs MODIS Land Surface Temperature data at 1 km resolution.

### Consequences for analysis

- Temporal thresholds for heatwave identification and tropical-night percentiles are computed at the single reference point (3.45°N, −76.53°W), not spatially gridded across the city.
- The wider ERA5-Land grid box is retained for contextual spatial visualizations only; it does not constrain heatwave thresholds or health outcome attribution.
- Intra-urban spatial variation in heat exposure is explicitly addressed in Layer 3 using MODIS LST (1 km), which resolves neighbourhood-scale gradients and enables stratified health outcome analysis by residential heat exposure.
