"""
This file contains an example for running the `convert_indices` and
`write_lhalo_binary` functions within`converter.py`.  Refer to the
documentation of those function for full explanation of each variable.

The default parameters are chosen to match the ASTRO3D Genesis trees as
produced by VELOCIraptor + Treefrog.
"""
#!/usr/bin:env python
from __future__ import print_function
from astro3D.genesis.utils import convert_indices as converter

import numpy as np


if __name__ == '__main__':

    fname_in = "/fred/oz004/jseiler/astro3d/nov2018/N1024_sorted.hdf5"
    fname_out = "/fred/oz004/jseiler/astro3d/nov2018/N1024_lhalo_indices.hdf5"

    haloID_field = "ID"
    forestID_field = "ForestID"
    sort_fields = ["ForestID", "hostHaloID", "Mass_200mean"]
    sort_direction = np.array([1, 1, -1])
    ID_fields = ["Head", "Tail", "RootHead", "RootTail", "ID", "hostHaloID"]
    index_mult_factor = 1e12

    converter.convert_indices(fname_in, fname_out,
                              haloID_field, forestID_field,
                              ID_fields, index_mult_factor)
