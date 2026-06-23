"""
Spherical harmonic basis functions for magnetic field analysis.

Author: Prakash Adhikari
University of Kentucky
"""

import numpy as np
from scipy.special import sph_harm


def spherical_harmonic_basis(theta, phi, l, m):
    """
    Compute spherical harmonic Y_l^m.
    """
    return sph_harm(m, l, phi, theta)
