# spherical-harmonic-magnetic-field-analysis
Spherical harmonic / GLM analysis of magnetic-field gradients with bootstrap uncertainty, position-error studies, and false-EDM estimates.
# Spherical Harmonic Magnetic Field Analysis and Uncertainty Quantification

## Overview

This repository contains Python tools for magnetic-field analysis using spherical harmonic expansions and generalized linear model (GLM) fitting. The framework extracts spherical harmonic coefficients (G_l,m), estimates coefficient uncertainties using bootstrap resampling, studies the impact of measurement-position uncertainties, and evaluates false-EDM systematic effects.

## Scientific Motivation

Precise characterization of magnetic-field gradients is essential for reducing systematic uncertainties in neutron electric dipole moment (nEDM) experiments. This project investigates the extraction and uncertainty quantification of spherical harmonic coefficients from magnetic-field measurements.

## Methods

* Construction of spherical harmonic basis functions up to a selected maximum harmonic order, (l_{\max})
* Determination of harmonic expansion coefficients (G_{l,m}) through linear least-squares fitting
* Bootstrap resampling for statistical uncertainty estimation of the extracted coefficients
* Position uncertainty studies, including:

  * Radial offsets
  * Azimuthal offsets
  * Vertical (height) offsets
* Evaluation of false-EDM systematic effects arising from magnetic-field gradients

## Results

* Extraction of harmonic coefficients (G_{l,m}) up to a selected harmonic order (l_{\max})

* Bootstrap uncertainty estimates reported as

  (G_{l,m} \pm \sigma(G_{l,m}))

* Quantification of the sensitivity of gradient coefficients to measurement-position uncertainties

* Evaluation of systematic shifts associated with radial, azimuthal, and vertical position errors

* Estimation of false-EDM contributions arising from magnetic-field nonuniformities


## Author

Prakash Adhikari
Department of Physics and Astronomy
University of Kentucky
