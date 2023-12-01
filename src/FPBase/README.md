GPT-4 Response:
# Protein Fluorescence Predictor 2D: Preprocessing Pipeline

## Overview

This project involves a series of scripts designed to fetch, filter, and preprocess protein data from the FPbase. The end goal is to prepare the data for analysis, which includes machine learning tasks. Below, you will find descriptions for each script along with the expected outputs.

## Prerequisites

To run these scripts, you will need:

- Python 3.11
- R programming environment (for `6_rcpi.r`)
- Required Python libraries: `requests`, `json`, `csv`, `os`, `pandas`
- Required R packages: `Rcpi`

## Script Descriptions

### 1. `1_getFPBaseProteins.py`

This script fetches protein data from the FPbase using a GraphQL API. It saves the fetched data as `proteins.json`.

### 2. `2_removeNans.py`

Takes `proteins.json` as input and removes entries with empty sequences or without 'EM' type spectra. The resulting filtered dataset is stored as `filtered_proteins.json`.

### 3. `3_json2csv.py`

Converts the filtered protein data (`filtered_proteins.json`) to a comma-separated value (CSV) format, creating `proteins_info.csv`. Augmenting this, it saves individual spectra data for each protein to separate CSV files within a `spectra/` directory.

### 4. `4_cleanup.py`

Performs cleanup operations on `proteins_info.csv`, focusing on correcting or removing cells that only contain "[]".

### 5. `5_normalizeSpectra.py`

Adjusts the spectra data files to have a uniform wavelength range, filling in missing wavelength values with zeroes. The adjusted spectra are stored in the `adjusted_spectra/` directory.

### 6. `6_rcpi.r`

Utilizes the `Rcpi` R package to extract the pseudo-amino acid composition (PAAC) of the protein sequences from `proteins_info.csv`, saving the results to `proteins_paac.csv`.

### 7. `7_NN.py`

(This file is mentioned in the list but not included in the details provided. As such, we can infer that this script is expected to construct or train a neural network model and save it as `mlp_model.h5`).

## Usage

To run the scripts, navigate to the folder containing them, and execute each one sequentially:

```shell
python3 1_getFPBaseProteins.py
python3 2_removeNans.py
python3 3_json2csv.py
python3 4_cleanup.py
python3 5_normalizeSpectra.py
Rscript 6_rcpi.r
```

Make sure to have the necessary Python and R dependencies installed in your environment.

## Outputs

The scripts will output the following files:

- `proteins.json`: Contains the raw protein data fetched from FPbase.
- `filtered_proteins.json`: Contains the protein data after removing entries with NAN values.
- `proteins_info.csv`: Contains processed protein data in CSV format.
- `adjusted_spectra/`: Directory containing normalized spectra CSV files per protein.
- `proteins_paac.csv`: Contains extracted feature sets derived from protein sequences using PAAC.


---

