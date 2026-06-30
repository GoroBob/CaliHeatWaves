# CaliHeatWaves

A three-layer epidemiological study on heat-related morbidity and mortality in Santiago de Cali, Colombia, with emphasis on the Aguablanca district (comunas 13, 14, 15, 21).

## Rationale

Cali is a tropical city with persistent intra-urban heat heterogeneity. Low-income, densely built areas like Aguablanca experience significantly higher temperatures due to limited tree canopy, high surface imperviousness, and proximity to industrial zones. Despite growing recognition of urban heat as a public health threat in the Global South, Cali lacks a systematic characterization of local heatwave-mortality associations. This repository integrates satellite-derived surface temperatures, station-based measurements, and vital statistics to quantify heat stress patterns and their health impacts at the neighborhood level.

## Three Research Layers

- **Layer 1 — Climatology**: Heat-stress characterization for Cali 2000–2024 using ERA5-Land, MODIS land-surface temperature, and ground-based IDEAM/CVC station data. Establishes local heatwave and tropical-night thresholds following WHO/WMO 2015 guidance.

- **Layer 2 — Mortality**: Descriptive spatial epidemiology of cardiovascular, renal, respiratory, and all-cause mortality by comuna using DANE Estadísticas Vitales (EEVV) microdata, stratified by age and sex.

- **Layer 3 — Attribution**: Distributed Lag Non-Linear Model (DLNM) linking Layer 1 exposure metrics to Layer 2 outcomes, stratified by comuna, to quantify excess mortality attributable to heat.

## Repository Structure

```
CaliHeatWaves/
├── shared/
│   ├── data/
│   │   ├── raw/
│   │   ├── interim/
│   │   └── processed/
│   ├── geography/
│   └── references/
├── layer1_climatology/
│   ├── notebooks/
│   ├── src/
│   ├── outputs/
│   └── manuscript/
├── layer2_mortality/
│   ├── notebooks/
│   ├── src/
│   ├── outputs/
│   └── manuscript/
├── layer3_attribution/
│   ├── notebooks/
│   ├── src/
│   ├── outputs/
│   └── manuscript/
└── docs/
```

## How to Use

Each layer is independent and self-contained. Start with the `notebooks/` folder in your target layer:
- **Layer 1**: Begin with `layer1_climatology/notebooks/` for exploratory climate analysis and threshold derivation.
- **Layer 2**: Begin with `layer2_mortality/notebooks/` for mortality trend and spatial distribution analysis.
- **Layer 3**: Begin with `layer3_attribution/notebooks/` for lag-response modeling and risk attribution.

Shared data, geography files, and references live in the `shared/` directory. Consult `docs/` for methods, data sources, and terminology.
