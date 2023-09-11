CREATE TABLE IF NOT EXISTS fluorophores (
    Tag VARCHAR(255),
    Chromophore VARCHAR(255),
    Solvent VARCHAR(255),
    Absorption_max_nm FLOAT,
    Emission_max_nm FLOAT,
    Lifetime_ns FLOAT,
    Quantum_yield FLOAT,
    log_e_mol_1_dm3_cm_1 FLOAT,
    abs_FWHM_cm_1 FLOAT,
    emi_FWHM_cm_1 FLOAT,
    abs_FWHM_nm FLOAT,
    emi_FWHM_nm FLOAT,
    Molecular_weight_g_mol_1 FLOAT,
    Reference TEXT
);
