# ChemData Processor README

This script handles the processing and organization of chemical data files. 

## Requirements

Make sure to have the following libraries installed:
- `os`
- `csv`
- `pandas`
- `numpy`
- A custom utility (`util`) for loading environment variables.

## Environment Variables

Before running the script, set the following environment variables:
- `DAT`: The path where your data files reside.
- `RES`: (Not used in the provided script, but might be relevant for other purposes)

## Script Execution Breakdown

1. **Define Paths**:
    - Load the environment variables.
    - Set the paths based on the environment variables.

2. **Import Libraries**: 
    - The necessary libraries for processing are imported.

3. **Main Execution**:

    **0. PaDEL Calculations**:
    - Not conducted within the main function. This is due to the extensive computational time it may take.

    **1. Append Headers**:
    - Headers from `headers.csv` are appended to `descriptors_backup.csv` from a specific date, producing a combined CSV named `descriptors_headers.csv`.

    **2. Merge Input with Output**:
    - `descriptors_headers.csv` is merged with `molecules.csv` from a specific date based on a 'Tag' column, producing `train_with_NaN.csv`.

    **3. Remove NaNs**:
    - Any rows containing NaN values in `train_with_NaN.csv` are removed. The cleaned data is written to `train.csv` in a date-specific directory.

    **4. Remove Temporary Files**:
    - This step is commented out in the provided script but is intended for cleaning up any temporary files used during execution.

