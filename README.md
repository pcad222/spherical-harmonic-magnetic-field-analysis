# Spherical Harmonic Analysis of Magnetic Fields for nEDM Gradient Characterization

This repository contains Python tools for the characterization of magnetic fields through spherical harmonic decomposition. The analysis framework was developed for studies of magnetic-field gradients and systematic effects relevant to neutron electric dipole moment (nEDM) experiments.

---

## Physics Motivation

The search for a permanent neutron electric dipole moment requires precise control and characterization of magnetic-field nonuniformities. Spatial magnetic-field gradients can produce frequency shifts that mimic an EDM signal and therefore constitute an important source of systematic uncertainty.

To quantify these effects, measured magnetic fields are expanded in a basis of harmonic modes. The resulting harmonic coefficients are used to characterize the magnetic environment, evaluate field-quality requirements, and estimate false-EDM contributions arising from magnetic-field gradients.

---

## Methods

* Construction of spherical harmonic basis functions up to a selected maximum harmonic order, $l_{\max}$
* Determination of harmonic expansion coefficients $G_{l,m}$ through linear least-squares fitting
* Bootstrap resampling for statistical uncertainty estimation of the extracted coefficients
* Position uncertainty studies including:

  * Radial offsets
  * Azimuthal offsets
  * Vertical (height) offsets
* Evaluation of false-EDM systematic effects arising from magnetic-field gradients

---

## Analysis Components

### Harmonic Decomposition

Magnetic-field measurements are expanded in terms of spherical harmonic basis functions to determine the coefficients $G_{l,m}$ describing the field distribution within the experimental volume.

### Bootstrap Uncertainty Estimation

Statistical uncertainties on the extracted harmonic coefficients are evaluated through repeated resampling of the measurement data.

### Position-Uncertainty Studies

The sensitivity of the extracted harmonic coefficients to measurement-position errors is investigated through controlled radial, azimuthal, and vertical offsets.

### False-EDM Evaluation

Extracted gradient coefficients are propagated to estimate false electric dipole moment signals associated with magnetic-field nonuniformities.

---

## Results

* Extraction of harmonic coefficients $G_{l,m}$ up to a selected harmonic order $l_{\max}$
* Bootstrap uncertainty estimates reported as

$$
G_{l,m} \pm \sigma(G_{l,m})
$$

* Quantification of the sensitivity of gradient coefficients to measurement-position uncertainties
* Evaluation of systematic shifts associated with radial, azimuthal, and vertical position errors
* Estimation of false-EDM contributions arising from magnetic-field nonuniformities

---

## Repository Structure

```text
src/
├── harmonic_basis.py
├── least_squares_fit.py
├── bootstrap.py
├── position_uncertainty.py
└── false_edm.py

notebooks/
├── 01_harmonic_decomposition.ipynb
├── 02_bootstrap_uncertainty.ipynb
├── 03_false_edm_estimation.ipynb
├── 04_radial_uncertainty.ipynb
├── 05_azimuthal_uncertainty.ipynb
└── 06_vertical_uncertainty.ipynb

figures/
data/
```

---

## Representative Outputs

* Harmonic coefficient spectra
* Bootstrap distributions of selected $G_{l,m}$ coefficients
* Gradient sensitivity to mapper-position uncertainties
* False-EDM systematic estimates

---

## Author

Prakash Adhikari

Department of Physics and Astronomy

University of Kentucky
