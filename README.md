# spherical-harmonic-magnetic-field-analysis
Spherical harmonic / GLM analysis of magnetic-field gradients with bootstrap uncertainty, position-error studies, and false-EDM estimates.
# Spherical Harmonic Magnetic Field Analysis and Uncertainty Quantification

## Overview

This repository contains Python tools for magnetic-field analysis using spherical harmonic expansions and generalized linear model (GLM) fitting. The framework extracts spherical harmonic coefficients (G_l,m), estimates coefficient uncertainties using bootstrap resampling, studies the impact of measurement-position uncertainties, and evaluates false-EDM systematic effects.

## Scientific Motivation

Precise characterization of magnetic-field gradients is essential for reducing systematic uncertainties in neutron electric dipole moment (nEDM) experiments. This project investigates the extraction and uncertainty quantification of spherical harmonic coefficients from magnetic-field measurements.

## Methods

* Spherical harmonic basis functions
* Generalized Linear Model (GLM) fitting
* Bootstrap uncertainty estimation
* Position uncertainty studies

  * Radial offsets
  * Azimuthal offsets
  * Height offsets
* False-EDM calculations

## Example Results

* Extraction of G_l,m coefficients up to selected harmonic order
* Bootstrap uncertainty estimates for each coefficient
* Sensitivity of gradients to position errors
* False-EDM systematic estimates

## Author

Prakash Adhikari
Department of Physics and Astronomy
University of Kentucky
